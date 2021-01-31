# made by : https://github.com/jubnl

from discord.ext import commands
import sys


class RestartCog(commands.Cog, name="Commande !exit"):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,10)
    @commands.command(name="restart",description=":\nrestart le bot", hidden=True)
    async def restart(self,ctx):
        """Restarts the bot."""

        await ctx.message.delete()
        
        await ctx.send("Le bot va redémarrer, veuillez patienter quelques secondes...", delete_after=5)
        sys.exit(0)


def setup(client):
    client.add_cog(RestartCog(client))
    