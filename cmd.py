import cogs
import discord
import random
from discord.ext import commands


class Cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def gay(self, ctx):
        await ctx.send("%s is %s%% gay!"%(ctx.author.mention, random.choice(range(1, 102))))
        
    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("test")

    @commands.command(name="piss")
    async def piss(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/602966702191280139/617107230269112331/PISS.gif")
    
    @commands.command(name="mikufancam")
    async def mikucam(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=KNrdGx69pCo")


def setup(bot):
    bot.add_cog(Cmd(bot))