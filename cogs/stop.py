from discord.ext import commands
from discord import Embed, Activity, ActivityType, Color
from cogs.utils.utilitiesBot import get_config
from discord_slash import cog_ext, SlashContext


class StopCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name='stop', description="Change l'activité du bot", guild_ids=[769252209090625566])
    async def stop(self, ctx: SlashContext):
        """Changes the activity of the bot."""

        config = get_config()
        embed = Embed(title=f'Activity changed to "{config["waiting"]}"', description=Embed.Empty, colour=Color.dark_blue())
        await ctx.send(embed=embed, delete_after=5)
        await self.client.change_presence(activity=Activity(type=ActivityType.playing, name=config['waiting']))


def setup(client):
    client.add_cog(StopCog(client))
