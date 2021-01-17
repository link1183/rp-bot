from discord.ext import commands

dices_results = {
    "green": ['test1', 'test2'],
    "yellow": ['test3', 'test4'],
    "purple": ['test5', 'test6'],
    "red": ['test7', 'test8'],
    "white": ['test9', 'test10']
}


def get_client():
    """Retourne le client, ne prends pas de paramètres"""

    # set le client
    client = commands.Bot(command_prefix='+')

    #retourne le client
    return client
