# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class MuteCog(commands.Cog, name="Commande !mute"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(name="mute",description="[@member] :\npermet de mute un membre")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, reason=None):

        if reason is None:
            reason = 'No specified reason.'

        await member.add_roles(discord.utils.get(member.guild.roles, id=825462327922262016))
        embed_mute = discord.Embed(title='Mute', colour=discord.Color.light_gray(),
                            description=f'{member}'
                                        f' was successfully muted by {ctx.author}.')
        embed_mute.add_field(name="Reason: ", value=f'{reason}')
        embed_mute.set_thumbnail(url=member.avatar_url)
        await ctx.channel.send(embed=embed_mute)
        channel = discord.utils.get(member.guild.channels, id=734427047404765267)
        embed_mute_log = discord.Embed(title='Mute log', description='', colour=discord.Color.light_gray())
        embed_mute_log.add_field(name='From:', value=fr'{ctx.message.author}', inline=False)
        embed_mute_log.add_field(name='On:', value=fr'{member}', inline=False)
        embed_mute_log.add_field(name='For:', value=f'{reason}', inline=False)
        embed_mute_log.add_field(name='In:', value=f'{ctx.channel}', inline=False)
        await channel.send(embed=embed_mute_log)

def setup(client):
    client.add_cog(MuteCog(client))