from discord.ext import commands, tasks
import requests
from cogs.utils.utilitiesBot import get_config
from discord.utils import get


class TwitchCog(commands.Cog, name='auto live message'):

    def __init__(self, client):
        self.client = client
        self.config = get_config()
        # self.is_live.start()
    

    @tasks.loop(seconds=10.0)
    async def is_live(self):
        URL = 'https://api.twitch.tv/helix/streams?user_login=link1183_'
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

        r = requests.get(URL, headers=head).json()['data'][0]
        channel = self.client.get_channel(823957275151564810)
        await channel.send(r)

        if r == '[]' or r.status_code == 200:
            return
        
        if channel is None:
            return
        
        title = r["title"]
        game_id = r["game_id"]

        

    @commands.command()
    async def ttv(self, ctx):
        URL = 'https://api.twitch.tv/helix/streams?user_login=link1183_'
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

        r = requests.get(URL, headers=head).json()['data']
        channel = self.client.get_channel(823957275151564810)

        datas = [
        {
            "broadcaster_language": "en",
            "display_name": "a_seagull",
            "game_id": "506442",
            "id": "19070311",
            "is_live": True,
            "tags_ids": [
                "6ea6bca4-4712-4ab9-a906-e3336a9d8039"
            ],
            "thumbnail_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/a_seagull-profile_image-4d2d235688c7dc66-300x300.png",
            "title": "a_seagull",
            "started_at": "2020-03-18T17:56:00Z"
        }]
    

def setup(client):
    client.add_cog(TwitchCog(client))

