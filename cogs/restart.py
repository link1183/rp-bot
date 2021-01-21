# made by : https://github.com/jubnl

from discord.ext import commands
import sys
from cogs.utils.utilitiesBot import get_client


class RestartCog(commands.Cog, name="Commande !exit"):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @commands.cooldown(1,10)
    @client.command(name="restart",description=":\nrestart le bot",hidden=True)
    # @commands.has_role('DevBot' or 'Super Admin' or 'Admin')
    async def restart(self,ctx):
        await ctx.message.delete()
        await ctx.send("Le bot va redémarrer, veuillez patienter quelques secondes...")
        sys.exit(0)

def setup(client):
    client.add_cog(RestartCog(client))