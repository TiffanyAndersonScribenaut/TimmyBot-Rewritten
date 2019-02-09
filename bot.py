import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix="t!")

@bot.event
async def on_ready():
   print("Ready!")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")

bot.run(os.getenv('TOKEN'))
