# bot.py
import os
import random
import discord
from dotenv import load_dotenv

from discord.ext import commands
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(
        f'{bot.user} has connected to discord'
    )

@bot.command(name="gay")
async def gay(ctx):
    num = random.choice(range(1, 102))
    await ctx.send("%s is %s%% gay!"%(ctx.author.mention, num))

@bot.command(name="test")
async def test(ctx):
    await ctx.send("shut up f*g")
    
bot.run(token)