# made by : https://github.com/jubnl

import discord
from discord.ext import commands


class BanlistCog(commands.Cog, name="Commande !banlist"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(aliases=['bl'],name="banlist",description=" :\nListe des membres bannis",hidden=True)
    @commands.has_permissions(ban_members=True)
    async def banlist(self, ctx):
        """affiche la liste des membres bannis"""

        embed = discord.Embed(title='Banlist', color=discord.Color.dark_red())
        ban_list = await ctx.guild.bans()
        i = 0
        for b in ban_list:
            user = b.user
            embed.add_field(name=f'{user.name}#{user.discriminator}', value=b.reason, inline=False)
            i+=1
        if i == 0:
            embed.add_field(name='No banned users.', value="-", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(BanlistCog(client))