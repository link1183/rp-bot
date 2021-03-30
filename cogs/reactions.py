import discord
from discord.ext import commands


class RoleCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def reaction(self, ctx):
        await ctx.message.delete()
        emojis = ['🎮']
        embed = discord.Embed(title='Reaction Role', description=':video_game: React to get the <@&801859621009883186> role.', colour=discord.Color.blue())
        
        react = await ctx.send(embed=embed)
        msg_id = ctx.message.id

        for i in emojis:
            await react.add_reaction(i)

    
    @commands.Cog.listener(name='on_raw_reaction_add')
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):

        message_id = payload.message_id

        if message_id == 825673141279653938:
            if payload.emoji.name == '🎮':
                role = discord.utils.get(discord.utils.get(self.client.guilds, id=payload.guild_id).roles, id=801859621009883186)
                await payload.member.add_roles(role)

            elif payload.emoji.name == '📺':
                role = discord.utils.get(discord.utils.get(self.client.guilds, id=payload.guild_id).roles, id=826410777912410113)
                await payload.member.add_roles(role)
            
            else:
                return


    @commands.Cog.listener(name='on_raw_reaction_remove')
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):

        message_id = payload.message_id

        if message_id == 825673141279653938:
            if payload.emoji.name == '🎮':
                guild = discord.utils.get(self.client.guilds, id=payload.guild_id)
                role = discord.utils.get(guild.roles, id=801859621009883186)
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)
        
            elif payload.emoji.name == '📺':
                guild = discord.utils.get(self.client.guilds, id=payload.guild_id)
                role = discord.utils.get(guild.roles, id=826410777912410113)
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)
            
            else:
                return


def setup(client):
    client.add_cog(RoleCog(client))
