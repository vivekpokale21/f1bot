"""
Configuration settings for the F1 Discord Bot.
"""

class Config:
    # Bot configuration
    TOKEN_ENV_VAR = 'token'
    COMMAND_PREFIX = '+'
    
    # File paths
    DATA_DIR = 'data'
    SCHEDULE_FILE = f'{DATA_DIR}/sched.csv'
    FLAGS_FILE = f'{DATA_DIR}/country_flags.json'
    
    # FastF1 configuration
    CACHE_DIR = '.fastf1_cache'
    
    # Visualization settings
    DEFAULT_FIG_SIZE = (12, 8)
    DEFAULT_MINI_SECTORS = 20
    
    # Discord message settings
    LOADING_MESSAGE = "FastF1 can take up to 30s to fetch data for a race unless it is already cached. Stand by, your graph will be loaded shortly."
