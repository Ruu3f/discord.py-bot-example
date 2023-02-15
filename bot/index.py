#imports
import os
os.system("pip install -r requirements.txt") #install packages, a requirements file is required
import discord
from discord.ext import commands
from colorama import Fore #colors for text (opt)

intents = discord.Intents.all() #you can change intents as per your usage, on default i've enabled every intent
bot = commands.Bot(command_prefix = "!", intents = intents) #you can change prefix to anything here if you dont want the ! prefix

@bot.event
async def on_ready():
	print(f"{Fore.GREEN} {bot.user.name} is ready!") #the message it shows when the bot is ready
	await bot.change_presence(status = discord.Status.online, #set the bots status, can be dnd, online or idle.
              activity = discord.Activity(type = discord.ActivityType.watching, #you can set watching to something else like playing, listening, etc.
              name = "change this in index.py")) #change the status message of the bot

bot.load_extension("cog") #load cogs (you can load multiple by copy pasting this line again and put the name of the cog without .py)

bot.run("TOKEN") #your bots token
