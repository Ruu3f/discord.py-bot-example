#note: this works but this is just a simple example of response
import discord
from discord.ext import commands

class cog(commands.Cog): #this is the class
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="ping", description="get a response.") #name="ping" is the name of the command, description"get a response" is the description/help of a command
    async def ping(self, ctx):
        with open("data/config.json", "r") as f: #opening the config.json file
            config = json.load(f) #loading config.json to extract values from it
            msg = config["msg"] #msg value extracted from config.json
        start_time = time.time()
        embed = discord.Embed(description=f"Pong!\nMSG={msg}", color=0x69696) #you can change the color using hex codes
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(cog(bot)) #choose any name you want just keep it same as the class name
