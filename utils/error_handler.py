"""
Error handling utilities for the F1 Discord Bot.
"""

import logging
import traceback
import discord
from discord.ext import commands

logger = logging.getLogger('f1bot')

class ErrorHandler:
    """
    Centralized error handling for the F1 Discord Bot.
    """
    
    @staticmethod
    async def handle_command_error(ctx, error):
        """
        Handle errors that occur during command execution.
        
        Args:
            ctx: The command context
            error: The error that occurred
        """
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found. Use `+help` to see available commands.")
            return
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}. Use `+help {ctx.command}` for proper usage.")
            return
            
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Invalid argument provided. Use `+help {ctx.command}` for proper usage.")
            return
            
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds.")
            return
            
        # FastF1 specific errors
        if "Session does not exist" in str(error):
            await ctx.send(f"Session not found. Please check the year, race, and session type.")
            return
            
        if "Driver(s) not found" in str(error) or "could not find driver" in str(error).lower():
            await ctx.send(f"Driver not found. Please check the driver code.")
            return
            
        # Log unexpected errors
        logger.error(f"Unhandled error in command {ctx.command}: {error}")
        logger.error(traceback.format_exc())
        
        # Send a user-friendly error message
        embed = discord.Embed(
            title="An error occurred",
            description="An unexpected error occurred while processing your command.",
            color=discord.Color.red()
        )
        embed.add_field(name="Error", value=str(error)[:1024])
        embed.add_field(name="Command", value=f"{ctx.command} {ctx.message.content}")
        embed.set_footer(text="The error has been logged and will be investigated.")
        
        await ctx.send(embed=embed)
