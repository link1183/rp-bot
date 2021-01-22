from discord.ext import commands
from cogs.utils.utilitiesBot import get_client, get_config


class StartCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    self.client = get_client()
    self.config = get_config()
    
    
    @self.client.command()
    async def start(self, ctx):
        embed = discord.Embed(title=f'Activity changed to {config['playing']}', description=discord.Embed.Empty, colour=discord.Color.dark_blue())
        await ctx.send(embed=embed)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=config['starting']))


def setup(client):
    cliend.add_cog(client)
