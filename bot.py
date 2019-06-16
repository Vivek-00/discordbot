import discord
import json
from discord.ext import commands

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot is running")

@client.command()
async def ping(ctx):
    await ctx.send(f'latency:{round(client.latency)}ms')

@client.command()
async def det(ctx,searchName):
    with open('data.json') as f:
        data=json.load(f)
        for name, details in data.items():
            if name==searchName:
                (teamVar, teamVal),(gamesVar,gamesVal),(killsVar, killsVal),(deathVar, deathVal),(kdVar, kdVal),(mvpVar, mvpVal),(winsVar,winsVal),(lossVar,lossVal)=details.items()
                await ctx.send(f'{teamVar} : {teamVal} \n {gamesVar} : {gamesVal} \n {killsVar} : {killsVal} \n {deathVar} : {deathVal} \n {kdVar} : {kdVal} \n {mvpVar} : {mvpVal} \n {winsVar} : {winsVal} \n {lossVar} : {lossVal} \n For more info visit www.brawlesports.com ')

client.run(' ')
