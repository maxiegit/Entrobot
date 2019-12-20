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

extentions = ['cmd', 'moderation']
limst = ['periodt', 'pyramidt', 'placenta', 'peepeeit', 'communism', 'pussy']

@bot.event
async def on_ready():
    print(
        f'{bot.user} has connected\n'
        '-------------------------------------------------------'    )

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

    if message.content == "and thats on what?":
        await message.channel.send(random.choice(limst))
        
    await bot.process_commands(message)

if __name__ == "__main__":
        for extention in extentions:
            try:
                bot.load_extension(extention)
            except Exception as error:
                print("oopsy whoopsy i made a fucky wucky!! {} failed to woad owo [{}]".format(extention, error))
        bot.run(token)