# made by : https://github.com/jubnl

from discord.ext import commands
from discord import Embed, Color
from random import choice


class GreenDiceCog(commands.Cog,name="command green"):

    def __init__(self, client):
        self.client = client


    @commands.command(name="green",description="message for green dices")
    async def green(self,ctx):
        """Send the message used by the listener for the green dice."""

        await ctx.message.delete()

        emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        embed=Embed(title=":green_square: Dés verts",
                    description="Réagissez avec le nombre de dés que vous voulez lancer",
                    colour=Color.green()
                    )

        embed.add_field(name="Résultats possibles :",value="1x Avantage : 37.5% de chance\n2x Avantage : 12.5% de chance\n1x Avantage + 1x Réussite : 12.5% de chance\n1x Réussite : 12.5% de chance\n2x Réussite : 12.5% de chance\n1x Rien : 12.5% de chance")
        react = await ctx.send(embed=embed)

        for emoji in emojis:
            await react.add_reaction(emoji)


    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self, payload):
        """Listener for the reactions on the green dice message."""

        message_id = payload.message_id
        
        if message_id == 802142991619850250 :
            
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



            dices = ['Réussite', 'Avantage', 'Avantage', 'Avantage', 'Double avantage', 'Double réussite', 'Avantage/réussite', 'Rien']

            value = ""

            reussites = 0
            avantages = 0

            for i in range(count):
                rand_choice = choice(dices)
                value+=f"Lancé {i+1} : {rand_choice}\n"
                if rand_choice == "Réussite":
                    reussites+=1
                elif rand_choice == "Avantage":
                    avantages+=1
                elif rand_choice == "Double réussite":
                    reussites+=2
                elif rand_choice == "Double avantage":
                    avantages+=2
                elif rand_choice == "Avantage/réussite":
                    avantages+=1
                    reussites+=1
            

            embed = Embed(title=f":green_square: Lancé de dés verts pour {member.display_name}",colour=Color.green())
            embed.add_field(name=f"Nombre de dés lancés : {count}",value=value)
            embed.add_field(name="Résultats :",value=f"Réussites : {reussites}\nAvantages : {avantages}")

            channel = self.client.get_channel(801793957062639666)

            await channel.send(embed=embed)



def setup(client):
	client.add_cog(GreenDiceCog(client))
    