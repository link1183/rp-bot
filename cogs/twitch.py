import discord
from discord.ext import commands


class TwitchCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ttv(self, ctx):
        await ctx.send(ctx.message.author.desktop_status)


    @commands.Cog.listener(name='on_member_update')
    async def on_member_update(self, before, after):
        channel = self.client.get_channel(823957275151564810)
        await channel.send(before)
        await channel.send(after)
    

def setup(client):
    client.add_cog(TwitchCog(client))

