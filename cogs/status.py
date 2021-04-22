from discord.ext import commands
from discord_slash import SlashContext, cog_ext


class StatusCog(commands.Cog, name='auto live message'):

    def __init__(self, client):
        self.client = client
        self.status = 0

    
    @cog_ext.cog_slash(name='status', guild_ids=[733000706088501309])
    async def status(self, ctx: SlashContext):
        await ctx.send(content=self.status)


def setup(client):
    client.add_cog(StatusCog(client))