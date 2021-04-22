import discord
from discord.ext import commands
from cogs.utils.utilitiesBot import get_config
from discord_slash import cog_ext, SlashContext


class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @cog_ext.cog_slash(name='test', guild_ids=[733000706088501309])
    async def test(self, ctx: SlashContext):
        await ctx.send(content='test')


def setup(client):
    client.add_cog(TestCog(client))
