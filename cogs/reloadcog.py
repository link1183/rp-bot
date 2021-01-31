# made by : https://github.com/jubnl

import discord
from discord.ext import commands
from pathlib import Path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import traceback
import sys


class UserInfoCog(commands.Cog, name="Commande !userinfo"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(hidden=True,name="reload",description="[cog] :\nPermet de recharger un cog")
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner
        """

        await ctx.message.delete()

        if 1==1:
            now = datetime.now()
            dt_string = now.strftime("%b-%d-%Y %H:%M:%S")

            if cog == "*" or cog == "all":
                mod_path = Path(__file__).parent
                relative_path_cogs = '../cogs'
                cogs_folder = (mod_path / relative_path_cogs).resolve()
                cogs_files = [f for f in listdir(cogs_folder) if isfile(join(cogs_folder, f))]
                files = []

                for i in cogs_files:
                    size = len(i)
                    f = i[:size -3]
                    files.append(f)

                log = self.client.get_channel(771496855044882463)

                for cog in files: 
                    cog = f"cogs.{cog}"

                    try:
                        await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO RELOAD`** {cog[5:]}",delete_after=10)
                        self.client.unload_extension(cog)
                        self.client.load_extension(cog)

                    except commands.ExtensionAlreadyLoaded:
                        await ctx.send(f"**`[{dt_string}] :` COG {cog[5:]} is ALREADY LOADED**")

                    except Exception as e:
                        print(e)
                        embed=discord.Embed(description=f'```py\n{traceback.format_exc()}\n```')
                        embed.add_field(name=f"**`[{dt_string}] : FAILED TO RELOAD` {cog[5:]}**",value=traceback.print_exc(file=sys.stdout))
                        await log.send(embed=embed)

                    else:
                        await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY RELOADED COG`** **{cog[5:]}**',delete_after=10)

            else:
                cog = f"cogs.{cog}"

                try:
                    await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO RELOAD`** {cog[5:]}",delete_after=10)
                    self.client.unload_extension(cog)
                    self.client.load_extension(cog)

                except Exception as e:
                    print(e)
                    embed=discord.Embed(description=f'```py\n{traceback.format_exc()}\n```')
                    embed.add_field(name=f"**`[{dt_string}] : FAILED TO RELOAD` {cog[5:]}**",value=traceback.print_exc(file=sys.stdout))
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY RELOADED COG`** **{cog[5:]}**',delete_after=10)


def setup(client):
    client.add_cog(UserInfoCog(client))
    