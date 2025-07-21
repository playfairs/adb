import discord
import time

from discord.ext import commands
from discord import app_commands
from discord.ext.commands import (
    Cog,
    Context,
    Cog,
    hybrid_command as hybrid,
)

class Commands(Cog, description="Commands for ADB"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.tree = bot.tree

    @hybrid(name="adb", description="Run the ADB command")
    async def adb(self, ctx: Context) -> None:
        embed = discord.Embed(
            title="ADB Command Run Successfully!",
            description="In 30 days, you can claim your Active Developer Badge at https://discord.com/developers/active-developer-badge\n\n**You can claim your badge at <t:{}:F>**".format(int(time.time()) + 2592000)
        )
        embed.set_thumbnail(url="https://media.playfairs.cc/adb.png")
        await ctx.author.send(embed=embed)
        await ctx.send("Command was successful, check your DMs.", ephemeral=True)

    @hybrid(name="info", description="Get info about the ADB bot")
    async def info(self, ctx: Context) -> None:
        embed = discord.Embed(
            title="ADB Info",
            description="This bot is meant to be a simple way to get the **Active Developer Badge** on Discord for those who either don't have the time or don't know how to do it themselves."
        )
        embed.add_field(name="Developer", value="> [playfairs](https://github.com/playfairs)", inline=False)
        embed.add_field(name="Source Code", value="> https://github.com/playfairs/adb", inline=False)
        embed.add_field(name="Support Server", value="> https://discord.gg/vortexbot", inline=False)
        embed.set_thumbnail(url="https://media.playfairs.cc/adb.png")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Commands(bot))