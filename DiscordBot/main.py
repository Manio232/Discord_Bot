from email import message

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID = 927964153375760435  # ID kanału powitalnego
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='~', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user}!{bot.user.name}')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f'{member.mention} Witaj na serwerze. Napisz ~help aby zobaczyć dostępne komendy!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('~hello'):
        await message.channel.send(f'Hello {message.author.mention}!')
    if "kurwa" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention} Nie przeklinaj kolego! to jest serwer z kulturą! Bardzo cię proszę! :pleading_face:')
    if "spierdalaj" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention} Nie przeklinaj kolego! to jest serwer z kulturą! Bardzo cię proszę! :pleading_face:')
    if "chuj" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention} Nie przeklinaj kolego! to jest serwer z kulturą! Bardzo cię proszę! :pleading_face:')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(token)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')


@bot.command()
async def help(ctx):
    await ctx.send(f'Dostępne komendy:\n~ping - odpisuje pong\n~hello - powita użytkownika\n~help - wyświetla dostępne komendy\n~role - przypisuje rolę użytkownikowi')


@bot.command()
async def role(ctx):
    roles = discord.utils.get(ctx.guild.roles, name="Mister")
    if roles in ctx.author.roles:
        await ctx.send(f'{ctx.author.mention} Masz już tą rolę!')
    else:
        await ctx.author.add_roles(roles)
        await ctx.send(f'{ctx.author.mention} Otrzymałeś rolę Mister!')


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
