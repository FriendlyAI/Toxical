import asyncio
from discord import Game
from discord.ext.commands import Bot
from pymongo import MongoClient
from analyze_sentiment import analyze

BOT_PREFIX = '!'
TOKEN = 'NDI3MTQ3Mjc0NDk4MzQyOTMy.DZgT3g.UwYjlweXBF0b1X03r74lUt-v1ms'  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)
c = MongoClient()
db = c['toxicity']


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='toxic'))
    print('Logged in as ' + client.user.name)
    servers = list(client.servers)
    database = db.serves
    for server in servers:
        for member in server.members:
            # print(database.find({'UID': member.id}).count())
            if database.find({'UID': member.id}).count() == 0:
                database.insert_one({'UID': member.id, 'points': 100})
    # print(list(database.find()))



async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print('Current servers:')
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content != '!score' and message.author.id != client.user.id:
        message_toxicity_string, toxicity_dict = analyze(message.content)
        await client.send_message(message.channel, message_toxicity_string)


@client.command(pass_context=True)
async def score(ctx):
    database = db.serves.find()
    for user in database:
        if user.get('UID') == ctx.message.author.id:
            await client.send_message(ctx.message.channel,
                                      f'{ctx.message.author}\'s score is {user.get("points")}/100')


client.loop.create_task(list_servers())
client.run(TOKEN)
