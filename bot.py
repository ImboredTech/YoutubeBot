import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Online!')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
    else:
        print("__pycache__ folder is being stupid.")
        



bot.run(config.token)