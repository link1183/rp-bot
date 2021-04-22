import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class TGCMCog(commands.Cog, name='Commande +tgcm'):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name='TGCM', description='Ta gueule, juste, ta gueule, c\'est magique.', guild_ids=[769252209090625566])
    async def tgcm(self, ctx: SlashContext):
        """Send the TGCM embed."""
        
        embed = discord.Embed(title=f'Ta gueule. Juste, ta gueule, c\'est magique.', description=discord.Embed.Empty, colour=discord.Color.dark_green())
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(TGCMCog(client))
    