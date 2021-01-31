# made by : https://github.com/jubnl

import discord
from discord.ext import commands
from discord.ext.commands.core import cooldown
import re


class SpamCog(commands.Cog, name="Commande +spam [@member]"):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command(name="spam",description=" [@member] [nombre de spam] (message à spam) :\nspam un membre")
    async def spam(self, ctx, member: discord.Member, nombre=10, *, message=None):

        await ctx.message.delete()

        if isinstance(member, discord.Member):
            pass

        else:
            return await ctx.send("Veuillez specifier un membre du discord [@member]",delete_after=5)


        try:
            nombre = int(nombre)

        except ValueError:
            return await ctx.send("Veuillez entrer un nombre valide [nombre]",delete_after=5)


        if message is None:
            message = "spam"

        try:
            await member.send(f"de la part de {ctx.author.display_name} :")

            for _ in range(nombre):
                await member.send(message)

        except Exception:
            await ctx.send(f"{member.display_name} a bloqué le bot.",delete_after=5)


def setup(client):
    client.add_cog(SpamCog(client))
