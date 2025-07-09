"""
Main entry point for the F1 Discord Bot.
"""

import os
import logging
import discord
from discord.ext import commands
import fastf1
from config import Config
from utils.logging_setup import setup_logging
from utils.error_handler import ErrorHandler

# Setup logging
logger = setup_logging()

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=Config.COMMAND_PREFIX, intents=intents, help_command=None)

# Enable FastF1 cache and setup
# Create cache directory if it doesn't exist
if not os.path.exists(Config.CACHE_DIR):
    os.makedirs(Config.CACHE_DIR)
    logger.info(f"Created FastF1 cache directory: {Config.CACHE_DIR}")

fastf1.Cache.enable_cache(Config.CACHE_DIR)
#fastf1.plotting.setup_mpl(misc_mpl_mods=False)

# Setup hook for loading extensions
@bot.event
async def setup_hook():
    """
    Called when the bot is starting up.
    This is the recommended way to load extensions in discord.py 2.0+
    """
    await bot.load_extension('commands.telemetry')
    await bot.load_extension('commands.race_analysis')
    await bot.load_extension('commands.info')
    logger.info('All extensions loaded')

# Global error handler
@bot.event
async def on_command_error(ctx, error):
    """
    Global error handler for all commands.
    
    Args:
        ctx: The command context
        error: The error that occurred
    """
    await ErrorHandler.handle_command_error(ctx, error)

@bot.event
async def on_ready():
    """
    Event handler for when the bot is ready.
    """
    logger.info(f'Bot is ready. Logged in as {bot.user}')
    logger.info(f'Bot is in {len(bot.guilds)} guilds')
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="F1 telemetry | +bhelp"
        )
    )

@bot.event
async def on_guild_join(guild):
    """
    Event handler for when the bot joins a guild.
    
    Args:
        guild: The guild the bot joined
    """
    logger.info(f'Bot joined guild: {guild.name} (ID: {guild.id})')

def main():
    """
    Main function to start the bot.
    """
    try:
        # Get token from environment variable
        token = ''
        if not token:
            logger.error(f'No token found in environment variable {Config.TOKEN_ENV_VAR}')
            return
        
        # Start the bot
        logger.info('Starting bot...')
        bot.run(token)
        
    except Exception as e:
        logger.error(f'Error starting bot: {e}')

if __name__ == '__main__':
    main()
