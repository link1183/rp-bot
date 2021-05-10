import discord
from discord.ext import commands, tasks
import sys


class RestartLoopCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loop.start()

    
    @tasks.loop(hours=24.0)
    async def loop(self, ctx):
        sys.exit(0)


def setup(client):
    client.add_cog(RestartLoopCog(client))
