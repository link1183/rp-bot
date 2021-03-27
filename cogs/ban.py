# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class BanCog(commands.Cog, name="Commande !ban"):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,10)
    @commands.command(name="ban",description="[@member] :\nban un membre")
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        """commande pour bannir les membres"""
        
        
        if reason is None:
            reason = 'No specified reason'

        # errors
        if member is None:
            return await ctx.send('Please enter a valid username.', delete_After=5)

        if member.id == ctx.author.id:
            return await ctx.send("Why do you want to ban yourself?", delete_After=5)
        
        # send message user
        embed = discord.Embed(title=f'You were banned from the discord server {ctx.guild.name} for: "{reason}".', colour=discord.Color.dark_red())
        embed = discord.Embed(title='Ban log', description='', colour=discord.Color.dark_red())

        # content message send user and log
        embed.add_field(name='From:', value=f'<@{ctx.author.id}>', inline=False)
        embed.add_field(name='On:', value=fr'{member}', inline=False)
        embed.add_field(name='For:', value=f'{reason}', inline=False)
        embed.add_field(name='In:', value=f'<#{ctx.channel.id}>', inline=False)
        await member.send(embed=embed)

        # view ban user
        embed_ban = discord.Embed(title=f'{member.display_name} was successfully banned for: "{reason}"', colour=discord.Color.dark_red())
        embed_ban.set_thumbnail(url=member.avatar_url)
        
        # ban
        await member.ban(reason=reason)
        await ctx.channel.send(embed=embed_ban)
        
        # logs
        channel = discord.utils.get(member.guild.channels, id=734427047404765267)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(BanCog(client))