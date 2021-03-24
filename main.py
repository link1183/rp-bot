# made by : https://github.com/jubnl

import discord
from discord.ext import commands
import json
from pathlib import Path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import traceback


# get path for config file
mod_path = Path(__file__).parent
relative_path = 'assets/config/config_bot.json'
config_bot_json = (mod_path / relative_path).resolve()

# load config file in `config`
with open(config_bot_json,'r') as js_config:
    config = json.load(js_config)

# create bot instance
client = commands.Bot(command_prefix=[config['prefix']])

client.remove_command("help")

# get path for cogs
relative_path_cogs = 'cogs/'
cogs_folder = (mod_path / relative_path_cogs).resolve()

# retrive all cogs files
cogs_files = [f"cogs.{f[:-3]}" for f in listdir(cogs_folder) if isfile(join(cogs_folder, f))]
print(cogs_files)


if __name__ == '__main__':
    for extension in cogs_files:
        try:
            client.load_extension(extension)
            print(f"TRY TO LOAD {extension}")
        except Exception as e:
            print(e)
            # A FAIRE : AJOUTER UN PUTAIN DE SYSTEME DE LOG POUR LOAD LES EXTENSIONS C'EST CHIANT DE PASSER PAR PUTTY
            traceback.print_exc()
            continue
        print(f"LOADED {extension}")



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
        await ctx.send(f'Il manque un argument ! Tapez la commande `+help {(ctx.message.content.split(" ", 1)[0])[1:]}`', delete_after=5)

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('Vous n\'avez pas la permission d\'executer cette commande !', delete_after=5)

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Veuillez réessayer dans {error.retry_after:.0f} secondes', delete_after=5)

    elif isinstance(error, commands.CommandError):
        embed = discord.Embed(title="Log :",timestamp=datetime.now(), description=trcError)
        embed.add_field(name="Envoyé dans :",value=f"<#{ctx.channel.id}>")
        embed.add_field(name="Envoyé par :",value=ctx.author.display_name)
        embed.add_field(name="Commande envoyée :",value=ctx.message.content,inline=False)
        embed.add_field(name="Erreur :",value=error,inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        log1 = client.get_channel(771496855044882463)
        log2 = client.get_channel(823957275151564810)
        await log1.send(embed=embed)
        await log2.send(embed=embed)
        

@client.event
async def on_ready():
    channel1 = client.get_channel(771496855044882463)
    channel2 = client.get_channel(823957275151564810)
    embed = discord.Embed(title='Bot is now ready', description=discord.Embed.Empty, colour=discord.Color.dark_blue())
    await channel1.send(embed=embed)
    await channel2.send(embed=embed)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=config['waiting']))


client.run(config['token'], bot=True, reconnect=True)
