import discord
from discord.ext import commands
from cogs.utils.utilitiesBot import get_config


class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = get_config()


    @commands.command()
    async def test(self, ctx):
        await ctx.send(self.config)
        await ctx.send(self.config['message_sent']['link'])


def setup(client):
    client.add_cog(TestCog(client))
