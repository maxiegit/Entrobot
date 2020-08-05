import cogs
import discord
import random
from discord.ext import commands
from discord import Embed
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO

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

    @commands.command(name="ramalama")
    async def ramalama(self, ctx):
        await ctx.send("We go together\nLike rama lama lama ka dinga da dinga dong\nRemembered forever\nAs shoo-bop sha wadda wadda yippity boom de boom\nChang chang changitty chang sha-bop\nThat\'s the way it should be\nWah-oooh, yeah!\nWe\'re one of a kind\nLike dip da-dip da-dip doo-wop da doo-bee doo\nOur names are signed\nBoogedy boogedy boogedy boogedy\nShooby doo-wop she-bop\nChang chang changitty chang sha-bop\nWe'll always be like one, wa-wa-wa-one\nWhen we go out at night\nAnd stars are shinin' bright\nUp in the skies above\nOr at the high school dance\nWhere you can find romance\nMaybe it might be love\nRama lama lama ka dinga da dinga dong\nShoo-bop sha wadda wadda yippity boom de boom\nChang chang changitty chang sha-bop\nDip da-dip da-dip doo-wop da doo-bee doo\nBoogedy boogedy boogedy boogedy\nShoo-be doo-wop she-bop\nSha-na-na-na-na-na-na-na yippity dip de doom\nRama lama lama ka dinga da dinga dong\nShoo-bop sha wadda wadda yippity boom de boom\nChang chang changitty chang sha-bop\nDip da-dip da-dip doo-wop da doo-bee doo\nBoogedy boogedy boogedy boogedy\nShoo-be doo-wop she-bop\nSha-na-na-na-na-na-na-na yippity dip de doom\nWop ba-ba lu-mop and wop bam boom!\nWe're for each other\nLike a wop ba-ba lu-bop and wop bam boom\nJust like my brother is\nSha-na-na-na-na-na-na-na yippity dip de doom\nChang chang chanitty chang sha-bop\nWe'll always be together\nWha oooh, yeah!\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together\nWe'll always be together")
        
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member):
        if avamember:
            userAvatarUrl = avamember.avatar_url
            embed=discord.Embed()
            embed.set_image(url=userAvatarUrl)
            embed.set_footer(text="You look so pretty~~")
            await ctx.send(embed=embed)    

    @commands.command()
    async def version(self, ctx):
        f = open("files/version.txt", "r")
        embed=discord.Embed(title="Running version " + f.read(), color=0x70de52)
        embed.set_author(name="Version", url=discord.Embed.Empty, icon_url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Cmd(bot))
