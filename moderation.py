import cogs
import discord
import random
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def cmd(self, ctx):
        embed=discord.Embed(title=" ", color=0xa985f9)
        embed.set_author(name="Comamnds")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/654614324509409300.png?v=1")
        embed.add_field(name="!piss", value="Posts piss.gif", inline=False)
        embed.add_field(name="!gay", value="Tells you how gay you are", inline=False)
        embed.add_field(name="!mikufancam", value="Miku Fan Cam", inline=False)
        embed.set_footer(text="Use !noncmd for non command responses!")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
