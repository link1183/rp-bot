import discord
from discord.ext import commands
from cogs.utils.Utilities import get_client


class ClearCog(commands.Cog, name='Commande +clear'):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @commands.has_permissions(manage_messages=True)
    @client.command()
    async def clear(self, ctx, amount=7):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} messages ont étés supprimés avec succès.', delete_after=5)


def setup(client):
    client.add_cog(ClearCog(client))