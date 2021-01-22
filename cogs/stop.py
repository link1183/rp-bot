from discord.ext import commands
from discord import Embed, Activity, Color
from cogs.utils.utilitiesBot import get_client, get_config


class StopCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    client = get_client()
    config = get_config()
    
    
    @client.command(name='stop', description="Change l'activité du bot")
    async def stop(self, ctx):
        embed = Embed(title=f'Activity changed to {config['waiting']}', description=Embed.Empty, colourColor.dark_blue())
        await ctx.send(embed=embed)
        await client.change_presence(activity=Activity(type=ActivityType.playing, name=config['waiting']))


def setup(client):
    cliend.add_cog(client)
