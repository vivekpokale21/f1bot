"""
Service for handling F1 telemetry data processing.
"""

import logging
import numpy as np
import pandas as pd
import fastf1
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import seaborn as sns
from config import Config

logger = logging.getLogger('f1bot')

class MiniSectorAnalyzer:
    """
    Analyzer for creating and analyzing mini-sectors on a track.
    """
    
    def __init__(self, telemetry_data, num_sectors=Config.DEFAULT_MINI_SECTORS, sector_type='distance'):
        """
        Initialize the mini-sector analyzer.
        
        Args:
            telemetry_data: The telemetry data to analyze
            num_sectors: Number of mini-sectors to create (default: from Config)
            sector_type: Type of mini-sectors ('distance', 'time', or 'angle')
        """
        self.telemetry = telemetry_data
        self.num_sectors = num_sectors
        self.sector_type = sector_type
        
    def create_mini_sectors(self):
        """
        Create mini-sectors based on the specified type.
        
        Returns:
            pandas.DataFrame: Telemetry data with mini-sector information
        """
        if self.sector_type == 'distance':
            self.telemetry['MiniSector'] = pd.cut(
                self.telemetry['Distance'], 
                self.num_sectors, 
                labels=False
            )
        elif self.sector_type == 'time':
            self.telemetry['MiniSector'] = pd.cut(
                self.telemetry['Time'].dt.total_seconds(), 
                self.num_sectors, 
                labels=False
            )
        elif self.sector_type == 'angle':
            # Calculate track angle for more natural mini-sectors around corners
            x_diff = self.telemetry['X'].diff()
            y_diff = self.telemetry['Y'].diff()
            angles = np.arctan2(y_diff, x_diff)
            # Normalize angles to 0-2π range
            angles = (angles + 2 * np.pi) % (2 * np.pi)
            self.telemetry['Angle'] = angles
            self.telemetry['MiniSector'] = pd.cut(
                angles, 
                self.num_sectors, 
                labels=False
            )
        else:
            raise ValueError(f"Invalid sector_type: {self.sector_type}. Must be 'distance', 'time', or 'angle'.")
            
        return self.telemetry
        
    def find_fastest_drivers(self, drivers_telemetry_list):
        """
        Find the fastest driver in each mini-sector.
        
        Args:
            drivers_telemetry_list: List of telemetry data for different drivers
            
        Returns:
            pandas.DataFrame: DataFrame with the fastest driver for each mini-sector
        """
        # Combine all drivers' telemetry
        mini_sectors = pd.concat(drivers_telemetry_list)
        
        # Calculate the time spent in each mini-sector for each driver
        time_spent = mini_sectors.groupby(['Driver', 'MiniSector']).apply(
            lambda df: df['Time'].diff().sum()
        ).reset_index().rename(columns={0: 'TimeSpent'})
        
        # Find the fastest driver in each mini-sector
        fastest_per_mini_sector = time_spent.loc[
            time_spent.groupby('MiniSector')['TimeSpent'].idxmin()
        ]
        
        return fastest_per_mini_sector


