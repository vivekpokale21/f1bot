"""
Service for handling F1 race analysis.
"""

import logging
import numpy as np
import pandas as pd
import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt
import seaborn as sns
from config import Config

logger = logging.getLogger('f1bot')

class RaceAnalysisService:
    """
    Service for analyzing F1 race data.
    """
    
    def __init__(self):
        """Initialize the race analysis service."""
        pass
        
    def get_session(self, year, race, session_type='R'):
        """
        Get a FastF1 session.
        
        Args:
            year: The year of the session
            race: The race name or round number
            session_type: The session type (default: 'R' for race)
            
        Returns:
            fastf1.core.Session: The loaded session
        """
        logger.info(f"Loading session data for {year} {race} {session_type}")
        session = fastf1.get_session(int(year), race, session_type)
        session.load()
        return session
        
    def create_race_pace_plot(self, session, num_drivers=10):
        """
        Create a race pace comparison plot for the top drivers.
        
        Args:
            session: The FastF1 session
            num_drivers: Number of drivers to include (default: 10)
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        # Setup for timedelta support
        fastf1.plotting.setup_mpl(mpl_timedelta_support=True, misc_mpl_mods=False, color_scheme='fastf1')
        
        # Get the top drivers
        point_finishers = session.drivers[:num_drivers]
        driver_laps = session.laps.pick_drivers(point_finishers).pick_quicklaps()
        driver_laps = driver_laps.reset_index()
        
        # Get the finishing order for the plot
        finishing_order = [session.get_driver(i)["Abbreviation"] for i in point_finishers]
        
        # Get driver colors
        driver_colors = fastf1.plotting.get_driver_color_mapping(session=session)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=Config.DEFAULT_FIG_SIZE)
        
        # Convert lap times to seconds for plotting
        driver_laps["LapTime(s)"] = driver_laps["LapTime"].dt.total_seconds()
        
        # Create violin plot
        sns.violinplot(data=driver_laps,
                      x="Driver",
                      y="LapTime(s)",
                      inner=None,
                      scale='area',
                      order=finishing_order,
                      palette=driver_colors
                      )
        
        # Add swarm plot for tire compounds
        sns.swarmplot(data=driver_laps,
                     x="Driver",
                     y="LapTime(s)",
                     order=finishing_order,
                     hue="Compound",
                     palette=fastf1.plotting.get_compound_mapping(session=session),
                     hue_order=["SOFT", "MEDIUM", "HARD"],
                     linewidth=0,
                     size=5
                     )
        
        # Set labels and title
        ax.set_xlabel("Driver")
        ax.set_ylabel("Lap Time (s)")
        plt.suptitle(f"Race Pace Comparison\n"
                    f"{session.event['EventName']} {session.event.year}")
        
        # Style adjustments
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        
        # Save and return
        filename = "plot.png"
        plt.savefig(filename)
        
        return fig, filename
        
    def create_team_pace_plot(self, session):
        """
        Create a team pace comparison plot.
        
        Args:
            session: The FastF1 session
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        # Get quick laps
        laps = session.laps.pick_quicklaps()
        
        # Convert lap times to seconds for plotting
        transformed_laps = laps.copy()
        transformed_laps.loc[:, "LapTime (s)"] = laps["LapTime"].dt.total_seconds()
        
        # Order teams from fastest to slowest
        team_order = (
            transformed_laps[["Team", "LapTime (s)"]]
            .groupby("Team")
            .median()["LapTime (s)"]
            .sort_values()
            .index
        )
        
        # Get team colors
        team_palette = fastf1.plotting.get_team_color_mapping(session=session)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(15, 10))
        
        # Create box plot
        sns.boxplot(
            data=transformed_laps,
            x="Team",
            y="LapTime (s)",
            order=team_order,
            palette=team_palette,
            whiskerprops=dict(color="white"),
            boxprops=dict(edgecolor="white"),
            medianprops=dict(color="grey"),
            capprops=dict(color="white"),
        )
        
        # Set title and style
        plt.title(f"Race Pace Visualization\n"
                 f"{session.event['EventName']} {session.event.year}")
        plt.grid(visible=False)
        
        # Remove redundant x-label
        ax.set(xlabel=None)
        plt.tight_layout()
        
        # Save and return
        filename = "plot.png"
        plt.savefig(filename)
        
        return fig, filename
        
    def create_lap_sections_plot(self, session, drivers=None):
        """
        Create a lap sections analysis plot.
        
        Args:
            session: The FastF1 session
            drivers: List of driver codes (default: None, will use top 5)
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        # If no drivers specified, use the top 5 fastest
        if not drivers:
            laps = session.laps.pick_quicklaps()
            drivers = laps['Driver'].unique()[:5]
        else:
            drivers = drivers[:5]  # Limit to 5 drivers
        
        # Create the plot with 4 subplots
        fig, axs = plt.subplots(2, 2, figsize=Config.DEFAULT_FIG_SIZE)
        fig.suptitle(f"Lap Sections for {session.event['EventName']} {session.event.year}")
        
        # Define the section types
        section_types = ['braking', 'cornering', 'acceleration', 'full_throttle']
        
        # Process each driver
        for driver in drivers:
            lap = session.laps.pick_driver(driver).pick_fastest()
            telemetry = lap.get_telemetry()
            
            time = telemetry['Time']
            
            # Define the sections
            braking_mask = telemetry['Brake'] > 0
            full_throttle_mask = telemetry['Throttle'] == 100
            cornering_mask = (telemetry['nGear'] < 5) & (telemetry['Speed'] > 100)  # Simplified cornering detection
            acceleration_mask = (telemetry['Throttle'] > 80) & (telemetry['Throttle'] < 100)
            
            masks = {
                'braking': braking_mask,
                'cornering': cornering_mask,
                'acceleration': acceleration_mask,
                'full_throttle': full_throttle_mask
            }
            
            # Plot each section
            for idx, section in enumerate(section_types):
                mask = masks[section]
                axs[idx // 2, idx % 2].plot(time[mask], telemetry['Speed'][mask], label=driver)
        
        # Add labels and legends
        for idx, section in enumerate(section_types):
            axs[idx // 2, idx % 2].set_title(section.replace('_', ' ').capitalize())
            axs[idx // 2, idx % 2].legend()
            axs[idx // 2, idx % 2].set_xlabel("Time")
            axs[idx // 2, idx % 2].set_ylabel("Speed (km/h)")
        
        # Save and return
        filename = "lap_sections.png"
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(filename)
        
        return fig, filename
