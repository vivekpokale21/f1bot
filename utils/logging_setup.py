"""
Logging configuration for the F1 Discord Bot.
"""

import logging
import os
from datetime import datetime

def setup_logging(log_level=logging.INFO, log_to_file=True):
    """
    Set up logging for the application.
    
    Args:
        log_level: The logging level (default: INFO)
        log_to_file: Whether to log to a file (default: True)
        
    Returns:
        logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    if log_to_file and not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure logger
    logger = logging.getLogger('f1bot')
    logger.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Add file handler if enabled
    if log_to_file:
        log_filename = f"logs/f1bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
