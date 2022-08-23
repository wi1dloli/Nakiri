import discord 
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello World")

async def setup(bot:commands.Bot):
    await bot.add_cog(Misc(bot))