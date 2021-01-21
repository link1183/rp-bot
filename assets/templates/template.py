# made by : https://github.com/jubnl

from discord.ext import commands
from cogs.utils.utilitiesBot import get_client


class TemplateCog(commands.Cog, name="Commande !template"):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @commands.cooldown(1,10) # N'ENLEVEZ CETTE LIGNE EN AUCUN CAS
    @client.command(name="A remplir",description="A remplir")
    async def template(self,ctx):
        await ctx.message.delete()
        pass

def setup(client):
    client.add_cog(TemplateCog(client))