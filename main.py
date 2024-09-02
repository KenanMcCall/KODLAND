import discord
from discord.ext import commands
from bot_console import *
from bot_console import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def sifre(ctx):
    await ctx.send(gen_pass(10))
    
@bot.command()
async def Merhaba(ctx):
    await ctx.send("Merhaba!")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTI3NzY3MzQ4ODU4ODYwNzY0MQ.GrLJf1.AyPRLTRcyAVlThi9G5KFRI3Wcw_QXfbTfd0_fg")
