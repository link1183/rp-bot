# made by : https://github.com/jubnl

from discord.ext import commands



class PurgeCog(commands.Cog, name="Commande !purge"):

    def __init__(self, client):
        self.client = client


    @commands.cooldown(1,10)
    @commands.command(pass_context=True, name='purge', aliases=['purgemessages'], no_pm=True,description="(nb de messages) :\nPurge le nombre de messages specifiés")
    @commands.has_role('DevBot')
    async def ppurge(self,ctx,number=None):
        ctx.message.delete()
        if number == None:
            number = 1
        number = int(number)
        if number > 150 or number < 1:
            await ctx.send("I can only delete messages in a range from 1 to 150 messages", delete_after=10)
        else:
            mgs = []
            number = int(number)
            channel = ctx.message.channel
            async for x in channel.history(limit=int(number)):
                mgs.append(x)
            
            await ctx.channel.purge(limit=len(mgs))
            await ctx.send('Success!', delete_after=3)

def setup(client):
    client.add_cog(PurgeCog(client))