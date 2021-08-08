# made by : https://github.com/jubnl

import json
from pathlib import Path



def get_config():
    """retourne la config, ne prends pas de paramètres"""

    # Set le path pour la config
    mod_path = Path(__file__).parent
    relative_path_2 = '../../assets/config/config_bot.json'
    config_bot_json = (mod_path / relative_path_2).resolve()

    # Ouvre le fichier et le met dans une var (referme le fichier tout seul)
    with open(config_bot_json,'r') as js_config:
        config = json.load(js_config)

    # Retourne la config
    return config
