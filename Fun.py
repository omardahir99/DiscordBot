import discord
from discord.ext import commands
import platform
from random import randint



class Fun:
    def __init__(self, client):
        self.client = client

    @client.command(pass_context = True)
    async def bother(ctx, member:discord.User = None):
        if member != None:
            if member not in bothers:
                bothers.append(member)
                await client.send_message(ctx.message.channel, "I am now bothering {} anymore".format(member))
            else:
                bothers.remove(member)
                await client.send_message(ctx.message.channel, "I am not bothering {} anymore".format(member))

    @client.command(pass_context = True)
    async def eightball(ctx):
        answers = ["It is certain.", "Outlook good.", "Signs point to yes.", "Yuh.",
                   "Ask again later.", "Concentrate and ask again.", "Hol up.",
                   "Don't count on it.", "Outlook not so good.", "My reply is no.", "Nah."]
        num = randint(0,10)
        if num <= 10 and num >= 7:
            emb = discord.Embed(color=0xff0006)
        elif num <= 6 and num >= 4:
            emb = discord.Embed(color=0xffff00)
        elif num <= 3:
            emb = discord.Embed(color=0x00f400)
        emb.add_field(name = answers[num], value = "lol")
        await client.send_message(ctx.message.channel, embed=emb)

    @client.command(pass_context = True)
    async def coinflip(ctx):
        num = randint(1,1000)
        if num >= 500:
            text = "Heads"
        else:
            text = "Tails"
        await client.send_message(ctx.message.channel, text)

def setup(client):
    client.add_cog(Server_Comamands(client))
