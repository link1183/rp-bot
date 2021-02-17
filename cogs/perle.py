import discord
from discord.ext import commands
from datetime import datetime


class PerleCog(commands.Cog, name="Commande perle"):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def perle(self, ctx, member: discord.Member,* , sentence=None):
        """Send a message in #perles."""
        
        sep = '"'

        if sentence == None:
            sentence = ''
            sep = ''

        channel = self.client.get_channel(774362633364963398)
        embed = discord.Embed(title=f'{sep}{sentence}{sep}', colour=discord.Color.red())
        embed.set_footer(text=f'Par {member.name}', icon_url=member.avatar_url)
        embed.timestamp = datetime.now()
        if ctx.message.attachments != []:
            for i in ctx.message.attachments:
                embed.set_image(url=i.url)
        await channel.send(embed=embed)
        await ctx.message.delete()


def setup(client):
    client.add_cog(PerleCog(client))
    