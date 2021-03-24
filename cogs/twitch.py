from discord.ext import commands, tasks
import requests
from cogs.utils.utilitiesBot import get_config
from discord.utils import get


class TwitchCog(commands.Cog, name='auto live message'):

    def __init__(self, client):
        self.client = client
        channel = self.client.get_channel(823957275151564810)
        self.config = get_config()
        self.is_live.start()
    

    @tasks.loop(minutes=60.0)
    async def is_live(self):
        URL = 'https://api.twitch.tv/helix/streams?user_login=link1183_'
        auth_URL = 'https://id.twitch.tv/oauth2/token'
        client_ID = self.config["twitch_id"]
        secret  = self.config["twitch_secret"]

        aut_params = {'client_id': client_ID,
             'client_secret': secret,
             'grant_type': 'client_credentials'
        }


        aut_call = requests.post(url=auth_URL, params=aut_params) 
        access_token = aut_call.json()['access_token']

        head = {
            'Client-ID' : client_ID,
            'Authorization' :  "Bearer " + access_token
        }

        r = requests.get(URL, headers=head).json()['data']
        channel = self.client.get_channel(823957275151564810)
        print(channel)
        await channel.send(r)
    

def setup(client):
    client.add_cog(TwitchCog(client))

