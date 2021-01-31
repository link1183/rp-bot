from discord.ext import commands
from discord import Embed, Activity, ActivityType, Color
from cogs.utils.utilitiesBot import get_config


class StartCog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def start(self, ctx):
        """Changes the activity of the bot."""

        await ctx.message.delete()

        config = get_config()
        embed = Embed(title=f'Activity changed to "{config["starting"]}"', description=Embed.Empty, colour=Color.dark_blue())
        await ctx.send(embed=embed, delete_after=5)
        await self.client.change_presence(activity=Activity(type=ActivityType.playing, name=config['starting']))


def setup(client):
    client.add_cog(StartCog(client))
