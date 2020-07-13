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
        global client
        client = pyxivapi.XIVAPIClient( 
            session=aiohttp.ClientSession(), 
            api_key="c043b7f2b76c40a8b709aa41f9bdf013fa4aea2b66474698b9a7adec941ec142"
        )

    @commands.command()
    async def item(self, ctx, ID):
        item = await client.index_by_id(
            index="Item",
            content_id=ID,
            columns=["Name", "Description"]
        )   
        embed=discord.Embed(title=item["Name"], description=item["Description"], color=0xff36f8)
        await ctx.send(embed=embed)

    @commands.command()
    async def char(self, ctx, world, forename, surname):
        #search by name does not return as much data as ID
        #so when searching by name, we get the ID and preform a second search
        char_name = await client.character_search(
            world=world,
            forename=forename,
            surname=surname
        )

        charID=char_name["Results"][0]["ID"]
        char = await client.character_by_id(
            lodestone_id=charID,
            include_classjobs=True
         )

        char = json.dumps(char, indent=4)
        loaded_char = json.loads(char)

        embed=discord.Embed(title=loaded_char["Character"]["Name"], description=loaded_char["Character"]["ActiveClassJob"]["UnlockedState"]["Name"])
        embed.set_thumbnail(url=loaded_char["Character"]["Avatar"])
        embed.add_field(name="Server", value=loaded_char["Character"]["Server"], inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FFXIV(bot))