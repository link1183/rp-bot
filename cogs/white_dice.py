# made by : https://github.com/jubnl

from discord.ext import commands
from discord import Embed
from random import choice


class WhiteDiceCog(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="white",description="message for white dices")
    async def white(self,ctx):

        await ctx.message.delete()
        white_color = "#FFFFFF"
        emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        readableHex = int(hex(int(white_color.replace("#", ""), 16)), 0)
        embed=Embed(title=":white_medium_square: Dés blancs",
                    description="Réagissez avec le nombre de dés que vous voulez lancer",
                    colour=readableHex)
        
        embed.add_field(name="Résultats possibles :", value="⚪ : 16.66% de chance\n⚫ : 50% de chance\n⚪⚪ : 25% de chance\n⚫⚫ : 8.33% de chance")

        react = await ctx.send(embed=embed)

        for emoji in emojis:
            await react.add_reaction(emoji)


    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self,payload):

        message_id = payload.message_id
        
        if message_id == 801919469848625163 :
            
            if payload.emoji.name == '1️⃣':
                count = 1
            elif payload.emoji.name == '2️⃣':
                count = 2
            elif payload.emoji.name == '3️⃣':
                count = 3
            elif payload.emoji.name == '4️⃣':
                count = 4
            elif payload.emoji.name == '5️⃣':
                count = 5
            elif payload.emoji.name == '6️⃣':
                count = 6
            elif payload.emoji.name == '7️⃣':
                count = 7
            elif payload.emoji.name == '8️⃣':
                count = 8
            elif payload.emoji.name == '9️⃣':
                count = 9
            else:
                return
                        
            
            channel = self.client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = payload.member
            await message.remove_reaction(payload.emoji, member)



            dices = ['⚪','⚪','⚪⚪','⚪⚪','⚪⚪','⚫','⚫','⚫','⚫','⚫','⚫','⚫⚫']

            value = ""

            for i in range(count):
                value+=f"Lancé {i+1} : {choice(dices)}\n"

            white_color = "#FFFFFF"
            readableHex = int(hex(int(white_color.replace("#", ""), 16)), 0)
            
            embed = Embed(title=f":white_medium_square: Lancé de dés blanc pour {member.display_name}",colour=readableHex)
            embed.add_field(name=f"Nombre de dés lancés : {count}",value=value)

            channel = self.client.get_channel(801793957062639666)

            await channel.send(embed=embed)


def setup(client):
    client.add_cog(WhiteDiceCog(client))

