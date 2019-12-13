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
        f'{bot.user} has connected to discord\n'
        '-------------------------------------------------------'    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "hatsune miku":
        await message.channel.send("hatsune miku")

    if message.content == "me":
        await message.channel.send("pussy")

@bot.command(name="gay")
async def gay(ctx):
    num = random.choice(range(1, 102))
    await ctx.send("%s is %s%% gay!"%(ctx.author.mention, num))

@bot.command(name="test")
async def test(ctx):
    await ctx.send("test")

@bot.command(name="piss")
async def piss(ctx):
    await ctx.send("https://media.discordapp.net/attachments/602966702191280139/617107230269112331/PISS.gif")
    
@bot.command(name="mikufancam")
async def mikucam(ctx):
    await ctx.send("https://www.youtube.com/watch?v=KNrdGx69pCo")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "hatsune miku":
        await message.channel.send("hatsune miku")

    if message.content == "me":
        await message.channel.send("pussy")

    if message.content == "straight pride":
        await message.channel.send("straight pride?? HAHAHAHAHA")
        
    await bot.process_commands(message)

@bot.command(name="cmd")
async def cmd(ctx):
    embed=discord.Embed(title="Commands", color=0xbf75ec)
    embed.add_field(name="!piss", value="Posts piss.gif", inline=True)
    embed.add_field(name="!gay", value="tells you how gay you are", inline=True)
    await ctx.send(embed=embed)

bot.run(token)