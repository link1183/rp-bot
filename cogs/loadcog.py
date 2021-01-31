# made by : https://github.com/jubnl

import discord
from discord.ext import commands
from pathlib import Path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import traceback
from cogs.utils.utilitiesBot import get_client


class LoadCog(commands.Cog, name="Commande !userinfo"):

    def __init__(self, client):
        self.client = client

    client=get_client()

    @commands.cooldown(1,10)
    @client.command(name='load', hidden=True,description="[cog] :\nCharge le cog specifié")
    async def load(self, ctx, *, cog: str):
        await ctx.message.delete()
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        if ctx.author.id != 222775418590068736:
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
                
                channel = self.client.get_channel(769190738968838148)
                for cog in files: 
                    cog = f"cogs.{cog}"
                    try:
                        await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO LOAD`** {cog[5:]}",delete_after=10)
                        self.client.load_extension(cog)
                    except commands.ExtensionAlreadyLoaded:
                        await ctx.send(f"**`[{dt_string}] :` COG {cog[5:]} is ALREADY LOADED**")
                    except Exception as e:
                        embed=discord.Embed()
                        embed.add_field(name=f"**`[{dt_string}] : FAILED TO LOAD` {cog[5:]}**",value=f'```py\n{traceback.format_exc()}\n```')
                        await channel.send(embed=embed)
                    else:
                        await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY LOADED COG`** **{cog[5:]}**',delete_after=10)
            else:
                cog = f"cogs.{cog}"
                try:
                    await ctx.send(f"**`[{dt_string}] : ATTEMPTING TO LOAD`** {cog[5:]}",delete_after=10)
                    self.client.load_extension(cog)
                except commands.ExtensionAlreadyLoaded:
                    await ctx.send(f"**`[{dt_string}] :` COG {cog[5:]} is ALREADY LOADED**")
                except Exception as e:
                    channel = self.client.get_channel(769190738968838148)
                    await channel.send(traceback.format_exc())
                else:
                    await ctx.send(f'**`[{dt_string}] : SUCCESSFULLY LOADED COG`** **{cog[5:]}**',delete_after=10)


def setup(client):
    client.add_cog(LoadCog(client))
