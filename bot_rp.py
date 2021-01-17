import discord
from discord.ext import commands
import random
import traceback
from datetime import datetime
import json
from pathlib import Path
from os import listdir
from os.path import isfile, join

dices_results = {
    "green": ['test1', 'test2'],
    "yellow": ['test3', 'test4'],
    "purple": ['test5', 'test6'],
    "red": ['test7', 'test8'],
    "white": ['test9', 'test10']
}

client = commands.Bot(command_prefix='+')


@client.command()
async def test(ctx):
    guild = client.get_guild(769252209090625566)
    print(guild.roles)


@client.event
async def on_ready():
    channel = client.get_channel(771496855044882463)
    embed = discord.Embed(title='Bot is now ready', description='', colour=discord.Color.default())
    await channel.send(embed=embed)


@client.event
async def on_command_error(ctx, error):

    # create traceback
    trcError = f'```py\n{traceback.format_exc()}\n```'

    def is_invoke(m):
        return m.id == ctx.message.id
    await ctx.channel.purge(limit=1, check=is_invoke)

    # return error message
    if isinstance(error, commands.MissingRole):
        await ctx.send('Vous n\'avez pas le rôle requis !',delete_after=5)

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Il manque un argument ! Tapez la commande `+help {(ctx.message.content.split(" ", 1)[0])[1:]}`',delete_after=5)

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('Vous n\'avez pas la permission d\'executer cette commande !',delete_after=5)

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Veuillez réessayer dans {error.retry_after:.0f} secondes',delete_after=5)

    elif isinstance(error, commands.CommandError):
        embed = discord.Embed(title="Log :",timestamp=datetime.now(), description=trcError)
        embed.add_field(name="Envoyé dans :",value=f"<#{ctx.channel.id}>")
        embed.add_field(name="Envoyé par :",value=ctx.author.display_name)
        embed.add_field(name="Commande envoyée :",value=ctx.message.content,inline=False)
        embed.add_field(name="Erreur :",value=error,inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        log = client.get_channel(771496855044882463)
        await log.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(title=':ping_pong: Pong !', description='', colour=discord.Color.red())
    embed.add_field(name='**{round(client.latency * 1000)} ms.**', value=discord.Embed.Empty, inline=False)
    await ctx.send(embed=embed)


@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, amount=7):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages ont étés supprimés avec succès.', delete_after=5)


@client.command()
async def tgcm(ctx, user: discord.Member):
    embed = discord.Embed(title=f'Ta gueule. Juste, ta gueule, c\'est magique.', description=discord.Embed.Empty, colour=discord.Color.dark_green())
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


# COMMANDES RP HUGP
@client.command()
async def roll(ctx, green, yellow=0, purple=0, red=0, white=0):
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
    




client.run('NzcxNDk2MDE3NTY4ODU4MTI0.X5s9qA.8oy-vA2830IoJhq6eCsDl7AjTik')