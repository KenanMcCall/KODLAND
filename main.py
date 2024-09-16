import discord
from discord.ext import commands, tasks
import os, random
from itertools import cycle
import requests
from bot_console import *
from bot_console import gen_pass

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

activities = [
    discord.Game(name = "By Kenan McCall"),
    discord.Activity(type=discord.ActivityType.listening, name = "Kenan McCall'ın Hizmetinde!"),
    discord.Activity(type=discord.ActivityType.watching, name = "Sunucu Güvenliğini Sağlıyor!")
]

statuses = [
    discord.Status.online,
    discord.Status.idle,
    discord.Status.dnd,
]

@tasks.loop(minutes = 5)  
async def update_status():
    activity = random.choice(activities)
    status = random.choice(statuses)
    await bot.change_presence(activity=activity, status=status)
    print(f'Aktiflik durumu ve kullanıcı durumu değiştirildi: {activity}, {status}')

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı!')
    update_status.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "selam" in message.content.lower():
        await message.channel.send("Aleyküm Selam!")
    await bot.process_commands(message)


@bot.command()
async def mem(ctx):
    resim_adi = random.choice(os.listdir("images"))
    file_path = f'images/{resim_adi}' 
    try:
        with open(file_path, 'rb') as f:
            picture = discord.File(f)  
        await ctx.send(file=picture) 
    except FileNotFoundError:
        await ctx.send("Fotoğraf bulunamadı.")  


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def sifre(ctx):
    await ctx.send(gen_pass(10))

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
        await ctx.send("1 ile 200 arasında bir sayı girin.")
        return
    
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send(f"**{len(deleted)}** *mesaj silindi.*", delete_after=2)

duyuru_mesajlari = cycle([
    "**🌍 Çevremizi Temiz Tutalım!**\n\n"
    "*Temiz bir çevre sağlıklı bir yaşam için en temel gereksinimlerden biridir.* "
    "*Çevremizi temiz tutmak için lütfen aşağıdaki adımlara dikkat edelim* :\n\n"
    "**1.** ♻️ Atıklarınızı doğru şekilde geri dönüştürün.\n"
    "**2.** 🗑️ Çöplerinizi uygun alanlara atın.\n"
    "**3.** 💡 Enerji tasarrufu yapın ve doğal kaynakları koruyun.\n"
    "**4.** 🚮 Sokakları ve parkları temiz tutalım, çöplerimizi etrafa bırakmayalım.\n\n"
    "*Hep birlikte daha yaşanabilir bir dünya için adım atalım!* \n<@&1219368556031115354>",

    "**♻️ Geri Dönüşümün Önemi!**\n\n"
    "*Geri dönüşüm, doğal kaynakları korumanın ve enerji tasarrufu yapmanın harika bir yoludur.* "
    "*Her atık doğru bir şekilde geri dönüştürülmelidir* :\n\n"
    "**1.** Cam, kağıt ve plastik atıklarınızı ayrı ayrı biriktirin.\n"
    "**2.** Geri dönüşüm kutularını kullanın ve atıkları ayırın.\n"
    "**3.** Elektronik atıkları özel toplama merkezlerine teslim edin.\n\n"
    "*Doğayı korumak için geri dönüşüm bilincini yayalım!* \n<@&1219368556031115354>",

    "**🌱 Doğal Kaynakları Korumak**\n\n"
    "*Doğal kaynaklar sınırlıdır ve onları doğru kullanmak zorundayız.* "
    "*Bunun için şu adımları takip edelim* :\n\n"
    "**1.** 💧 Su tasarrufu yapın, muslukları gereksiz yere açık bırakmayın.\n"
    "**2.** 🔋 Yenilenebilir enerji kaynaklarını tercih edin.\n"
    "**3.** 🍃 Doğal ürünler tüketmeye özen gösterin.\n\n"
    "*Daha yeşil bir gelecek için bugünden harekete geçelim!* \n<@&1219368556031115354>"
])

@tasks.loop(seconds=10)
async def cevre_bilgilendirme_gorevi(duyuru_kanal_id):
    duyuru_kanal = bot.get_channel(duyuru_kanal_id)
    duyuru_mesaji = next(duyuru_mesajlari)

    if duyuru_kanal:
        await duyuru_kanal.send(duyuru_mesaji)

@bot.command()
async def duyuru(ctx):
    duyuru_kanal_id = 1219368610166997053
    cevre_bilgilendirme_gorevi.start(duyuru_kanal_id)

bot.run("TOKEN")
