import discord
from discord.ext import commands

TOKEN = 'NTE2MDgzMDkyMDUwNTQyNjAx.DtvO8Q.ONcpXUa5Jj6_8-IFip_fztMkDIY'

client = commands.Bot(command_prefix = "]")

players = {}


@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name='with Humans'))
    print('Bot is ready ^.^')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{} deleted this: {}\nNice try BAKA :P'.format(author, content))

@client.command()
async def hacked(*args):
    for word in args:
        if word.lower() ==  "navid":
            await client.say("You have just been hacked XD")

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def banish(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context = True)
async def prank(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player("https://www.youtube.com/watch?v=jD3c0RwF55c")
    players[server.id] = player
    player.start()

client.run(TOKEN)
