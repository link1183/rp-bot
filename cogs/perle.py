import discord
from discord.ext import commands
from datetime import datetime


class PerleCog(commands.Cog, name="Commande perle"):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def perle(self, ctx, member: discord.Member,* , sentence=None):
        """Send a message in #perles."""

        await ctx.message.delete()

        channel = self.client.get_channel(774362633364963398)
        embed = discord.Embed(title=f'"{sentence}"', colour=discord.Color.red())
        embed.set_footer(text=f'Par {member.name}', icon_url=member.avatar_url)
        embed.timestamp = datetime.now()
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(PerleCog(client))
    