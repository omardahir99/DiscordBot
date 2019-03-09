import discord
from discord.ext import commands
import platform
from random import randint
import youtube_dl
import json

client = commands.Bot(command_prefix = "]")
players = {}
extensions = ['Server_Commands', 'Fun', 'Youtube_Player']

with open('strings.json') as json_data:
    data = json.load(json_data)
TOKEN = data[token]

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    await client.change_presence(game = discord.Game(name='with Humans'))
    print('Bot is ready ^.^')

if __name__ == "__main__":
    for ext in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. Error: {}'.format(extension, error))
    client.run(TOKEN)
