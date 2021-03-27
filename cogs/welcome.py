import discord
from discord.ext import commands


class WelcomeCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(733002044784246864)
        
        if channel is None or member is None:
            return
        
        if member.guild.id != 733000706088501309:
            return

        await member.add_roles(discord.utils.get(member.guild.roles, id=734427182738178159))
        
        if member.id == 491951489565196289:
            await member.add_roles(discord.utils.get(member.guild.roles, id=825464868231446588))

        embed = discord.Embed(title=f'Welcome {member.name} to the discord server!', description=discord.Embed.Empty, colour=discord.Color.dark_gray())
        await channel.send(embed=embed)



def setup(client):
    client.add_cog(WelcomeCog(client))
