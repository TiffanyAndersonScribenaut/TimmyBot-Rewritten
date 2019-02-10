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

@bot.command(pass_context=True)
async def botinfo(ctx):
    await bot.say("Sup. my name is TimmyBot. A bot created by `TimmyTimothyAnderson#3719`")
    await bot.say("Library: discord.py `Used to be made in discord.js`")

bot.run(os.getenv('TOKEN'))
