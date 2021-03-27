import discord
from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx, blah='test'):
        await ctx.send(ctx.author.guild.id)

    

def setup(client):
    client.add_cog(TestCog(client))
