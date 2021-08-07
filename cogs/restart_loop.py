from discord.ext import commands, tasks
import sys


class RestartLoopCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status = 0
        self.loop.start()

    
    @tasks.loop(hours=24.0)
    async def loop(self):
        print('24 hours loop is starting')
        if self.status != 0:
            sys.exit(0)
        self.status += 1


    @loop.before_loop
    async def before_loop(self):
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(RestartLoopCog(client))
