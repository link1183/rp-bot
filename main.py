import discord
from discord import colour
from discord.ext import commands
import json
from pathlib import Path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import traceback

client = commands.Bot(command_prefix='+')

# get path for cogs
mod_path = Path(__file__).parent
relative_path_cogs = 'cogs/'
cogs_folder = (mod_path / relative_path_cogs).resolve()

# retrive all cogs files
cogs_files = [f"cogs.{f[:-3]}" for f in listdir(cogs_folder) if isfile(join(cogs_folder, f))]

if __name__ == '__main__':
    for extension in cogs_files:
        try:
            client.load_extension(extension)
        except Exception:
            # A FAIRE : AJOUTER UN PUTAIN DE SYSTEME DE LOG POUR LOAD LES EXTENSIONS C'EST CHIANT DE PASSER PAR PUTTY
            traceback.print_exc()


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
        await ctx.send(f'Il manque un argument !',delete_after=5)

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
        

@client.event
async def on_ready():
    print('bot ready')
    channel = client.get_channel(771496855044882463)
    embed = discord.Embed(title='Bot is now ready', description=discord.Embed.Empty, colour=discord.Color.dark_blue())
    await channel.send(embed=embed)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Waiting for RP to start'))


client.run('NzcxNDk2MDE3NTY4ODU4MTI0.X5s9qA.8oy-vA2830IoJhq6eCsDl7AjTik', bot=True, reconnect=True)