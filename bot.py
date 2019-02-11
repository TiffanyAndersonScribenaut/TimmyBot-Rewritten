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
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await bot.say(f"My ping is {ping}ms")

@bot.command(pass_context=True)
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")

@bot.command(pass_context=True)
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")


@bot.command(pass_context=True)
async def botinfo(ctx, discord):
    embed=discord.Embed(title="Info", description="Sup. My name is TimmyBot. ", color=0xebc000)
    embed.add_field(name=Name, value=TimmyBot, inline=False)
    embed.add_field(name="Bot Author", value="TimmyTimothyAnderson#3719", inline=False)
    embed.add_field(name="Library", value="discord.py (Python)", inline=False)
    embed.set_footer(text="Use t!help to get a list of commands")
    await bot.say(embed)

bot.run(os.getenv('TOKEN'))
