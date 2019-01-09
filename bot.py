import discord
import os
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

guildids = ["519451035836874763"]
channelids = ["519490720583778307", "520494704442212382", "519491305324281857"]

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id not in channelids and message.server.id in guildids:
        def check(message):
            return message.content
        spam = await client.wait_for_message(author=message.author, channel= message.channel,check=check, timeout=1)
        spam1 = await client.wait_for_message(author=message.author, check=check, timeout=1, channel= message.channel)
        spam2 = await client.wait_for_message(author=message.author, check=check, timeout=1, channel= message.channel)
        await client.delete_message(spam)
        await client.delete_message(spam1)
        await client.delete_message(spam2)
    else:
      return

client.run(os.environ['Token'])
