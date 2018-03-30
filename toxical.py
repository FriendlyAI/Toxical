import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot
from pymongo import MongoClient
from analyze_sentiment import analyze
import time

BOT_PREFIX = '!'
# Get at https://discordapp.com/developers/applications/me
TOKEN = 'NDI3MTQ3Mjc0NDk4MzQyOTMy.DZgT3g.UwYjlweXBF0b1X03r74lUt-v1ms'

client = Bot(command_prefix=BOT_PREFIX)
c = MongoClient()
db = c['toxicity']

MAX_SCORE = 25
WARNING_SCORE = 15
BAN_SCORE = 10
database = db.serves


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='positively'))
    print('Logged in as ' + client.user.name)
    servers = list(client.servers)
    for server in servers:
        for member in server.members:
            if database.find({'UID': member.id}).count() == 0:
                database.insert_one({'UID': member.id, 'points': MAX_SCORE, 'last message': time.time()})
    for x in list(database.find()):
        print(x)


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
        try:
            score_change = 0
            for sentence in message.split('. '):
                score_change += min(analyze(sentence).get('watson'), 0)
            # message_toxicity_string, toxicity_dict = analyze(message.content)
            # await client.send_message(message.channel, message_toxicity_string)
        except TypeError:  # returned none
            return

        # Update score

        current_time = time.time()
        old_time = current_time

        if database.find({'UID': message.author.id}).count() == 0:
            database.insert_one({'UID': message.author.id, 'points': MAX_SCORE, 'last message': time.time()})

        database_match = db.serves.find({'UID': message.author.id})
        for user in database_match:
            prev_score = user.get('points')
            old_time = user.get('last message')

        time_points = (current_time - old_time) / 600

        new_score = min(prev_score + time_points, MAX_SCORE) + score_change

        db.serves.update({'UID': message.author.id},
                         {'UID': message.author.id,
                          'points': new_score,
                          'last message': current_time})

        if new_score <= BAN_SCORE:
            try:
                await client.ban(message.server.get_member(message.author.id), delete_message_days=0)
            except discord.errors.Forbidden:
                print('Privilege too low')
            else:
                db.serves.remove({'UID': message.author.id})

        elif new_score <= WARNING_SCORE:
            await client.send_message(message.channel,
                                      f'**WARNING, <@{message.author.id}>, your positivity score is very low '
                                      f'({"{0:0.1f}".format(new_score)}/{MAX_SCORE})**'
                                      f'\nYou will be banned if your score reaches {BAN_SCORE} or below.')


@client.command(pass_context=True)
async def score(ctx):

    if database.find({'UID': ctx.message.author.id}).count() == 0:
        database.insert_one({'UID': ctx.message.author.id, 'points': MAX_SCORE, 'last message': time.time()})

    current_time = time.time()
    old_time = current_time

    database_match = db.serves.find({'UID': ctx.message.author.id})
    for user in database_match:
        old_time = user.get('last message')
        prev_score = user.get('points')

    time_points = (current_time - old_time) / 600

    db.serves.update({'UID': ctx.message.author.id},
                     {'UID': ctx.message.author.id,
                      'points': min(prev_score + time_points, MAX_SCORE),
                      'last message': current_time})

    await client.send_message(ctx.message.channel,
                              f'{ctx.message.author}\'s score is '
                              f'{"{0:0.1f}".format(min(prev_score + time_points, MAX_SCORE))}/{MAX_SCORE}')


client.loop.create_task(list_servers())
client.run(TOKEN)
