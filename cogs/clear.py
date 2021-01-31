from discord.ext import commands
from cogs.utils.utilitiesBot import get_client


class ClearCog(commands.Cog, name='Commande +clear'):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @commands.has_permissions(manage_messages=True)
    @client.command()
    async def clear(self, ctx, amount=7):
        """
        @param ctx: context object
        @param amount: the amount of messages to delete (default value = 7)

        This command deletes a certain amount of messages into the context channel
        """
        
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages ont étés supprimés avec succès.', delete_after=5)


def setup(client):
    client.add_cog(ClearCog(client))
    