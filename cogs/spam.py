# made by : https://github.com/jubnl

from discord.ext import commands
from discord.ext.commands.core import cooldown
import re


class SpamCog(commands.Cog, name="Commande +spam [@member]"):

    def __init__(self, client):
        self.client = client

    @cooldown(1, 180)
    @commands.has_permissions(administrator=True)
    @commands.command(name="spam",description=" [@member] [nombre de spam] (message à spam) :\nspam un membre")
    async def spam(self, ctx, member=None, nombre=None,* , message=None):
        await ctx.message.delete()

        if member is not None:

            try:
                victim = int(re.sub(r'\D','',member))

            except Exception:
                return await ctx.send("Veuillez specifier un membre du discord [@member]",delete_after=5)

            else:
                victim = self.client.get_user(victim)

        else:
            return await ctx.send("Veuillez specifier un membre du discord [@member]",delete_after=5)


        try:
            nombre = int(nombre)
            if nombre>15:
                nombre=15

        except ValueError:
            return await ctx.send("Veuillez entrer un nombre valide [nombre]",delete_after=5)


        if message is None:
            message = "spam"

        try:
            await victim.send(f"de la part de {ctx.author.display_name} :")

            for _ in range(nombre):
                await victim.send(message)

        except Exception:
            await ctx.send(f"{victim.display_name} a bloqué le bot.",delete_after=5)


def setup(client):
    client.add_cog(SpamCog(client))
