"""
Race analysis commands for the F1 Discord Bot.
"""

import logging
import discord
from discord.ext import commands
from services.race_analysis_service import RaceAnalysisService
from config import Config

logger = logging.getLogger('f1bot')

class RaceAnalysisCog(commands.Cog):
    """
    Commands for F1 race analysis.
    """
    
    def __init__(self, bot):
        """
        Initialize the race analysis commands.
        
        Args:
            bot: The Discord bot instance
        """
        self.bot = bot
        self.race_analysis_service = RaceAnalysisService()
    
    @commands.command(name="racepace")
    async def racepace(self, ctx, year, race):
        """
        Show race pace comparison for the top 10 drivers.
        
        Args:
            ctx: The command context
            year: The year of the race
            race: The race name or round number
        """
        await ctx.send(Config.LOADING_MESSAGE)
        
        try:
            # Load session data
            session = self.race_analysis_service.get_session(year, race)
            
            # Create the plot
            _, filename = self.race_analysis_service.create_race_pace_plot(session)
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
        except Exception as e:
            logger.error(f"Error in racepace command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="teampace")
    async def teampace(self, ctx, year, race):
        """
        Show team pace comparison.
        
        Args:
            ctx: The command context
            year: The year of the race
            race: The race name or round number
        """
        await ctx.send(Config.LOADING_MESSAGE)
        
        try:
            # Load session data
            session = self.race_analysis_service.get_session(year, race)
            
            # Create the plot
            _, filename = self.race_analysis_service.create_team_pace_plot(session)
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
        except Exception as e:
            logger.error(f"Error in teampace command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="lapsections")
    async def lapsections(self, ctx, year, grand_prix, session_name, *drivers):
        """
        Analyze different sections of laps.
        
        Args:
            ctx: The command context
            year: The year of the session
            grand_prix: The race name
            session_name: The session type (e.g., 'R', 'Q', 'FP1')
            drivers: Optional list of driver codes (up to 5)
        """
        await ctx.send(Config.LOADING_MESSAGE)
        
        try:
            # Load session data
            session = self.race_analysis_service.get_session(year, grand_prix, session_name)
            
            # Create the plot
            _, filename = self.race_analysis_service.create_lap_sections_plot(session, drivers)
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
        except Exception as e:
            logger.error(f"Error in lapsections command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @racepace.error
    @teampace.error
    @lapsections.error
    async def race_analysis_error(self, ctx, error):
        """
        Error handler for race analysis commands.
        
        Args:
            ctx: The command context
            error: The error that occurred
        """
        if isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.name == "racepace":
                await ctx.send("Usage: `+racepace [year] [race]`\n"
                              "Example: `+racepace 2023 Monaco`")
            elif ctx.command.name == "teampace":
                await ctx.send("Usage: `+teampace [year] [race]`\n"
                              "Example: `+teampace 2023 Monaco`")
            elif ctx.command.name == "lapsections":
                await ctx.send("Usage: `+lapsections [year] [race] [session] [driver1] [driver2] ...`\n"
                              "Example: `+lapsections 2023 Monaco Q VER HAM PER`\n"
                              "Note: Drivers are optional. If not provided, the top 5 fastest drivers will be used.")
        else:
            logger.error(f"Unhandled error in {ctx.command.name}: {error}")
            await ctx.send(f"An error occurred: {str(error)}")


async def setup(bot):
    """
    Set up the race analysis cog.
    
    Args:
        bot: The Discord bot instance
    """
    await bot.add_cog(RaceAnalysisCog(bot))
