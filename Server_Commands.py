import discord
from discord.ext import commands
import platform
from random import randint



class Server_Commands:
    
    def __init__(self, client):
        self.client = client

    @client.event
    async def on_server_join(server):
        await client.send_message(ctx.message.channel, "K-konichiwa I'm a new transfer students >_<")

    @client.event
    async def on_member_join(member):
    roles = member.server.role_hierarchy
    if member.top_role == member.server.default_role:
        if len(roles) > 1:
            i = -2
            loop = True
            while loop and i != -1*len(roles):
                if roles[i].managed:
                    mem_roles = member.roles.append(roles[i])
                    await client.add_roles(member, *mem_roles)
                    loop = False
                i -= 1

    @client.command(pass_context = True)
    async def user(ctx, member:discord.User = None):
        try:
            if member == None:
                member = ctx.message.author
            join = member.joined_at
            role = member.top_role
            emb = discord.Embed(title = str(member), description = "Info on {}".format(member.mention), color=0xff0006)
            emb.set_thumbnail(url = member.avatar_url)
            emb.add_field(name="Name", value = member)
            emb.add_field(name="Role", value = role)
            emb.add_field(name="Joined", value = join)
            await client.send_message(ctx.message.channel, embed=emb)
        except Exception as e:
            await client.send_message(ctx.message.channel, "Please @ a specific HUMAN user")
            print(e)

    @client.command(pass_context = True)
    async def banlist(ctx):
        bans = client.get_bans(ctx.message.server)
        ban_list = "\n".join(bans)
        emb = discord.Embed(title = "People who GTAB", description = ban_list)
        await client.send_message(ctx.message.channel, embed = emb)


    @client.command(pass_context = True)
    async def perms(ctx, role:discord.Role = None):
        try:
            if role == None:
                role = ctx.message.channel.server.default_role
            emb = discord.Embed(title = str(role.name), description = "Permissions of {}".format(role.name), color=role.color)
            perms = permission_handler(role.permissions)
            emb.add_field(name="Permissions", value=perms)
            await client.send_message(ctx.message.channel, embed=emb)
        except Exception as e:
            await client.send_message(ctx.message.channel, "Please @ a specific role")
            print(e)

    
    def permission_handler(perms):
        ret = ""
        ret += "Kick Members: " + str(perms.kick_members) + "\n"
        ret += "Ban Members: " + str(perms.ban_members) + "\n"
        ret += "Manage Channels: " + str(perms.manage_server) + "\n"
        ret += "Mute Members: " + str(perms.mute_members) + "\n"
        ret += "Deafen Members: " + str(perms.deafen_members) + "\n"
        ret += "Move Members: " + str(perms.move_members) + "\n"
        ret += "Manage Roles: " + str(perms.manage_roles)
        return ret
    
    @client.command(pass_context = True)
    async def membercount(ctx):
        emb = discord.Embed(title = str(ctx.message.channel.server), description = "There are: {} members".format(ctx.message.channel.server.member_count), color=0x0ba9f4)
        emb.set_thumbnail(url =ctx.message.channel.server.icon_url)
        await client.send_message(ctx.message.channel, embed=emb)


def setup(client):
    client.add_cog(Server_Comamands(client))
