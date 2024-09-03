import discord
from discord.ext import commands
from bot_console import *
from bot_console import gen_pass

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "selam" in message.content.lower():
        await message.channel.send("Aleyküm Selam!")
    await bot.process_commands(message)

@bot.command()
async def sifre(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def emoji(ctx):
    await ctx.send()

@bot.command()
async def yazitura(ctx):
    yazi = "Yazı", "Tura"
    money = random.randint(1, 2)
    if money == 1:
        return("Yazı")
    elif money == 2:
        return("Tura")

@bot.command()
async def remoji(ctx):
    emoji = [":crown:", ":eyes:", ":heart:", ":zap:"]
    return random.choice(emoji)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, limit: int):
    if limit < 1 or limit > 200:
        await ctx.send('1 ile 200 arasında bir sayı girin.')
        return
    
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send(f'{len(deleted)} *mesaj silindi.*', delete_after=2)

bot.run("Token")
