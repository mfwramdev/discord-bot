import time
import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from utils import default


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self.process = psutil.Process(os.getpid())

    @commands.command(aliases=["qna"],hidden=True)
    async def emb(self,ctx,title,desc="embed karta hai bas"):
        await ctx.message.delete()
        embed = discord.Embed(
                title = title,
                description=desc,
                colour = discord.Colour.blue())
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Information(bot))
