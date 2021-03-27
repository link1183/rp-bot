# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class WarnCog(commands.Cog, name="Commande !warn"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(name="warn",description="[@member] :\navertis un membre")
    @commands.has_permissions(ban_members=True)
    async def warn(self,ctx, member: discord.Member, *, reason=None):
        """permet d'avertir un membre"""

        
        if reason is None:
            reason = 'Pas de raison spécifiée'

        embed = discord.Embed(title='Warn',
                            colour=discord.Color.red(),
                            description=f'{member.mention}, you were warned by'
                                        f' {ctx.message.author} for: '
                                        f'"{reason}". Don\'t do that again please.')
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.channel.send(embed=embed)
        channel = discord.utils.get(member.guild.channels, id=734427047404765267)
        embed = discord.Embed(title='Warn log', description='', colour=discord.Color.red())
        embed.add_field(name='From:', value=fr'{ctx.message.author}', inline=False)
        embed.add_field(name='On:', value=fr'{member}', inline=False)
        embed.add_field(name='For:', value=f'{reason}', inline=False)
        embed.add_field(name='In:', value=f'{ctx.channel}', inline=False)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(WarnCog(client))