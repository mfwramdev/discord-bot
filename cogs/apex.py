import random
import discord
import secrets
import asyncio
import aiohttp
import discord
from io import BytesIO
from discord.ext import commands
from utils import lists, permissions, http, default


class Apex_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()


    @commands.command()
    async def apex(self, ctx):
        """ CORE APEX TEAM """

        embedmsg = discord.Embed(title = "CORE APEX", color = 0xff8100)
        embedmsg.add_field(name = "PRESIDENT: ", value = "HITARTH KHURANA", inline = False)
        embedmsg.add_field(name = "VICE PRESIDENT: ", value = "INESH TICKOO", inline = False)
        embedmsg.add_field(name = "HACKING HEAD: ", value = "TARUSH SONAKYA", inline = False)        
        embedmsg.add_field(name = "PROGRAMMNIG HEAD: ", value = "NEEL LODHA", inline = False)
        embedmsg.add_field(name = "CREATIVE HEAD: ", value = "KARTIKAY SHARMA", inline = False)        
        embedmsg.add_field(name = "QUIZZING HEAD: ", value = "MEHARDEEP KAUR", inline = False)
        embedmsg.add_field(name = "GAMING HEAD: ", value = "VIHAAN SARIN", inline = False)
        embedmsg.add_field(name = "HARDWARE HEAD: ", value = "TEJAS ANAND", inline = False)
        embedmsg.add_field(name = "MEMBERS: ", value = "ANANT CHOUDHARY\nADARSH BHATT\nTARAN CHADHA\nRAHUL RAMDEV\nMANAN\nGAURIKA AGARWAL\nJAI NANDA\nKARMANYA BHALLA\nASHNI AHLAWAT\nAYAAN CHOUDHURY\nARNAV VERMA", inline = False)
        embedmsg.set_thumbnail(url = r'https://cdn.discordapp.com/attachments/613689252232036362/856963616603504660/pp.png')



        await ctx.send(embed = embedmsg)
    
    @commands.command(hidden = True)
    async def updateapex(self, ctx):
        """ CORE APEX TEAM """

        embedmsg = discord.Embed(title = "CORE APEX", color = 0xff8100)
        embedmsg.add_field(name = "PRESIDENT: ", value = "HITARTH KHURANA", inline = False)
        embedmsg.add_field(name = "VICE PRESIDENT: ", value = "INESH TICKOO", inline = False)
        embedmsg.add_field(name = "HACKING HEAD: ", value = "TARUSH SONAKYA", inline = False)        
        embedmsg.add_field(name = "PROGRAMMNIG HEAD: ", value = "NEEL LODHA", inline = False)
        embedmsg.add_field(name = "CREATIVE HEAD: ", value = "KARTIKAY SHARMA", inline = False)        
        embedmsg.add_field(name = "QUIZZING HEAD: ", value = "MEHARDEEP KAUR", inline = False)
        embedmsg.add_field(name = "GAMING HEAD: ", value = "VIHAAN SARIN", inline = False)
        embedmsg.add_field(name = "HARDWARE HEAD: ", value = "TEJAS ANAND", inline = False)
        embedmsg.add_field(name = "MEMBERS: ", value = "ANANT CHOUDHARY\nADARSH BHATT\nTARAN CHADHA\nRAHUL RAMDEV\nMANAN\nGAURIKA AGARWAL\nJAI NANDA\nKARMANYA BHALLA\nASHNI AHLAWAT\nAYAAN CHOUDHURY\nARNAV VERMA", inline = False)
        embedmsg.set_thumbnail(url = r'https://cdn.discordapp.com/attachments/613689252232036362/856963616603504660/pp.png')

        channel = self.bot.get_channel(837752413740990487)
        msg = await channel.fetch_message(857147175645478943)

        await msg.edit(embed = embedmsg)
        await ctx.message.add_reaction(chr(0x1F44D))

def setup(bot):
    bot.add_cog(Apex_Commands(bot))


