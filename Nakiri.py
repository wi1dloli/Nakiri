# Nakiri.py
import os

import asyncio
import discord
intents = discord.Intents.all()
intents.reactions = True
intents.members = True
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';;', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

async def startup():
    await bot.load_extension("cogs.misc")
    bot.run(TOKEN)

#asyncio.run(startup())