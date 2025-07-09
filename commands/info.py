"""
Informational commands for the F1 Discord Bot.
"""

import logging
import discord
from discord.ext import commands
from services.standings_service import StandingsService
from services.schedule_service import ScheduleService
from utils.embed_builder import EmbedBuilder
from config import Config

logger = logging.getLogger('f1bot')

class InfoCog(commands.Cog):
    """
    Commands for F1 information (schedule, standings, etc.).
    """
    
    def __init__(self, bot):
        """
        Initialize the info commands.
        
        Args:
            bot: The Discord bot instance
        """
        self.bot = bot
        self.standings_service = StandingsService()
        self.schedule_service = ScheduleService()
        self.embed_builder = EmbedBuilder()
    
    @commands.command(name="f1")
    async def f1(self, ctx):
        """
        Show the next F1 event.
        
        Args:
            ctx: The command context
        """
        try:
            # Load schedule and country flags
            self.schedule_service.load_schedule()
            country_flags = self.schedule_service.load_country_flags()
            
            # Get the next event
            next_event = self.schedule_service.get_next_event()
            
            if not next_event:
                await ctx.send("No upcoming F1 events found.")
                return
            
            # Create and send the embed
            embed = self.embed_builder.build_event_embed(next_event, country_flags)
            await ctx.send(embed=embed)
            
        except Exception as e:
            logger.error(f"Error in f1 command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="drivers")
    async def drivers(self, ctx, year=None):
        """
        Show the current F1 driver standings.
        
        Args:
            ctx: The command context
            year: Optional year to get standings for
        """
        try:
            # Get driver standings
            standings = self.standings_service.get_driver_standings(year)
            
            if not standings:
                await ctx.send("Could not retrieve driver standings.")
                return
            
            # Create and send the embed
            embed = self.embed_builder.build_driver_standings_embed(standings)
            await ctx.send(embed=embed)
            
        except Exception as e:
            logger.error(f"Error in drivers command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="constructors")
    async def constructors(self, ctx, year=None):
        """
        Show the current F1 constructor standings.
        
        Args:
            ctx: The command context
            year: Optional year to get standings for
        """
        try:
            # Get constructor standings
            standings = self.standings_service.get_constructor_standings(year)
            
            if not standings:
                await ctx.send("Could not retrieve constructor standings.")
                return
            
            # Create and send the embed
            embed = self.embed_builder.build_constructor_standings_embed(standings)
            await ctx.send(embed=embed)
            
        except Exception as e:
            logger.error(f"Error in constructors command: {e}")
            await ctx.send(f"An error occurred: {str(e)}")
    
    @commands.command(name="bhelp")
    async def help_command(self, ctx, command_name=None):
        """
        Show help information for commands.
        
        Args:
            ctx: The command context
            command_name: Optional command name to get help for
        """
        if not command_name:
            # General help
            embed = discord.Embed(
                title="F1 Discord Bot Help",
                description="Here are the available commands:",
                color=discord.Color.blue()
            )
            
            # Telemetry commands
            embed.add_field(
                name="Telemetry Commands",
                value="`speedtrace` - Compare speed traces between two drivers\n"
                      "`gearshifts` - Show gear shifts on a track map\n"
                      "`trackdominance` - Show which driver is fastest in each mini-sector",
                inline=False
            )
            
            # Race analysis commands
            embed.add_field(
                name="Race Analysis Commands",
                value="`racepace` - Show race pace comparison\n"
                      "`teampace` - Show team pace comparison\n"
                      "`lapsections` - Analyze different sections of laps",
                inline=False
            )
            
            # Info commands
            embed.add_field(
                name="Info Commands",
                value="`f1` - Show the next F1 event\n"
                      "`drivers` - Show the current F1 driver standings\n"
                      "`constructors` - Show the current F1 constructor standings",
                inline=False
            )
            
            # Help command
            embed.add_field(
                name="Help",
                value="Use `+bhelp [command]` to get detailed help for a specific command.",
                inline=False
            )
            
            await ctx.send(embed=embed)
            
        else:
            # Command-specific help
            command_name = command_name.lower()
            
            if command_name == "speedtrace":
                embed = self.embed_builder.build_help_embed(
                    "speedtrace",
                    "Compare speed traces between two drivers.",
                    "+speedtrace [year] [race] [session] [driver1] [driver2]",
                    ["+speedtrace 2023 Monaco Q VER HAM"]
                )
                
            elif command_name == "gearshifts":
                embed = self.embed_builder.build_help_embed(
                    "gearshifts",
                    "Show gear shifts on a track map.",
                    "+gearshifts [year] [race] [session] [driver]",
                    ["+gearshifts 2023 Monaco Q VER"]
                )
                
            elif command_name == "trackdominance":
                embed = self.embed_builder.build_help_embed(
                    "trackdominance",
                    "Show which driver is fastest in each mini-sector.",
                    "+trackdominance [year] [race] [session] [driver1] [driver2] [driver3]",
                    [
                        "+trackdominance 2023 Monaco Q VER HAM PER",
                        "+trackdominance 2023 Monaco Q"
                    ]
                )
                
            elif command_name == "racepace":
                embed = self.embed_builder.build_help_embed(
                    "racepace",
                    "Show race pace comparison for the top 10 drivers.",
                    "+racepace [year] [race]",
                    ["+racepace 2023 Monaco"]
                )
                
            elif command_name == "teampace":
                embed = self.embed_builder.build_help_embed(
                    "teampace",
                    "Show team pace comparison.",
                    "+teampace [year] [race]",
                    ["+teampace 2023 Monaco"]
                )
                
            elif command_name == "lapsections":
                embed = self.embed_builder.build_help_embed(
                    "lapsections",
                    "Analyze different sections of laps.",
                    "+lapsections [year] [race] [session] [driver1] [driver2] ...",
                    [
                        "+lapsections 2023 Monaco Q VER HAM PER",
                        "+lapsections 2023 Monaco Q"
                    ]
                )
                
            elif command_name == "f1":
                embed = self.embed_builder.build_help_embed(
                    "f1",
                    "Show the next F1 event.",
                    "+f1",
                    ["+f1"]
                )
                
            elif command_name == "drivers":
                embed = self.embed_builder.build_help_embed(
                    "drivers",
                    "Show the current F1 driver standings.",
                    "+drivers [year]",
                    ["+drivers", "+drivers 2023"]
                )
                
            elif command_name == "constructors":
                embed = self.embed_builder.build_help_embed(
                    "constructors",
                    "Show the current F1 constructor standings.",
                    "+constructors [year]",
                    ["+constructors", "+constructors 2023"]
                )
                
            else:
                embed = discord.Embed(
                    title="Command Not Found",
                    description=f"Command `{command_name}` not found.",
                    color=discord.Color.red()
                )
            
            await ctx.send(embed=embed)
    
    @f1.error
    @drivers.error
    @constructors.error
    async def info_error(self, ctx, error):
        """
        Error handler for info commands.
        
        Args:
            ctx: The command context
            error: The error that occurred
        """
        logger.error(f"Unhandled error in {ctx.command.name}: {error}")
        await ctx.send(f"An error occurred: {str(error)}")


async def setup(bot):
    """
    Set up the info cog.
    
    Args:
        bot: The Discord bot instance
    """
    await bot.add_cog(InfoCog(bot))
