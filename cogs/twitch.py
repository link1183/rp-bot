from discord.ext import commands, tasks
import requests
from cogs.utils.utilitiesBot import get_config
from discord.utils import get
from discord_slash import SlashContext, cog_ext


class TwitchCog(commands.Cog, name='auto live message'):

    def __init__(self, client):
        self.client = client
        self.config = get_config()
        self.status = 0
        self.is_live.start()
        print('========== loop is starting ==========')


    @tasks.loop(minutes=1.0)
    async def is_live(self):
        request = self.get_live('link1183_')
        self.main_channel = self.client.get_channel(733001167763669012)
        self.is_sent = self.config['message_sent']['link']

        #========================================
        if request == None:
            self.status = 0

        else:
            title = request["title"]
            display_name = request["user_name"]

            message = f':tv: **{display_name}** is now live on Twitch! :tv:\nHe is streaming **{title}** at https://twitch.tv/{display_name} <@&801859621009883186>'

            if self.main_channel is None:
                print('dev channel not found')
                return
        
            if self.status == 1:
                return

            await self.main_channel.send(message)
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
                self.status = 0
                return

        return r
    

def setup(client):
    client.add_cog(TwitchCog(client))

