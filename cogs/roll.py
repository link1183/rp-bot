import discord
from discord.ext import commands
import random
from cogs.utils.Utilities import get_client, dices_results


class RollCog(commands.Cog, name='Commande !roll'):

    def __init__(self, client):
        self.client = client
    
    client = get_client()
    @client.command()
    async def roll(self, ctx, green=0, yellow=0, purple=0, red=0, white=0):
        results_green = []
        results_yellow = []
        results_purple = []
        results_red = []
        results_white = []

        for i in range(green):
            result = random.choice(dices_results['green'])
            results_green.append(result)

        for i in range(yellow):
            result = random.choice(dices_results['yellow'])
            results_yellow.append(result)
    
        for i in range(purple):
            result = random.choice(dices_results['purple'])
            results_purple.append(result)
    
        for i in range(red):
            result = random.choice(dices_results['red'])
            results_red.append(result)
    
        for i in range(white):
            result = random.choice(dices_results['white'])
            results_white.append(result)
    
        separator = ', '

        msg_green = separator.join(results_green)
        msg_yellow = separator.join(results_yellow)
        msg_purple = separator.join(results_purple)
        msg_red = separator.join(results_red)
        msg_white = separator.join(results_white)

        if msg_green == '':
            msg_green = 'No dices rolled'
    
        if msg_yellow == '':
            msg_yellow = 'No dices rolled'
    
        if msg_purple == '':
            msg_purple = 'No dices rolled'
    
        if msg_red == '':
            msg_red = 'No dices rolled'
    
        if msg_white == '':
            msg_white = 'No dices rolled'

    
        embed = discord.Embed(title='Dices results', description=discord.Embed.Empty, colour=discord.Color.blue())

        embed.add_field(name=':green_square: Green Dices', value=f'{msg_green}', inline=False)
        embed.add_field(name=':yellow_square: Yellow Dices', value=f'{msg_yellow}', inline=False)
        embed.add_field(name=':purple_square: Purple Dices', value=f'{msg_purple}', inline=False)
        embed.add_field(name=':red_square: Red Dices', value=f'{msg_red}', inline=False)
        embed.add_field(name=':white_large_square: White Dices', value=f'{msg_white}', inline=False)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(RollCog(client))