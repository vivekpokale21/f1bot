"""
Telemetry-related commands for the F1 Discord Bot.
"""

import logging
import discord
from discord.ext import commands
from services.telemetry_service import TelemetryService
from config import Config

logger = logging.getLogger('f1bot')

class TelemetryCog(commands.Cog):
    """
    Commands for F1 telemetry data visualization.
    """
    
    def __init__(self, bot):
        """
        Initialize the telemetry commands.
        
        Args:
            bot: The Discord bot instance
        """
        self.bot = bot
        self.telemetry_service = TelemetryService()
    
    @commands.command(name="speedtrace")
    async def speedtrace(self, ctx, year, race, session, driver1, driver2):
        """
        Compare speed traces between two drivers.
        
        Args:
            ctx: The command context
            year: The year of the session
            race: The race name or round number
            session: The session type (e.g., 'R', 'Q', 'FP1')
            driver1: The first driver code
            driver2: The second driver code
        """
        await ctx.send(Config.LOADING_MESSAGE)
        
        try:
            # Load session data
            session_obj = self.telemetry_service.get_session(year, race, session)
            
            # Create the plot
            _, filename = self.telemetry_service.create_speed_trace_plot(
                session_obj, driver1, driver2
            )
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
        except Exception as e:
            logger.error(f"Error in speedtrace command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="gearshifts")
    async def gearshifts(self, ctx, year, race, session, driver):
        """
        Show gear shifts on a track map.
        
        Args:
            ctx: The command context
            year: The year of the session
            race: The race name or round number
            session: The session type (e.g., 'R', 'Q', 'FP1')
            driver: The driver code
        """
        try:
            # Load session data
            session_obj = self.telemetry_service.get_session(year, race, session)
            
            # Create the plot
            _, filename = self.telemetry_service.create_gear_shifts_plot(
                session_obj, driver
            )
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
        except Exception as e:
            logger.error(f"Error in gearshifts command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="trackdominance")
    async def trackdominance(self, ctx, year, grand_prix, session_name, *drivers):
        """
        Show which driver is fastest in each mini-sector.
        
        Args:
            ctx: The command context
            year: The year of the session
            grand_prix: The race name
            session_name: The session type (e.g., 'R', 'Q', 'FP1')
            drivers: Optional list of driver codes (up to 3)
        """
        try:
            # Load session data
            session_obj = self.telemetry_service.get_session(year, grand_prix, session_name)
            
            # Create the plot
            _, filename, driver_info = self.telemetry_service.create_track_dominance_plot(
                session_obj, drivers
            )
            
            # Send the image
            image = discord.File(filename)
            await ctx.send(file=image)
            
            # Send driver info as a follow-up message
            if driver_info:
                embed = discord.Embed(
                    title="Driver Information",
                    color=discord.Color.blue()
                )
                
                for driver, info in driver_info.items():
                    embed.add_field(
                        name=f"{driver} - {info['DriverNumber']}",
                        value=f"Sector 1: {info['Sector1']}\n"
                              f"Sector 2: {info['Sector2']}\n"
                              f"Sector 3: {info['Sector3']}",
                        inline=True
                    )
                
                await ctx.send(embed=embed)
            
        except Exception as e:
            logger.error(f"Error in trackdominance command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @speedtrace.error
    @gearshifts.error
    @trackdominance.error
    async def telemetry_error(self, ctx, error):
        """
        Error handler for telemetry commands.
        
        Args:
            ctx: The command context
            error: The error that occurred
        """
        if isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.name == "speedtrace":
                await ctx.send("Usage: `+speedtrace [year] [race] [session] [driver1] [driver2]`\n"
                              "Example: `+speedtrace 2023 Monaco Q VER HAM`")
            elif ctx.command.name == "gearshifts":
                await ctx.send("Usage: `+gearshifts [year] [race] [session] [driver]`\n"
                              "Example: `+gearshifts 2023 Monaco Q VER`")
            elif ctx.command.name == "trackdominance":
                await ctx.send("Usage: `+trackdominance [year] [race] [session] [driver1] [driver2] [driver3]`\n"
                              "Example: `+trackdominance 2023 Monaco Q VER HAM PER`\n"
                              "Note: Drivers are optional. If not provided, the top 3 fastest drivers will be used.")
        else:
            logger.error(f"Unhandled error in {ctx.command.name}: {error}")
            await ctx.send(f"An error occurred: {str(error)}")


async def setup(bot):
    """
    Set up the telemetry cog.
    
    Args:
        bot: The Discord bot instance
    """
    await bot.add_cog(TelemetryCog(bot))
