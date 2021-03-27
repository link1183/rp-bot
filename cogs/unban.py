# made by : https://github.com/jubnl

import discord
from discord.ext import commands



class PardonCog(commands.Cog, name="Commande !pardon"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(aliases=['pardon'],name="unban",description="[username#discriminator] :\nunban un membre")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member=None):
        """commande pour débannir les membres"""

        if member is None:
            await ctx.channel.send('Please enter a valid user.')
            return

        ban_list = await ctx.guild.bans()
            
        name, disc = member.split('#')
        for b in ban_list:
            user = b.user
            if (name, disc) == (user.name, user.discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=fr'{member} was successfully unbanned.', colour=discord.Color.red(),
                                        description='')
                await ctx.channel.send(embed=embed)
                return

        channel = discord.utils.get(member.guild.channels, id=734427047404765267)
        embed = discord.Embed(title='Unban log', description='', colour=discord.Color.blue())
        embed.add_field(name='from:', value=fr'{ctx.message.author}', inline=False)
        embed.add_field(name='On:', value=fr'{member}', inline=False)
        embed.add_field(name='In:', value=f'{ctx.channel}', inline=False)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(PardonCog(client))