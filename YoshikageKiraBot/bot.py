#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

dirname = os.path.dirname(__file__)

def get_image(name: str) -> discord.File:
    filename = os.path.join(dirname, 'images', name)
    return discord.File(filename)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    channels = client.get_all_channels()
    
    for channel in channels:
        print(channel.guild)
        if channel.name in ['bots', 'general']:
            await channel.send("Has anyone seen a brown paper bag?")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'mona lisa' in message.content.lower():
        await message.channel.send(file=get_image('smile.jpg'))
    if 'ambulance' in message.content.lower():
        await message.channel.send(file=get_image('ambulance.gif')) 
    if 'lunch' in message.content.lower() or 'hungry' in message.content.lower():
        await message.channel.send("Ah, time for lunch", file=get_image('lunch.jpeg'))
    if 'bites the dust' in message.content.lower(): 
        await message.channel.send(file=get_image('bitesthedust.gif'))
    if 'open door' in message.content.lower():
        await message.channel.send(f"@{message.author} Killer Queen has already touched that doorknob", file=get_image('doorknob.gif'))

client.run(TOKEN)
