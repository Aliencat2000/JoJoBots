#!/usr/bin/python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'mona lisa' in message.content.lower():
        await message.channel.send(file=discord.File('smile.jpg'))
    if 'ambulance' in message.content.lower():
        await message.channel.send(file=discord.File('ambulance.gif')) 
    if 'lunch' in message.content.lower() or 'hungry' in message.content.lower():
        await message.channel.send("Ah, time for lunch", file=discord.File('lunch.jpeg'))
    if 'bites the dust' in message.content.lower(): 
        await message.channel.send(file=discord.File('bitesthedust.gif'))
    if 'open door' in message.content.lower():
        await message.channel.send(f"@{message.author} Killer Queen has already touched that doorknob", file=discord.File('doorknob.gif'))

client.run(TOKEN)
