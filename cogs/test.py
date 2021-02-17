import discord
from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx, blah='test'):
        for i in ctx.message.attachments:
            embed = discord.Embed()
            embed.set_image(url=i.url)
            await ctx.send(embed=embed)
        await ctx.message.delete()

    

def setup(client):
    client.add_cog(TestCog(client))
