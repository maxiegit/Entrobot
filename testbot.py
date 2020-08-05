# bot.py
import os
import random
import discord
import cogs
from dotenv import load_dotenv

from discord.ext import commands
load_dotenv()
token = os.getenv('TEST_TOKEN')

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')

extentions = [  'cogs.cmd.cmd', 
                'cogs.moderation.moderation',
                'cogs.FFXIV.FFXIV',
                'cogs.error.error'
                ]
                
@bot.event
async def on_ready():
    print(
        f'{bot.user} has connected\n'
        '-------------------------------------------------------'    )

if __name__ == "__main__":
        for extention in extentions:
            try:
                bot.load_extension(extention)
            except Exception as error:
                print("oopsy whoopsy i made a fucky wucky!! {} failed to woad owo [{}]".format(extention, error))
        bot.run(token)