from discord.ext import commands
from discord import Embed, Activity, ActivityType, Color
from cogs.utils.utilitiesBot import get_client, get_config


class StartCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    client = get_client()
    config = get_config()
    
    
    @client.command()
    async def start(self, ctx):
        embed = Embed(title=f'Activity changed to {config['playing']}', description=Embed.Empty, colour=Color.dark_blue())
        await ctx.send(embed=embed)
        await client.change_presence(activity=Activity(type=ActivityType.playing, name=config['starting']))


def setup(client):
    cliend.add_cog(client)
