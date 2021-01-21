# made by : https://github.com/jubnl

from discord.ext import commands
import json
from pathlib import Path



def get_config():
    """retourne la config, ne prends pas de paramètres"""

    # set le path pour la config
    mod_path = Path(__file__).parent
    relative_path_2 = '../../assets/config/config_bot.json'
    config_bot_json = (mod_path / relative_path_2).resolve()

    # ouvre le fichier et le met dans une var (referme le fichier tout seul)
    with open(config_bot_json,'r') as js_config:
        config = json.load(js_config)

    #retourne la config
    return config


def get_client():
    """Retourne le client, ne prends pas de paramètres"""

    # obtient la config
    config = get_config()

    # set le client
    client = commands.Bot(command_prefix=config['prefix'])

    #retourne le client
    return client
