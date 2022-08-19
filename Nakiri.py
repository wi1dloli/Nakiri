# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.AutoShardedBot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

bot.run(os.getenv("DISCORD_TOKEN"))