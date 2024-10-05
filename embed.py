import discord
import json
from datetime import datetime


class F1Embed:
    def __init__(self, event):
        self.event = event
        self.country_flags = self.load_country_flags()

    def load_country_flags(self):
        # Load country flag URLs from a JSON file
        with open("country_flags.json", "r") as f:
            country_flags = json.load(f)
        return country_flags

    def create_embed(self):
        embed = discord.Embed(title="Next F1 Event", color=discord.Color.blue())

        # Calculate time to go
        current_time = datetime.utcnow()
        time_to_go = self.event.start_time - current_time
        days, seconds = time_to_go.days, time_to_go.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        time_remaining = f"{days} Days, {hours} Hours, {minutes} Minutes" if days > 0 else f"{hours} Hours, {minutes} Minutes"

        # Get the flag URL
        flag_url = self.country_flags.get(self.event.country,
                                          "https://example.com/default_flag.png")  # Default flag if country not found

        # Add fields for race name, event type, and time to go
        embed.add_field(name="Race Name", value=self.event.race_name, inline=False)
        embed.add_field(name="Event Type", value=self.event.event_type, inline=False)
        embed.add_field(name="Location", value=self.event.location, inline=False)
        embed.add_field(name="Time to Go", value=time_remaining, inline=False)

        # Set the flag URL as a thumbnail
        embed.set_thumbnail(url=flag_url)

        return embed
