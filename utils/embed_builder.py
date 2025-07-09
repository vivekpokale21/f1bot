"""
Utilities for building Discord embeds for the F1 Discord Bot.
"""

import discord
from datetime import datetime

class EmbedBuilder:
    """
    Utility class for building Discord embeds.
    """
    
    @staticmethod
    def build_event_embed(event, country_flags):
        """
        Build an embed for an F1 event.
        
        Args:
            event: The F1 event object
            country_flags: Dictionary of country flags
            
        Returns:
            discord.Embed: The created embed
        """
        embed = discord.Embed(title="Next F1 Event", color=discord.Color.blue())

        # Calculate time to go
        current_time = datetime.utcnow()
        time_to_go = event.start_time - current_time
        days, seconds = time_to_go.days, time_to_go.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        time_remaining = f"{days} Days, {hours} Hours, {minutes} Minutes" if days > 0 else f"{hours} Hours, {minutes} Minutes"

        # Get the flag URL
        flag_url = country_flags.get(event.country, "https://example.com/default_flag.png")

        # Add fields for race name, event type, and time to go
        embed.add_field(name="Race Name", value=event.race_name, inline=False)
        embed.add_field(name="Event Type", value=event.event_type, inline=False)
        embed.add_field(name="Location", value=event.location, inline=False)
        embed.add_field(name="Time to Go", value=time_remaining, inline=False)

        # Set the flag URL as a thumbnail
        embed.set_thumbnail(url=flag_url)

        return embed
    
    @staticmethod
    def build_driver_standings_embed(standings):
        """
        Build an embed for driver standings.
        
        Args:
            standings: List of driver standings objects
            
        Returns:
            discord.Embed: The created embed
        """
        name_str = ""
        team_str = ""
        points_str = ""

        # Build strings with line breaks
        for driver in standings:
            name_str += f"{driver.name}\n"
            team_str += f"{driver.team}\n"
            points_str += f"{driver.points}\n"

        # Create the embed
        embed = discord.Embed(title="Drivers' Standings", color=discord.Color.blue())
        embed.add_field(name="Driver", value=name_str, inline=True)
        embed.add_field(name="Team", value=team_str, inline=True)
        embed.add_field(name="Points", value=points_str, inline=True)
        
        return embed
    
    @staticmethod
    def build_constructor_standings_embed(standings):
        """
        Build an embed for constructor standings.
        
        Args:
            standings: List of constructor standings objects
            
        Returns:
            discord.Embed: The created embed
        """
        team_str = ""
        points_str = ""

        # Build strings with line breaks
        for team in standings:
            team_str += f"{team.team}\n"
            points_str += f"{team.points}\n"

        # Create the embed
        embed = discord.Embed(title="Constructors' Standings", color=discord.Color.green())
        embed.add_field(name="Team", value=team_str, inline=True)
        embed.add_field(name="Points", value=points_str, inline=True)
        
        return embed
    
    @staticmethod
    def build_help_embed(command_name, description, usage, examples):
        """
        Build a help embed for a command.
        
        Args:
            command_name: The name of the command
            description: Description of what the command does
            usage: Usage syntax
            examples: List of examples
            
        Returns:
            discord.Embed: The created embed
        """
        embed = discord.Embed(
            title=f"Help: {command_name}",
            description=description,
            color=discord.Color.blue()
        )
        
        embed.add_field(name="Usage", value=f"`{usage}`", inline=False)
        
        examples_text = "\n".join([f"`{example}`" for example in examples])
        embed.add_field(name="Examples", value=examples_text, inline=False)
        
        return embed
