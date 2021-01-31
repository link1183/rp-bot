import discord
from discord.ext import commands
from cogs.utils.utilitiesBot import get_client
from datetime import datetime


class PerleCog(commands.Cog, name="Commande perle"):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @client.command()
    async def perle(self, ctx, member: discord.Member,* , sentence=None):
        await ctx.message.delete()
        channel = self.client.get_channel(774362633364963398)
        embed = discord.Embed(title=f'"{sentence}"', colour=discord.Color.red())
        embed.set_footer(text=f'Par {member.name}', icon_url=member.avatar_url)
        embed.timestamp = datetime.now()
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(PerleCog(client))
    