# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class UnmuteCog(commands.Cog, name="Commande !unmute"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(name="unmute",description="[@member] :\nPermet d'unmute un membre")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):

        
        mute_role = discord.utils.get(member.guild.roles, name='Muted')
        for role in member.roles:
            if mute_role == role:
                await member.remove_roles(mute_role)
                embed = discord.Embed(title='Unmute',
                                    description=f'{ctx.message.author} unmuted {member}.',
                                    color=discord.Color.light_grey())
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.channel.send(embed=embed)
                channel = discord.utils.get(member.guild.channels, id=734427047404765267)
                embed = discord.Embed(title='Demute log', description='', colour=discord.Color.light_grey())
                embed.add_field(name='From:', value=fr'{ctx.message.author}', inline=False)
                embed.add_field(name='On:', value=fr'{member}', inline=False)
                embed.add_field(name='In:', value=f'{ctx.channel}', inline=False)
                await channel.send(embed=embed)
                return

        if mute_role not in member.roles:
            await ctx.channel.send(f'{member} is not muted.')

def setup(client):
    client.add_cog(UnmuteCog(client))