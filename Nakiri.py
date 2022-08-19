# Nakiri.py
import os

import discord
intents = discord.Intents.default()
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

bot.run(TOKEN)