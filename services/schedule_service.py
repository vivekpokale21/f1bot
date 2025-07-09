"""
Service for handling F1 schedule data.
"""

import logging
import csv
from datetime import datetime
import json
import os
from config import Config

logger = logging.getLogger('f1bot')

class F1Event:
    """
    Class to store F1 event details.
    """
    def __init__(self, race_name, event_type, start_time, location, country):
        """
        Initialize F1 event details.
        
        Args:
            race_name: Name of the race
            event_type: Type of event (e.g., 'Race', 'Practice 1', 'Qualifying')
            start_time: Start time of the event
            location: Location of the event
            country: Country of the event
        """
        self.race_name = race_name
        self.event_type = event_type
        self.start_time = start_time
        self.location = location
        self.country = country


class ScheduleService:
    """
    Service for handling F1 schedule data.
    """
    
    def __init__(self, schedule_file=Config.SCHEDULE_FILE, flags_file=Config.FLAGS_FILE):
        """
        Initialize the schedule service.
        
        Args:
            schedule_file: Path to the schedule CSV file
            flags_file: Path to the country flags JSON file
        """
        self.schedule_file = schedule_file
        self.flags_file = flags_file
        self.events = []
        self.country_flags = {}
        
    def load_schedule(self):
        """
        Load the F1 schedule from the CSV file.
        
        Returns:
            list: List of F1Event objects
        """
        events = []
        
        try:
            with open(self.schedule_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    country = row[0]
                    location = row[1]
                    race_name = row[2]
                    
                    i = 3
                    while i <= 12:  # Process up to 5 events per race weekend
                        if i + 1 >= len(row):
                            break
                            
                        event_type = row[i]
                        start_time_str = row[i + 1]
                        
                        try:
                            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
                            events.append(F1Event(race_name, event_type, start_time, location, country))
                        except ValueError as e:
                            logger.error(f"Error parsing date {start_time_str}: {e}")
                            
                        i += 2
            
            self.events = events
            logger.info(f"Loaded {len(events)} events from schedule file")
            return events
            
        except Exception as e:
            logger.error(f"Error loading schedule: {e}")
            return []
    
    def load_country_flags(self):
        """
        Load country flags from the JSON file.
        
        Returns:
            dict: Dictionary mapping country names to flag URLs
        """
        try:
            with open(self.flags_file, 'r') as f:
                self.country_flags = json.load(f)
            logger.info(f"Loaded {len(self.country_flags)} country flags")
            return self.country_flags
        except Exception as e:
            logger.error(f"Error loading country flags: {e}")
            return {}
    
    def get_next_event(self):
        """
        Get the next upcoming F1 event.
        
        Returns:
            F1Event: The next upcoming event, or None if no events are found
        """
        if not self.events:
            self.load_schedule()
            
        current_time = datetime.utcnow()
        
        # Filter out past events and sort by start time
        upcoming_events = [event for event in self.events if event.start_time > current_time]
        upcoming_events.sort(key=lambda x: x.start_time)
        
        if upcoming_events:
            return upcoming_events[0]
        else:
            logger.warning("No upcoming events found")
            return None
    
    def get_events_by_race(self, race_name):
        """
        Get all events for a specific race.
        
        Args:
            race_name: Name of the race
            
        Returns:
            list: List of F1Event objects for the specified race
        """
        if not self.events:
            self.load_schedule()
            
        return [event for event in self.events if event.race_name.lower() == race_name.lower()]
    
    def get_events_by_country(self, country):
        """
        Get all events in a specific country.
        
        Args:
            country: Name of the country
            
        Returns:
            list: List of F1Event objects for the specified country
        """
        if not self.events:
            self.load_schedule()
            
        return [event for event in self.events if event.country.lower() == country.lower()]
    
    def get_flag_url(self, country):
        """
        Get the flag URL for a country.
        
        Args:
            country: Name of the country
            
        Returns:
            str: URL of the country flag, or None if not found
        """
        if not self.country_flags:
            self.load_country_flags()
            
        return self.country_flags.get(country)
