import requests


url = "https://discord.com/api/v8/applications/771496017568858124/guilds/733000706088501309/commands"

json = {
    "name": "status",
    "description": "Sends the status of the streaming message",
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot NzcxNDk2MDE3NTY4ODU4MTI0.X5s9qA.-FMfeXawmYO-LuG6BZ8cDM3ERuY"
}

r = requests.post(url, headers=headers, json=json)