import discord 
import asyncio
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello World")

    @commands.command()
    async def prefix(self, ctx: commands.Context):
        await ctx.send("My prefix is ;;")
async def setup(bot:commands.Bot):
    await bot.add_cog(Misc(bot))