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
        self.status_sonorr = 0
        self.status_lise = 0
        self.is_live.start()
        print('========== loop is starting ==========')


    @tasks.loop(minutes=1.0)
    async def is_live(self):
        request_link = self.get_live('link1183_')
        request_jeez = self.get_live('jeezheus')
        request_shep = self.get_live('shepardeon')
        request_gen = self.get_live('genesis__z')
        request_sonorr = self.get_live('sonorr')
        request_lise = self.get_live('lise_g')
        self.main_channel = self.client.get_channel(733001167763669012)
        self.other_channel = self.client.get_channel(786543165444063274)
        self.is_sent_link = self.config['message_sent']['link']
        self.is_sent_gen = self.config['message_sent']['gen']
        self.is_sent_jeez = self.config['message_sent']['jeez']
        self.is_sent_shep = self.config['message_sent']['shep']

        #========================================
        if request_link == None:
            self.status_link = 0

        else:
            title = request_link["title"]
            display_name = request_link["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&801859621009883186>'

            if self.main_channel is None:
                print('dev channel not found')
                return
        
            if self.status_link == 1:
                return

            await self.main_channel.send(message)
            print('Successfully sent message')
            self.status_link = 1
        
        #========================================
        if request_gen == None:
            self.status_gen = 0

        else:
            title = request_gen["title"]
            display_name = request_gen["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&826410777912410113>'

            if self.other_channel is None:
                print('dev channel not found')
                return
        
            if self.status_gen == 1:
                return

            await self.other_channel.send(message)
            print('Successfully sent message')
            self.status_gen = 1
        
        #========================================
        if request_jeez == None:
            self.status_jeez = 0

        else:
            title = request_jeez["title"]
            display_name = request_jeez["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&826410777912410113>'

            if self.other_channel is None:
                print('dev channel not found')
                return
        
            if self.status_jeez == 1:
                return

            await self.other_channel.send(message)
            print('Successfully sent message')
            self.status_jeez = 1

        #========================================
        if request_shep == None:
            self.status_shep = 0

        else:    
            title = request_shep["title"]
            display_name = request_shep["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&826410777912410113>'

            if self.other_channel is None:
                print('dev channel not found')
                return
        
            if self.status_shep == 1:
                return

            await self.other_channel.send(message)
            print('Successfully sent message')
            self.status_shep = 1

        #========================================
        if request_sonorr == None:
            self.status_sonorr = 0

        else:    
            title = request_sonorr["title"]
            display_name = request_sonorr["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&826410777912410113>'

            if self.other_channel is None:
                print('dev channel not found')
                return
        
            if self.status_sonorr == 1:
                return

            await self.other_channel.send(message)
            print('Successfully sent message')
            self.status_sonorr = 1

        #========================================
        if request_lise == None:
            self.status_lise = 0

        else:    
            title = request_lise["title"]
            display_name = request_lise["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&826410777912410113>'

            if self.other_channel is None:
                print('dev channel not found')
                return
        
            if self.status_lise == 1:
                return

            await self.other_channel.send(message)
            print('Successfully sent message')
            self.status_lise = 1

    
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
            if streamer == 'Sonorrr':
                self.status_sonorr = 1
                return
            if streamer == 'lise_g':
                self.status_lise = 1
                return


        return r

        
    @commands.command()
    async def status(self, ctx):
        await ctx.send(f'{self.status_link} for link')
        await ctx.send(f'{self.status_shep} for shep')
        await ctx.send(f'{self.status_jeez} for jeez')
        await ctx.send(f'{self.status_gen} for genesis')
        await ctx.send(f'{self.status_sonorr} for sonorr')
        await ctx.send(f'{self.status_lise} for lise')
    

def setup(client):
    client.add_cog(TwitchCog(client))

