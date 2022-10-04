import discord, os
from discord.ext import commands
#from alive import keep_alive


from utils import default
from utils.data import Bot, HelpFormat

config = default.config()
print("Logging in...")

bot =  Bot(
    command_prefix=config["prefix"], prefix=config["prefix"],
    owner_ids=config["owners"], command_attrs=dict(hidden=True), help_command=HelpFormat(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    intents=discord.Intents(
        guilds=True, members=True, messages=True, reactions=True, presences=True
    )
)


@bot.event
async def on_ready():
    print("Starting")
    await bot.change_presence(status = discord.Status.online, activity=discord.Game("https://hailcore.co/discord"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# #keep_alive()

bot.run(config['token'])
# bot.run('NjkzNDU0MTM0ODA3ODg3OTkz.Xn9TfQ.rUyeIUTviVgsuproy6rkCJ1bt-g')
# bot.run('NzU5NjQ1MzkxODkyNTEyNzc4.X3Ag5g.kx1zWnWie1oiO_SC2PPnej9RYxo')
