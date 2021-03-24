import discord
from discord.ext import commands, tasks

import requests


class TwitchCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.is_live.start()
    

    @tasks.loop(minutes=5)
    async def is_live(self):
        URL = 'https://api.twitch.tv/helix/streams?user_login=link1183_'
        auth_URL = 'https://id.twitch.tv/oauth2/token'
        client_ID = 'r2jeo5utf9epj2xr85w7how2gw4ey2'
        secret  = '1kxrnxpzhyki2v293opfshrg1n7btt'

        aut_params = {'client_id': client_ID,
             'client_secret': secret,
             'grant_type': 'client_credentials'
        }



        AutCall = requests.post(url=auth_URL, params=aut_params) 
        access_token = AutCall.json()['access_token']

        head = {
            'Client-ID' : client_ID,
            'Authorization' :  "Bearer " + access_token
        }

        r = requests.get(URL, headers = head).json()['data']
        channel = self.client.get_channel(823957275151564810)
        await channel.send(r)


    @commands.command()
    async def ttv(self, ctx):
        await ctx.send('test')
    

def setup(client):
    client.add_cog(TwitchCog(client))

