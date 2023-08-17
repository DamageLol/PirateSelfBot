#Notes For Ideas On Selfbot.
# - Add Different Pages For Each Type Of Commands

#discord-self.py
#discord-self-embed.py

#pip install discord-self
#pip install bs4
#pip install requests



import discord
from discord.ext import commands
import os
import discord_self_embed
import string
import random
import colorama
from colorama import Fore
import requests
import bs4
import aiohttp


colorama.init()

with open('token.txt', 'r') as f:
    token=f.read().strip()

selfbotprefix = ('.')
bot = commands.Bot(command_prefix=selfbotprefix, self_bot=True)


@bot.event #on ready command, runs when the python file is first ran
async def on_ready():
    print('')
    print('')
    print(f'''{Fore.RESET}                 
    {Fore.LIGHTBLACK_EX}                           ╔═════════════════════════════════════════╗                 
    {Fore.LIGHTBLACK_EX}                           ║ {Fore.LIGHTCYAN_EX}╔═╗╦╦═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗ {Fore.LIGHTBLACK_EX}║
    {Fore.LIGHTBLACK_EX}                           ║ {Fore.WHITE}╠═╝║╠╦╝╠═╣ ║ ║╣   ╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║  {Fore.LIGHTBLACK_EX}║
    {Fore.LIGHTBLACK_EX}                           ║ {Fore.LIGHTCYAN_EX}╩  ╩╩╚═╩ ╩ ╩ ╚═╝  ╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩  {Fore.LIGHTBLACK_EX}║
    {Fore.LIGHTBLACK_EX}                           ╚═════════════════════════════════════════╝
    {Fore.WHITE}
    {Fore.WHITE}                                   Logged In As:{Fore.LIGHTCYAN_EX} {bot.user.name}
    {Fore.WHITE}                                   Account ID:{Fore.LIGHTCYAN_EX}   {bot.user.id}
    {Fore.WHITE}                                   Currently In: {Fore.LIGHTCYAN_EX}{len(list(bot.guilds))} Discord Servers
    {Fore.WHITE}                                   Selfbot Prefix: {Fore.LIGHTCYAN_EX}{selfbotprefix}
    ''' + Fore.RESET)

########################################
@bot.command() #main loop
async def mainmenu(ctx):
    await ctx.message.edit('```Pirate SelfBot Beta - Damage\n\nMain\nServer\nUser\nFun```')

@bot.command()
async def main(ctx):
    await ctx.message.edit('```Pirate Selfbot Main Settings\n\nSendMessage - .sendmessage @user\nUserPFP - .userprofile @user\nGetUserStatus - .getuserstatus @user```')

@bot.command()
async def server(ctx):
    await ctx.message.edit('```Pirate Selfbot Server Settings\n\nCreateChannel - createchannel (name)\nCreateRole - createrole (name)```')

@bot.command()
async def fun(ctx):
    await ctx.message.edit('```Pirate Selfbot Server Settings\n\n```')

#######################################

@bot.command()#creates a role in your discord server and you can have customized roles
async def createrole(ctx, role):
    role = await ctx.guild.create_role(name=role)
    print(f'''{Fore.RESET} 
{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}#{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} Role Created ({role}) 
 ''' + Fore.RESET)
    

@bot.command() #creates a channel in your discord server and you can have customized names
async def createchannel(ctx, channel):
    channel = await ctx.guild.create_text_channel(channel)
    print(f'''{Fore.RESET} 
{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}#{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} Channel Created ({channel}) ''' + Fore.RESET)

@bot.command() #sends a message to a user.
async def sendmessage(ctx, user: discord.Member, *, message):
 await user.send(message) 
 print(f'''{Fore.RESET} 
{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}#{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} Sent Message ({message}) To ({user}) ''' + Fore.RESET)


@bot.command() #gets the users userprofile
async def userprofile(ctx, user: discord.Member):
    avatar_url = user.avatar.url
    await ctx.message.edit(avatar_url)
    print(f'''{Fore.RESET} 
{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}#{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} Got {user} Avatar Picture ''' + Fore.RESET)

@bot.command() #gets a discord users staus by pinging the web application post request status
async def getuserstatus(ctx, user: discord.Member):
    userstatus = user.web_status
    await ctx.message.edit(userstatus)
    print(f'''{Fore.RESET} 
{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}#{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} Got {user} Status Information''' + Fore.RESET)


bot.run(token) #runs the token to login to the discord using token authorization