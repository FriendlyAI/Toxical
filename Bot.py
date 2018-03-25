import random
import asyncio
import requests
from discord import Game
from discord.ext.commands import Bot
from pymongo import MongoClient
from temp_sentiment_analyzer import analyze
from collections import deque

BOT_PREFIX = ("?", "!")
TOKEN = "NDI3MTQ3Mjc0NDk4MzQyOTMy.DZgT3g.UwYjlweXBF0b1X03r74lUt-v1ms" # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)
c = MongoClient()
db = c['toxicity']

queue = deque([])

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="toxic"))
    print("Logged in as " + client.user.name)
    servers = list(client.servers)
    ser = db.serves
    for x in range(len(servers)):
        for member in servers[x].members:
            ser.insert_one({"Servers":
                                {"SID": servers[x].id, "users":
                                    {"UID": member.id, "points":  100}}})

def calc_server_tox():
    servetox = db.serves.find()


# @client.command()
# async def bitcoin():
#     url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#     response = requests.get(url)
#     value = response.json()['bpi']['USD']['rate']
#     await client.say("Bitcoin price is: $" + value)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        message_toxicity_string, toxicity_dict = analyze(message.content)
        await client.send_message(message.channel, message_toxicity_string)
        if len(queue) > 100:
            queue.popleft()
        queue.append(message.content)


client.loop.create_task(list_servers())
client.run(TOKEN)