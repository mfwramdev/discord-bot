import random
import discord
import secrets
import asyncio
import aiohttp

from io import BytesIO
from discord.ext import commands
from utils import lists, permissions, http, default


class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates what you desire """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.reply(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")

    @commands.command(aliases=["noticemesenpai"])
    async def noticeme(self, ctx):
        """ Notice me senpai! owo """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = BytesIO(await http.get("https://i.alexflipnote.dev/500ce4.gif", res_method="read"))
        await ctx.send(file=discord.File(bio, filename="noticeme.gif"))

    @commands.command(hidden='True')
    async def ramdi(self, ctx, *, thing: commands.clean_content):
        ramdi_amount = random.uniform(0.0, 100.0)
        if 'rahul' in thing.lower():
            await ctx.reply("100% ramdi no doubt")
            return
        await ctx.reply(f"I'd rate you `{thing}` a **{round(ramdi_amount, 4)} / 100** ramdi")

    @commands.command(hidden='True')
    async def secretping(self, ctx, message, member:discord.Member):
        try:
            member = int(member)
            member = bot.get_user(member)
        except:
            pass
        await ctx.send(f"{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {member.mention}")
        await ctx.message.delete()






def setup(bot):
    bot.add_cog(Fun_Commands(bot))