class TelemetryService:
    """
    Service for processing and analyzing F1 telemetry data.
    """
    
    def __init__(self):
        """Initialize the telemetry service."""
        pass
        
    def get_session(self, year, race, session_type):
        """
        Get a FastF1 session.
        
        Args:
            year: The year of the session
            race: The race name or round number
            session_type: The session type (e.g., 'R', 'Q', 'FP1')
            
        Returns:
            fastf1.core.Session: The loaded session
        """
        logger.info(f"Loading session data for {year} {race} {session_type}")
        session = fastf1.get_session(int(year), race, session_type)
        session.load()
        return session
        
    def get_driver_fastest_lap(self, session, driver):
        """
        Get the fastest lap for a driver.
        
        Args:
            session: The FastF1 session
            driver: The driver code
            
        Returns:
            fastf1.core.Lap: The fastest lap
        """
        return session.laps.pick_driver(driver).pick_fastest()
        
    def create_speed_trace_plot(self, session, driver1, driver2):
        """
        Create a speed trace comparison plot for two drivers.
        
        Args:
            session: The FastF1 session
            driver1: The first driver code
            driver2: The second driver code
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        driver1_lap = self.get_driver_fastest_lap(session, driver1)
        driver2_lap = self.get_driver_fastest_lap(session, driver2)
        
        # Get telemetry data
        driver1_tel = driver1_lap.get_car_data().add_distance()
        driver2_tel = driver2_lap.get_car_data().add_distance()
        
        # Get driver colors
        # Setup for plotting
        fastf1.plotting.setup_mpl(mpl_timedelta_support=True, misc_mpl_mods=False, color_scheme='fastf1')
        
        # Get driver colors
        driver_colors = fastf1.plotting.get_driver_color_mapping(session=session)
        driver1_color = driver_colors.get(driver1, 'red')  # Default to red if driver not found
        driver2_color = driver_colors.get(driver2, 'blue')  # Default to blue if driver not found
        
        # Get lap times for display
        driver1_time = str(driver1_lap["LapTime"])[11:19]  # Format as MM:SS.sss
        driver2_time = str(driver2_lap["LapTime"])[11:19]
        
        # Get circuit info for corner markers
        circuit_info = session.get_circuit_info()
        v_min = min(driver1_tel['Speed'].min(), driver2_tel['Speed'].min())
        v_max = max(driver1_tel['Speed'].max(), driver2_tel['Speed'].max())
        
        # Create plot with two subplots (speed and throttle)
        fig, ax = plt.subplots(2, figsize=Config.DEFAULT_FIG_SIZE, 
                              gridspec_kw={'height_ratios': [10, 3]})
        
        # Speed plot
        ax[0].plot(driver1_tel['Distance'], driver1_tel['Speed'], 
                  color=driver1_color, label=f"{driver1} - {driver1_time}")
        ax[0].plot(driver2_tel['Distance'], driver2_tel['Speed'], 
                  color=driver2_color, label=f"{driver2} - {driver2_time}")
        
        # Add corner markers
        ax[0].vlines(x=circuit_info.corners['Distance'], 
                    ymin=v_min - 20, ymax=v_max + 10,
                    linestyles='dotted', colors='grey')
        
        # Add corner numbers
        for _, corner in circuit_info.corners.iterrows():
            txt = f"{corner['Number']}{corner['Letter']}"
            ax[0].text(corner['Distance'], v_min - 30, txt,
                      va='center_baseline', ha='center', size='small', rotation=-90)
        
        ax[0].set_xlabel('Distance (m)')
        ax[0].set_ylabel('Speed (km/h)')
        ax[0].set_ylim([v_min - 40, v_max + 5])
        ax[0].legend()
        
        # Throttle plot
        ax[1].plot(driver1_tel['Distance'], driver1_tel['Throttle'], 
                  color=driver1_color, label=f"{driver1}")
        ax[1].plot(driver2_tel['Distance'], driver2_tel['Throttle'], 
                  color=driver2_color, label=f"{driver2}")
        ax[1].set_ylabel('Throttle %')
        ax[1].legend()
        
        # Title
        plt.suptitle(f"Fastest Lap Comparison\n"
                    f"{session.event['EventName']} {session.event.year}")
        
        # Save and return
        filename = "plot.png"
        plt.savefig(filename)
        
        return fig, filename
        
    def create_gear_shifts_plot(self, session, driver):
        """
        Create a gear shift visualization plot.
        
        Args:
            session: The FastF1 session
            driver: The driver code
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        lap = self.get_driver_fastest_lap(session, driver)
        tel = lap.get_telemetry()
        
        x = np.array(tel['X'].values)
        y = np.array(tel['Y'].values)
        
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        gear = tel['nGear'].to_numpy().astype(float)
        
        fig, ax = plt.subplots(figsize=Config.DEFAULT_FIG_SIZE)
        
        cmap = plt.get_cmap('Paired')
        lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N + 1), cmap=cmap)
        lc_comp.set_array(gear)
        lc_comp.set_linewidth(4)
        
        ax.add_collection(lc_comp)
        ax.axis('equal')
        ax.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
        
        plt.suptitle(
            f"Fastest Lap Gear Shift Visualization\n"
            f"{lap['Driver']} - {session.event['EventName']} {session.event.year}"
        )
        
        cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
        cbar.set_ticks(np.arange(1.5, 9.5))
        cbar.set_ticklabels(np.arange(1, 9))
        
        filename = "plot.png"
        plt.savefig(filename)
        
        return fig, filename
        
    def create_track_dominance_plot(self, session, drivers, num_mini_sectors=Config.DEFAULT_MINI_SECTORS):
        """
        Create a track dominance visualization showing which driver is fastest in each mini-sector.
        
        Args:
            session: The FastF1 session
            drivers: List of driver codes
            num_mini_sectors: Number of mini-sectors to create
            
        Returns:
            tuple: (figure, filename) - The matplotlib figure and the saved filename
        """
        mini_sectors_list = []
        driver_info = {}
        
        # If no drivers specified, use the top 3 fastest
        if not drivers:
            laps = session.laps.pick_quicklaps()
            fastest_laps = laps.groupby('Driver')['LapTime'].min().sort_values().index[:3]
            drivers = fastest_laps.tolist()
        
        # Limit to 3 drivers for clarity
        drivers = drivers[:3]
        
        # Get telemetry data for each driver
        for driver in drivers:
            lap = self.get_driver_fastest_lap(session, driver)
            telemetry = lap.get_telemetry()
            telemetry['Driver'] = driver
            mini_sectors_list.append(telemetry)
            
            # Gather driver info
            driver_info[driver] = {
                'DriverNumber': lap['DriverNumber'],
                'DriverName': lap['Driver'],
                'Sector1': lap['Sector1Time'],
                'Sector2': lap['Sector2Time'],
                'Sector3': lap['Sector3Time'],
                'TeamColour': fastf1.plotting.get_driver_color_mapping(session=session).get(driver, 'white')
            }
        
        # Create mini-sectors
        analyzer = MiniSectorAnalyzer(pd.concat(mini_sectors_list), num_mini_sectors)
        mini_sectors = analyzer.create_mini_sectors()
        
        # Find fastest driver per mini-sector
        fastest_per_mini_sector = analyzer.find_fastest_drivers(mini_sectors_list)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=Config.DEFAULT_FIG_SIZE)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        
        # Get track map from the first driver's lap
        lap = session.laps.pick_driver(drivers[0]).pick_fastest()
        x = lap.telemetry['X'].values
        y = lap.telemetry['Y'].values
        
        # Plot the track outline
        ax.plot(x, y, color='black', linestyle='-', linewidth=16, zorder=0)
        
        # Create points and segments for coloring
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        
        # Color each mini-sector by fastest driver
        for minisector in range(num_mini_sectors):
            sector_data = mini_sectors[mini_sectors['MiniSector'] == minisector]
            if not sector_data.empty:
                fastest_driver = fastest_per_mini_sector[
                    fastest_per_mini_sector['MiniSector'] == minisector
                ]['Driver'].values[0]
                color = fastf1.plotting.get_driver_color_mapping(session=session).get(fastest_driver, 'white')
                segment_indices = sector_data.index
                segment_points = segments[segment_indices.min():segment_indices.max() + 1]
                lc = LineCollection(segment_points, colors=[color], linewidth=5)
                ax.add_collection(lc)
        
        # Add legend
        for driver in drivers:
            ax.plot([], [], color=fastf1.plotting.get_driver_color_mapping(session=session).get(driver, 'white'), label=driver)
        
        ax.legend()
        ax.set_title(f"{session.event.year} {session.event['EventName']} - Track Dominance by Mini-Sectors", 
                    color='white')
        ax.axis('off')
        ax.set_aspect('equal')
        
        # Save the plot
        filename = "track_dominance_minisectors.png"
        plt.savefig(filename, bbox_inches='tight', facecolor=fig.get_facecolor())
        
        return fig, filename, driver_info
