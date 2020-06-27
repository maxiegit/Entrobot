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

    @commands.command(name="bonk")
    async def bonk(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/611577151623528449/660896781919322125/bonk.mp4")
        
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        if avamember:
            userAvatarUrl = avamember.avatar_url
            embed=discord.Embed()
            embed.set_image(url=userAvatarUrl)
            embed.set_footer(text="You look so pretty~~")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Unable to get avatar", description="Command example")
            embed.add_field(name=" ", value=" !avatar @USER", inline=True)
            embed.set_thumbnail(url=embed.author.icon_url)
            await ctx.send(embed=embed)    

    # @commands.command(name="setcolor")
    # async def setcolor(self, ctx, arg):
    #     author = ctx.message.author
    #     await self.bot.create_role(author.server, name="arg", colour=discord.Colour(arg))

    #     user = ctx.message.author
    #     role = discord.utils.get(user.server.roles, name=arg)
    #     await self.bot.add_roles(user, role)

def setup(bot):
    bot.add_cog(Cmd(bot))
