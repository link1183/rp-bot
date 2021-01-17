import discord
from discord.ext import commands
from cogs.utils.Utilities import get_client


class PingCog(commands.Cog, name='Commande +ping'):
    def __init__(self, client):
        self.client = client
    
    client = get_client()
    @client.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=':ping_pong: Pong !', description=f'**{round(self.client.latency * 1000)} ms.**', colour=discord.Color.red())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(PingCog(client))