import cogs
import discord
import random
from urllib.request import urlopen
import pyxivapi
import asyncio
import aiohttp
import json
import colorsys
import urllib.request
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO


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

    #getting char id could probably be seperated into its own function
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

    @commands.command()
    async def classes(self, ctx, world, forename, surname, role=""):
        async with ctx.typing():
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
            
            #uses the role variable to determine where to start and end in the loop
            #so as to only return the relevent classes within the role

            if role=="":
                start=0
                end=18
                colour=0xffffff
            elif role=="tank":
                start=0
                end=4
                colour=0x149dff
            elif role=="melee":
                start=4
                end=8
                colour=0xdb0d3d
            elif role=="healer":
                start=8
                end=11
                colour=0x1bd13d
            elif role=="ranged":
                start=11
                end=14
                colour=0xf0ce11
            elif role=="magical":
                start=14
                end=18
                colour=0xa944e3
            else:
                raise Exception("Hmmmm I dont recognise that role")

            embed=discord.Embed(title=loaded_char["Character"]["Name"], colour=colour)
            embed.set_thumbnail(url=loaded_char["Character"]["Avatar"])
            
            # loops through to make embed fields for classes wanted
            while start < end:
                embed.add_field(name=loaded_char['Character']['ClassJobs'][start]['UnlockedState']['Name'], value=loaded_char['Character']['ClassJobs'][start]['Level'], inline=True)
                start += 1
            
            await ctx.send(embed=embed)
        

    @commands.command()
    async def portrait(self, ctx, world, forename, surname):
        async with ctx.typing():
            char_name = await client.character_search(
                world=world,
                forename=forename,
                surname=surname
            )

            charID=char_name["Results"][0]["ID"]
            char = await client.character_by_id(
                lodestone_id=charID
            )
            
            char = json.dumps(char, indent=4)
            loaded_char = json.loads(char)

            embed=discord.Embed(title=loaded_char["Character"]["Name"])
            embed.set_image(url=loaded_char['Character']['Portrait'])

            await ctx.send(embed=embed)

    @commands.command()
    async def image(self, ctx):
        async with ctx.typing():
            

            char_name = await client.character_search(
            world="Cactuar",
            forename="Lunar",
            surname="Orbit"
            )

            charID=char_name["Results"][0]["ID"]
            char = await client.character_by_id(
                lodestone_id=charID,
                include_classjobs=True
            )

            char = json.dumps(char, indent=4)
            loaded_char = json.loads(char)

            url = loaded_char['Character']['Portrait']
            with urllib.request.urlopen(url) as url:
                f = BytesIO(url.read())

            # w 640 h 873
            portrait = Image.open(f)

            bg = Image.new('RGB', (portrait.size[0] * 2, portrait.size[1]), color = (73, 109, 137))
            print(loaded_char)
            with BytesIO() as image_binary:
                create_image(bg, portrait, str(loaded_char['Character']['ClassJobs'][7]['UnlockedState']['Name']), str(loaded_char['Character']['ClassJobs'][7]['Level'])).save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

def create_image(bg, portrait, name, level):
    draw = ImageDraw.Draw(bg)

    draw.text((740, 75),name,(255,255,255))
    draw.text((740, 85),level,(255,255,255))

    bg.paste(portrait)

    return bg

def setup(bot):
    bot.add_cog(FFXIV(bot))
