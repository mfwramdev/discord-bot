import random
import discord
import secrets
import asyncio
import aiohttp
import discord
from io import BytesIO
from discord.ext import commands
from utils import lists, permissions, http, default


class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
        else:
            return m.id


class ActionReason(commands.Converter):
    async def convert(self, ctx, argument):
        ret = argument

        if len(ret) > 512:
            reason_max = 512 - len(ret) - len(argument)
            raise commands.BadArgument(f"reason is too long ({len(argument)}/{reason_max})")
        return ret


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()


class mod_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()


    @commands.command(hidden = True)
    @commands.has_permissions(administrator=True)
    async def sm(self, ctx, seconds: int):
        # if(not ctx.author.has_role(696331569979457546)): 
        #     return
    
        await ctx.channel.edit(slowmode_delay = seconds)
        if(seconds != 0): await ctx.send(f'Slowmode has been set to {seconds} seconds')
        else: await ctx.send('Slowmode has been removed')

    @commands.command(hidden = True)
    @permissions.has_permissions(ban_members=True)
    async def ban(self, ctx, member: MemberID, *, reason: str = None):
        """ Bans a user from the current server. """
        m = ctx.guild.get_member(member)
        if m is not None and await permissions.check_priv(ctx, m):
            return
        try:
            await ctx.guild.ban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))
            await ctx.send("Banned user")
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(mod_commands(bot))


