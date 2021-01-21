# made by : https://github.com/jubnl

from discord.ext import commands
from cogs.utils.utilitiesBot import get_client
from discord import Embed, Color


class WhiteDiceCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @client.command(name="white",description="message for white dices")
    async def white(self,ctx):
        await ctx.message.delete()
        white_color = "#FFFFFF"
        emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        readableHex = int(hex(int(white_color.replace("#", ""), 16)), 0)
        embed=Embed(title=":white_medium_square: Dés blancs",
                    description="Réagissez avec le nombre de dés que vous voulez lancer",
                    colour=readableHex
                    )
        
        react = await ctx.send(embed=embed)

        for emoji in emojis:
            await react.add_reaction(emoji)
        



def setup(client):
    client.add_cog(WhiteDiceCog(client))