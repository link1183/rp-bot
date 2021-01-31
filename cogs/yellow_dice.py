# made by : https://github.com/jubnl

from discord.ext import commands
from cogs.utils.utilitiesBot import get_client
from discord import Embed, Color
from random import choice


class YellowDiceCog(commands.Cog,name="command yellow"):

    def __init__(self, client):
        self.client = client

    client = get_client()

    @client.command(name="yellow",description="message for yellow dices")
    async def yellow(self,ctx):
        await ctx.message.delete()
        emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        embed=Embed(title=":yellow_square: Dés jaunes",
                    description="Réagissez avec le nombre de dés que vous voulez lancer",
                    colour=Color.gold()
                    )

        embed.add_field(name="Résultats possibles :",value="2x Avantage : 0.08% de chance\n2x Avantage : 0.08% de chance\n2x Réussite : 0.08% de chance\n2x Réussite : 0.08% de chance\n1x Avantage : 0.08% de chance\n1x Avantage : 0.08% de chance\n1x Avantage + 1x Réussite : 0.08% de chance\n1x Avantage + 1x Réussite : 0.08% de chance\n1x Réussite : 0.08% de chance\n1x Réussite : 0.08% de chance\n1x Rien : 0.08% de chance\n1x Réussite critique : 0.08% de chance")
        react = await ctx.send(embed=embed)

        for emoji in emojis:
            await react.add_reaction(emoji)


    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self,payload):
        message_id = payload.message_id
        if message_id == 802199309092782120 :
            
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


            dices = ['réussite', 'réussite', 'Avantage', 'Avantage', 'Double avantage', 'Double avantage', 
                    'Double réussite', 'Double réussite', 'Avantage/réussite', 'Avantage/réussite', 'Rien', 'Réussite critique']

            value = ""

            reussites = 0
            avantages = 0
            reussite_critique = 0

            for i in range(count):
                rand_choice = choice(dices)
                value+=f"Lancé {i+1} : {rand_choice}\n"
                if rand_choice == "réussite":
                    reussites+=1
                elif rand_choice == "Avantage":
                    avantages+=1
                elif rand_choice == "Double réussite":
                    reussites+=2
                elif rand_choice == "Double avantage":
                    avantages+=2
                elif rand_choice == "Désavantage/réussite":
                    avantages+=1
                    reussites+=1
                elif rand_choice == "Réussite critique":
                    reussite_critique += 1

            embed = Embed(title=f":purple_square: Lancé de dés yellow pour {member.display_name}",colour=Color.gold())
            embed.add_field(name=f"Nombre de dés lancés : {count}",value=value)
            if reussite_critique == 0:
                embed.add_field(name="Résultats :",value=f"Réussites : {reussites}\nAvantages : {avantages}", inline=False)
            
            elif reussite_critique > 0:
                embed.add_field(name="Résultats :",value='Réussite critique', inline=False)

            channel = self.client.get_channel(801793957062639666)

            await channel.send(embed=embed)


def setup(client):
	client.add_cog(YellowDiceCog(client))
    