import discord
from discord.ext import commands
from psutil import Process

class BotSysCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="ping", description="Get a pong message with response time.") #name="ping" is the name of the command, description"Get a pong message with response time." is the description/help of a command
    async def ping(self, ctx):
        start_time = time.time()
        embed = discord.Embed(description="Pong!", color=0x69696) #you can change the color using hex codes
        response = await ctx.respond(embed=embed)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        embed.description = f"Pong! {duration:.2f}ms."
        await response.edit(embed=embed)

def setup(bot):
    bot.add_cog(cog(bot)) #choose any name you want just keep it same as the class name
