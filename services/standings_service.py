"""
Service for handling F1 standings data.
"""

import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger('f1bot')

class DriverTeamDetails:
    """
    Class to store driver or team details.
    """
    def __init__(self, name, team, points):
        """
        Initialize driver or team details.
        
        Args:
            name: Driver name or team name
            team: Team name (same as name for constructor standings)
            points: Championship points
        """
        self.name = name
        self.team = team
        self.points = points


class StandingsService:
    """
    Service for fetching and processing F1 standings data.
    """
    
    def __init__(self):
        """Initialize the standings service."""
        pass
    
    @staticmethod
    def normalize_team_name(team_name):
        """
        Normalize team names to a consistent format.
        
        Args:
            team_name: The team name to normalize
            
        Returns:
            str: Normalized team name
        """
        if "Red" in team_name:
            return "Red Bull"
        elif "Alpine" in team_name:
            return "Alpine"
        elif "Aston" in team_name:
            return "Aston Martin"
        elif "McLaren" in team_name:
            return "McLaren"
        elif "Williams" in team_name:
            return "Williams"
        elif "RB" in team_name:
            return "Visa CashApp RB"
        elif "Kick" in team_name:
            return "Kick Sauber"
        elif "Haas" in team_name:
            return "Haas"
        elif "Ferrari" in team_name:
            return "Ferrari"
        elif "Mercedes" in team_name:
            return "Mercedes"
        else:
            return team_name
    
    def get_driver_standings(self, year=None):
        """
        Get the current F1 driver standings.
        
        Args:
            year: Optional year to get standings for (default: current year)
            
        Returns:
            list: List of DriverTeamDetails objects for drivers
        """
        # Determine URL based on year
        if year:
            url = f"https://www.formula1.com/en/results.html/{year}/drivers.html"
        else:
            url = "https://www.formula1.com/en/results.html/2025/drivers.html"
        
        logger.info(f"Fetching driver standings from {url}")
        
        try:
            # Fetch and parse the drivers' standings page
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find the standings table
            table = soup.find("table")
            if not table:
                logger.error("Could not find standings table on the page")
                return []
                
            rows = table.find_all("tr")[1:]  # Skip the header row
            
            driver_standings = []
            
            for row in rows:
                columns = row.find_all("td")
                driver_name = columns[1].get_text().strip()[:-3]
                
                team_name = columns[3].get_text().strip()
                points = int(float(columns[4].get_text().strip()))
                
                # Normalize team name
                team_name = self.normalize_team_name(team_name)
                
                driver_standings.append(DriverTeamDetails(driver_name, team_name, points))
            
            return driver_standings
            
        except Exception as e:
            logger.error(f"Error fetching driver standings: {e}")
            return []
    
    def get_constructor_standings(self, year=None):
        """
        Get the current F1 constructor standings.
        
        Args:
            year: Optional year to get standings for (default: current year)
            
        Returns:
            list: List of DriverTeamDetails objects for constructors
        """
        # Determine URL based on year
        if year:
            url = f"https://www.formula1.com/en/results.html/{year}/team.html"
        else:
            url = "https://www.formula1.com/en/results.html/2025/team.html"
        
        logger.info(f"Fetching constructor standings from {url}")
        
        try:
            # Fetch and parse the constructor standings page
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find the standings table
            table = soup.find("table")
            if not table:
                logger.error("Could not find standings table on the page")
                return []
                
            rows = table.find_all("tr")[1:]  # Skip the header row
            
            constructor_standings = []
            
            for row in rows:
                columns = row.find_all("td")
                team_name = columns[1].get_text().strip()
                points = int(float(columns[2].get_text().strip()))
                
                # Normalize team name
                team_name = self.normalize_team_name(team_name)
                
                constructor_standings.append(DriverTeamDetails(team_name, team_name, points))
            
            return constructor_standings
            
        except Exception as e:
            logger.error(f"Error fetching constructor standings: {e}")
            return []
