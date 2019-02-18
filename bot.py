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
async def botinfo(ctx, discord):
    embed=discord.Embed(title="Info", description="Sup. My name is TimmyBot. ", color=0xebc000)
    embed.add_field(name=Name, value=TimmyBot, inline=False)
    embed.add_field(name="Bot Author", value="TimmyTimothyAnderson#3719", inline=False)
    embed.add_field(name="Library", value="discord.py (Python)", inline=False)
    embed.set_footer(text="Use t!help to get a list of commands")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def timmy(ctx):
    await bot.say("https://cdn.discordapp.com/avatars/490270369865924638/b45370764d2dcf1d237f254c1789c1c3.png?size=1024")

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("Invite me with this link: https://discordapp.com/api/oauth2/authorize?client_id=530988566050897949&permissions=8&scope=bot")
      
bot.run(os.getenv('TOKEN'))
