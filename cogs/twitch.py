from discord.ext import commands, tasks
import requests
from cogs.utils.utilitiesBot import get_config
from discord.utils import get
from discord import Embed, Color
from datetime import datetime


class TwitchCog(commands.Cog, name='auto live message'):

    def __init__(self, client):
        self.client = client
        self.config = get_config()
        self.status_link = 0
        self.status_shep = 0
        self.status_gen = 0
        self.status_jeez = 0
        self.is_live_link.start()
        self.is_live_shep.start()
        self.is_live_gen.start()
        self.is_live_jeez.start()
        print('========== loop is starting ==========')


    @tasks.loop(minutes=1.0)
    async def is_live_link(self):
        request = self.get_live('link1183_')

        if request == None:
            self.status = 0
            return
                
        title = request["title"]
        display_name = request["user_name"]

        message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&801859621009883186>'

        channel = self.client.get_channel(733001167763669012)

        if channel is None:
            print('dev channel not found')
            return
        
        if self.status == 1:
            return

        await channel.send(message)
        print('Successfully sent message')
        self.status = 1

    
    def get_live(self, streamer):
        URL = f'https://api.twitch.tv/helix/streams?user_login={streamer}'
        auth_URL = 'https://id.twitch.tv/oauth2/token'
        client_ID = self.config["twitch_id"]
        secret  = self.config["twitch_secret"]

        aut_params = {'client_id': client_ID,
             'client_secret': secret,
             'grant_type': 'client_credentials'
        }


        auth_call = requests.post(url=auth_URL, params=aut_params) 
        access_token = auth_call.json()['access_token']

        head = {
            'Client-ID' : client_ID,
            'Authorization' :  "Bearer " + access_token
        }

        try:
            r = requests.get(URL, headers=head).json()['data'][0]
        except IndexError:
            return

        if r == []:
            if streamer == 'link1183_':
                self.status_link = 0
                return
            if streamer == 'genesis__z':
                self.status_gen = 0
                return
            if streamer == 'rnjeez':
                self.status_jeez = 0
                return
            if streamer == 'shepardeon':
                self.status_shep = 0
                return

        return r

    
    @tasks.loop(minutes=1.5)
    async def is_live_shep(self):
        request = self.get_live('shepardeon')

        if request == None:
            self.status_shep = 0
            return
                
        title = request["title"]
        display_name = request["user_name"]

        message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name}'

        channel = self.client.get_channel(786543165444063274)

        if channel is None:
            print('dev channel not found')
            return
        
        if self.status_shep == 1:
            return

        await channel.send(message)
        print('Successfully sent message')
        self.status_shep = 1


    @tasks.loop(minutes=1.5)
    async def is_live_gen(self):
        request = self.get_live('genesis__z')

        if request == None:
            self.status_gen = 0
            return
                
        title = request["title"]
        display_name = request["user_name"]

        message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name}'

        channel = self.client.get_channel(786543165444063274)

        if channel is None:
            print('dev channel not found')
            return
        
        if self.status_gen == 1:
            return

        await channel.send(message)
        print('Successfully sent message')
        self.status_gen = 1


    @tasks.loop(minutes=1.5)
    async def is_live_jeez(self):
        request = self.get_live('rnjeez')

        if request == None:
            self.status_jeez = 0
            return
                
        title = request["title"]
        display_name = request["user_name"]

        message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name}'

        channel = self.client.get_channel(786543165444063274)

        if channel is None:
            print('dev channel not found')
            return
        
        if self.status_jeez == 1:
            return

        await channel.send(message)
        print('Successfully sent message')
        self.status_jeez = 1

        
    @commands.command()
    async def status(self, ctx):
        await ctx.send(self.status)
    

def setup(client):
    client.add_cog(TwitchCog(client))

