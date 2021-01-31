# made by : https://github.com/jubnl

import discord
from discord.ext import commands
from pathlib import Path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import traceback
import sys


class UnloadCog(commands.Cog, name="Commande !unload"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(name='unload', hidden=True,description="[cog] :\nDécharge un cog")
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner
        """

        await ctx.message.delete()

        if ctx.author.id != 222775418590068736:
            dt_string = datetime.now().strftime("%b-%d-%Y %H:%M:%S")

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
                
                files.remove("utilitiesBot")
                channel = self.client.get_channel(771496855044882463)

                for cog in files:
                    cog = f"cogs.{cog}"

                    try:
                        await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO UNLOAD`** {cog[5:]}",delete_after=10)
                        self.client.unload_extension(cog)

                    except commands.ExtensionAlreadyLoaded:
                        await ctx.send(f"**`[{dt_string}] :` COG {cog[5:]} is ALREADY UNLOADED**")

                    except Exception as e:
                        channel = self.client.get_channel(771496855044882463)
                        embed=discord.Embed(description=f'```py\n{traceback.format_exc()}\n```')
                        embed.add_field(name=f"**`[{dt_string}] : FAILED TO UNLOAD` {cog[5:]}**",value=traceback.print_exc(file=sys.stdout))
                        await channel.send(embed=embed)

                    else:
                        await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY UNLOADED COG`** **{cog[5:]}**',delete_after=10)

            else:
                cog = f"cogs.{cog}"

                try:
                    await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO UNLOAD`** {cog[5:]}",delete_after=10)
                    self.client.unload_extension(cog)

                except commands.ExtensionAlreadyLoaded:
                    await ctx.send(f"**`[{dt_string}] :` COG {cog[5:]} is ALREADY UNLOADED**")

                except Exception:
                    channel = self.client.get_channel(771496855044882463)
                    embed=discord.Embed(description=f'```py\n{traceback.format_exc()}\n```')
                    embed.add_field(name=f"**`[{dt_string}] : FAILED TO UNLOAD` {cog[5:]}**",value=traceback.print_exc(file=sys.stdout))
                    await channel.send(embed=embed)
                    
                else:
                    channel = self.client.get_channel(771496855044882463)
                    await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY UNLOADED COG`** **{cog[5:]}**',delete_after=10)


def setup(client):
    client.add_cog(UnloadCog(client))
    