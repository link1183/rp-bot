from discord import Embed, Color
from discord.ext import commands
from os import listdir
from os.path import isfile, join, isdir
from pathlib import Path


class LinesCog(commands.Cog, name='Commande !lines'):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1, 10)
    @commands.command(name='lines', description='Affiche le nombre de lignes de codes total de l\'ensemble des fichiers du bot')
    async def line(self, ctx):

        #def is_invoke(m):
        #    return m.id == ctx.message.id
        #await ctx.channel.purge(limit=1, check=is_invoke)
        await ctx.message.delete()
        # get path for cogs
        mod_path = Path(__file__).parent.parent

        # retrive all cogs files
        def getListOfFiles(dirName):
            # create a list of file and sub directories 
            # names in the given directory 
            listOfFile = listdir(dirName)
            allFiles = list()
            # Iterate over all the entries
            for entry in listOfFile:
                # Create full path
                fullPath = join(dirName, entry)
                # If entry is a directory then get the list of files in this directory 
                if isdir(fullPath):
                    allFiles = allFiles + getListOfFiles(fullPath)
                else:
                    if fullPath[-3:] == ".py": allFiles.append(fullPath)
                        
            return allFiles
        
        line_count = 0

        cogs_files = getListOfFiles(mod_path)

        # print(cogs_files)

        for file in cogs_files:

            with open(file, 'r') as lines:

                for line in lines:

                    if line != "\n":

                        line_count += 1

        
        embed = Embed(title='Total number of code lines of this bot.', description=f'{line_count}', colour=Color.dark_blue())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(LinesCog(client))
