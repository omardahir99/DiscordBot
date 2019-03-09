import discord
from discord.ext import commands
import platform
from random import randint
import youtube_dl


class Youtube_Player:
    
    def __init__(self, client):
        self.client = client

    
    @client.command(pass_context=True)
    async def play(ctx, url):
        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel
        if channel:
            if not client.is_voice_connected(server):
                await client.join_voice_channel(channel)
            elif client.voice_client_in(server).channel != channel:
                await client.voice_client_in(server).disconnect()
                await client.join_voice_channel(channel)
            voice_client = client.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()
        else:
            await client.send_message(ctx.message.channel, "You aren't in a voice channel")
    
    @client.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
    
def setup(client):
    client.add_cog(Server_Comamands(client))
