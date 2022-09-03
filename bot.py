import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import asyncio
import random
import discord
import os
from discord.ext import commands
import time

player = {}

client = commands.Bot(command_prefix='%', intents=discord.Intents.all())

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

        raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

@client.event
async def on_ready():
    print('Bot ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command(aliases =['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yes', 'No', 'Maybe']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def iroh(ctx):
    possible_quotes = ["IT IS USUALLY BEST TO ADMIT MISTAKES WHEN THEY OCCUR, AND TO SEEK TO RESTORE HONOR.", "IT IS IMPORTANT TO DRAW WISDOM FROM MANY DIFFERENT PLACES.", "IT'S TIME FOR YOU TO LOOK INWARD AND START ASKING YOURSELF THE BIG QUESTION: WHO ARE YOU AND WHAT DO YOU WANT?","SHARING TEA WITH A FASCINATING STRANGER IS ONE OF LIFE’S TRUE DELIGHTS.","HOPE IS SOMETHING YOU GIVE YOURSELF. THAT IS THE MEANING OF INNER STRENGTH.","DESTINY IS A FUNNY THING. YOU NEVER KNOW HOW THINGS ARE GOING TO WORK OUT.","WHILE IT IS ALWAYS BEST TO BELIEVE IN ONESELF, A LITTLE HELP FROM OTHERS CAN BE A GREAT BLESSING.", "PRIDE IS NOT THE OPPOSITE OF SHAME, BUT ITS SOURCE. TRUE HUMILITY IS THE ONLY ANTIDOTE TO SHAME", "LIFE HAPPENS WHEREVER YOU ARE, WHETHER YOU MAKE IT OR NOT."]
    selected_quote = random.choice(possible_quotes)
    embed = discord.Embed(title = "Iroh's wise words")
    embed.add_field(name = "Quote",value = selected_quote, inline = False)
    await ctx.send(embed = embed)

@client.command()
async def h(ctx):
    embed1 = discord.Embed(title = "COMMANDS HELP")
    embed1.add_field(name = "SoundBites",value = "3hits,bna,screen,donger,dima,moneh,game,genius,nigga,omae,kokodayo,nico,over9k,konoyaro,humble,zai,jesus,legend,deargod,wasthat,retirement,pension,banana,dowry,nerd,sixk,idi,miko,onore,degen,pardun,kiamoan,sayonara,asa,pogchamp,smol,winf,kuso,nono,ehe,gg,ara,putin,okaeri,madar,chutiya,benc,chipapa,fightback,doktah,protect,based,ape,dayo,sick,rei,chicken,tasukete,giveup,not2speak,rockch,cuntaway,2cb,2gud,ams,aui,beaut,cheeky,ded,dove,ephy,expected,explain,fog,freeze,impressed,noo,pep,praise,ros,sheever,shi,t2m,wai,wat,wut,wyd,yuno,kokki,besto,congrats", inline = False)
    embed1.add_field(name = "Wise Words",value = "iroh", inline = False)
    embed1.add_field(name = "Pokedex",value = "dex <name of pokemon>", inline = False)
    await ctx.send(embed = embed1)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(aliases =['3hits'])
async def _3hits(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/3hits.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(6)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def screen(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/screen.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(6)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def donger(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/donger.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(9)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def dima(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/dima.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(15)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def moneh(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/moneh.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(11)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def game(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/game.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(18)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def genius(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/genius.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(6)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def nigga(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/nigga.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(5)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def omae(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/omae.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def kokodayo(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/kokodayo.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(4)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def nico(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/nico.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def over9k(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/over9k.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def konoyaro(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/konoyaro.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def humble(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/humble.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(5)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def zai(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/zai.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(6)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def jesus(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/jesus.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(5)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def legend(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/legend.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(5)

    server = ctx.message.guild.voice_client
    await server.disconnect()


@client.command()
async def deargod(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/deargod.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def wasthat(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/wasthat.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def retirement(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/retirement.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(3)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def pension(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/pension.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(2)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def banana(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('./audiofiles/banana.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    time.sleep(6)

    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def dowry(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/dowry.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(10)

        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def nerd(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/nerd.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(14)

        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def sixk(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/sixk.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def idi(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/idi.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def miko(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/miko.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def onore(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/onore.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def degen(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/degen.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def pardun(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/PARDUN.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def kiamoan(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/kiamoan.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(12)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def sayonara(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/sayonara.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def asa(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/asa.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(9)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def pogchamp(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/little_pogchamp1.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def smol(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/smol.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(14)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def winf(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/WinF.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(17)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def kuso(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/kuso.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def nono(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Not_there.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(7)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ehe(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Ehe_te_nandayo.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def gg(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Okay_Im_Dead_GG.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ara(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/AraAra.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def putin(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/boifrend.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def okaeri(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/OKAERI.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(10)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def madar(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Madar_Chodh.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def benc(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Benchodh.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(8)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def chutiya(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Chutiya.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(7)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def chipapa(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Chi_Pa_Pa.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def fightback(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/fightback.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def doktah(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Okaeri_Doktah.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ape(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/Ape.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(11)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def protect(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/protect.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def based(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/based.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def dayo(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/dayo.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def sick(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/sickfujck.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(11)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def rei(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/reirei.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def giveup(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/giveup.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(9)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def chicken(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/chicken.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(7)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def tasukete(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/tasukete.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def not2speak(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/not2speak.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(9)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def rockch(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/rockch.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def cuntaway(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/cuntaway.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(6)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command(aliases =['2cb'])
async def _2cb(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/2cb.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command(aliases =['2gud'])
async def _2gud(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/2gud.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ams(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/ams.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(1.5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def aui(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/aui.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def beaut(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/beaut.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def cheeky(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/cheeky.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()
@client.command()
async def ded(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/ded.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def dove(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/dove.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ephy(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/ephy.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def expected(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/expected.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def explain(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/explain.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def fog(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/fog.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def freeze(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/freeze.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def impressed(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/impressed.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def noo(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/noo.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def pep(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/pep.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def praise(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/praise.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def ros(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/ros.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def sheever(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/sheever.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def shi(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/shi.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def t2m(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/t2m.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def wai(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/wai.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def wat(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/wat.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def wut(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/wut.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def wyd(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/wyd.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(2)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def yuno(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/yuno.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def kokki(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/kokki_kumar.wav')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def bna(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/bna.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(3)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def besto(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/besto.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(5)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def congrats(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('./audiofiles/congrats.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        time.sleep(4)

        server=ctx.message.guild.voice_client
        await server.disconnect()

@client.command(pass_context=True)
async def dex(ctx, *, entryname):
    url = "https://www.pokemon.com/us/pokedex/" + entryname
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    html = urlopen(req)
    soup = BeautifulSoup(html, features="html.parser")
    textsc = soup.find_all('div', attrs={'class':'pokedex-pokemon-pagination-title'})
    textsc = str(textsc)
    pname = textsc[60:-62]
    print(pname)
    textsc = soup.find_all('span', attrs={'class':'pokemon-number'})
    textsc = str(textsc)
    pnum = textsc[233:-81]
    print(pnum)
    textsc = soup.find_all('p', attrs={'class':'version-x'})
    textsc = str(textsc)
    descrip = textsc[48:-22]
    print(descrip)
    c = 0
    type = []

#

    typelist = ["Fire","Grass","Water","Ice","Dragon","Rock","Ground","Electric","Fairy","Dark","Bug","Fighting","Poison","Steel","Flying","Normal","Psychic","Ghost"]
    textsc = soup.find_all('a', attrs={'href': lambda x: x and x.startswith('/us/pokedex/?type=') })
    textsc = str(textsc)
    for x in range(len(typelist)):
        if typelist[x] in textsc:
            type.append(typelist[x])
    await ctx.send("```Name: " + pname + "\nPokeDex No.: " + pnum + "\n" + descrip + "\nTypes: " + type[0] + type[1]"```")

#


client.run(os.environ['TOKEN'])
