import cogs
import discord
import random
from urllib.request import urlopen
import pyxivapi
import asyncio
import aiohttp
import json
from discord.ext import commands

class FFXIV(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def item(self, ctx, ID):
        client = pyxivapi.XIVAPIClient( 
            session=aiohttp.ClientSession(), 
            api_key="c043b7f2b76c40a8b709aa41f9bdf013fa4aea2b66474698b9a7adec941ec142"
        )

        item = await client.index_by_id(
            index="Item",
            content_id=ID,
            columns=["Name"]
        )   
        await ctx.send(item["Name"]+"\n"+ID) 


def setup(bot):
    bot.add_cog(FFXIV(bot))