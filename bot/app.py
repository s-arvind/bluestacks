import random

import discord
from config import BOT_TOKEN, SEARCH_SERVICE
from discord.ext import commands
from answers import *
import requests

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("C-3PO is Online.")


@client.event
async def on_message(message):
    await client.process_commands(message)
    if client.user.id != message.author.id:
        if message.content.lower() in GREETINGS_MSG:
            text = random.choice(GREETINGS_BOT)
            text += ', I am C-3PO. You probably saw me in **STAR WARS**. I speak English now.'
            await message.channel.send(text)
        elif 'how' in message.content.lower():
            text = 'I am not gonna lie. I have been better. \n Good Old Star Wars Days! :cry:'
            await message.channel.send(text)
        elif not message.content.startswith('!'):
            text = "I am sorry. My NLP engine is broken, can't talk. But believe me I do want to talk to you. :stuck_out_tongue:"
            await message.channel.send(text)



@client.command()
async def google(ctx, *args):
    # call search service to get search result
    phrase = ' '.join(args)
    response = requests.get(f'{SEARCH_SERVICE}/api/search/?q={phrase}')
    embed = discord.Embed(
        colour=discord.Colour.dark_green(),
        title='Google Search'
    )
    for search in response.json():
        embed.add_field(name="\u200b",value=search['title'], inline=False)
        embed.add_field(name="\u200b",value=search['link'], inline=False)
    await ctx.send(embed=embed)


@client.command()
async def recent(ctx, *args):
    # call search service to fetch recent searches
    phrase = ' '.join(args)
    response = requests.get(f'{SEARCH_SERVICE}/api/recent/?q={phrase}')
    embed = discord.Embed(
        colour=discord.Colour.dark_red(),
        title='Recent Searches'
    )
    for search in response.json():
        links = ' \n'.join(search['links'])
        embed.add_field(name="Title", value=search['text'], inline=False)
        embed.add_field(name="Links", value=links, inline=False)
    await ctx.send(embed=embed)


client.run(BOT_TOKEN)
