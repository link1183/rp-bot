import discord
from discord.ext import commands


class TGCMCog(commands.Cog, name='Commande +tgcm'):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def tgcm(self, ctx, user: discord.Member):
        embed = discord.Embed(title=f'Ta gueule. Juste, ta gueule, c\'est magique.', description=discord.Embed.Empty, colour=discord.Color.dark_green())
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(TGCMCog(client))
    