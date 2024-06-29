import discord
from discord.ext import commands
import random
import os
import requests
with open("token.txt", "r") as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

recycle = {
    'kulit_pisang': 'kompos skala kecil.\n cara membuat kompos https://youtu.be/jF_ja8ZT3MY?si=hDtp5pVECgk4ACoT ',
    'botol_plastic': 'sampah ini bisa di buat menjadi:mobil mainan.\n cara membuat mobil mainan https://www.youtube.com/watch?v=TOjDb2KRVxg&pp=ygUna2VyYWppbmFuIG1vYmlsIG1haW5hbiBkYXJpIGJvdG9sIGJla2Fz',
    'styrofoam': 'alternatif lem. \n cara membuat alternatif lem https://youtu.be/0NzIxLrhdFY?si=6oeBxR97pu-gqEKb ',
    'sedotan_plastic': 'perhiasan gelang.\ncara membuar gelang dari sedotan https://youtu.be/OFzMNPZfxbc',
    }
not_recycle = {
    'batery': 'sampah ini tidak bisa di daur ulang',
    'bola_lampu':'sampah ini tidak bisa di daur ulang',
}
@bot.command("daur_ulang")
async def ide(ctx, item: str):
    # Mengecek apakah ide kerajinan tersedia untuk item tertentu
    if item.lower() in recycle:
        await ctx.send(f"Ide untuk membuat kerajinan dari {item.capitalize()}:\n{recycle[item.lower()]}")
    elif item.lower() in not_recycle:
        await ctx.send(f"Ide untuk membuat kerajinan dari {item.capitalize()}:\n{not_recycle[item.lower()]}")
    else:
        await ctx.send(f"Maaf, ide untuk membuat kerajinan dari {item.capitalize()} tidak ditemukan.")
bot.run(token)
