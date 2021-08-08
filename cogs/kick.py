# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class KickCog(commands.Cog, name="Commande !kick"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(pass_context=True,name="kick",description="[@member] :\nKick le membre tagué")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """commande pour kick les membres"""

        await ctx.message.delete()

        if reason is None:
            reason = 'No specified reason.'

        # Confirmation embed
        embed = discord.Embed(title=fr'{member} was successfully kicked.',
                            description='', colour=discord.Color.red())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Reason:",value=reason)

        await member.kick(reason=reason)
        await ctx.channel.send(embed=embed)

        channel = discord.utils.get(member.guild.channels, id=734427047404765267)

        # Log embed
        embed = discord.Embed(title='Kick log', description='', colour=discord.Color.red())
        embed.add_field(name='From:', value=fr'{ctx.message.author}', inline=False)
        embed.add_field(name='On:', value=fr'{member}', inline=False)
        embed.add_field(name='For:', value=f'{reason}', inline=False)
        embed.add_field(name='In:', value=f'{ctx.channel}', inline=False)
        await channel.send(embed=embed)
        
def setup(client):
    client.add_cog(KickCog(client))