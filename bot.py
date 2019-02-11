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
    embed=discord.Embed(title="Info", description="Sup. My name is TimmyBot. ", color=0xebc000)
    embed.add_field(name=Name, value=TimmyBot, inline=False)
    embed.add_field(name="Bot Author", value="TimmyTimothyAnderson#3719", inline=False)
    embed.add_field(name="Library", value="discord.py (Python)", inline=False)
    embed.set_footer(text="Use t!help to get a list of commands")
    await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))
