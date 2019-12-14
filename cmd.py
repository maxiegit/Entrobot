import cogs
import discord
import random
from discord.ext import commands


class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog()
    async def gay(self, ctx):
        await ctx.send("%s is %s%% gay!"%(ctx.author.mention, random.choice(range(1, 102))))
