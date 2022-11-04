import discord
import requests
import json
import asyncio
import os

client = discord.Client(intents=discord.Intents.default())

def get_question():
    qs = ''
    id = 1
    answer =  0
    response = requests.get("http://mot-bot-app.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs+= "question: \n"
    qs+= json_data[0]['title'] + "\n"

    for item in json_data[0]["answer"]:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id

        id += 1
    return(qs, answer)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$question'):

        qs, ans = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()
        
        try:
            guess = await client.wait_for('message', check=check, timeout=3.0)
            
        except asyncio.TimeoutError:
            return await message.channel.send('Your response took too long.')

        if int(guess.content) == ans:
            await message.channel.send('Yay, you are right!')
        else:
            await message.channel.send('Oops! Wrong answer.')
        


client.run('DISCORD_TOKEN'),

