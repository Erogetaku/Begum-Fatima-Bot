import os
import discord 
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()
words = ["ma ki", "ma ka", "madarchod", "bhenchod","Ma ki", "ma Ki", "Ma Ki", "Madarchod", "Bhenchod", "madar chod", "Madar chod", "madar Chod", "Madar Chod", "Bhen chod", "bhen chod", "bhen Chod", "Bhen Chod", "Behen chod", "behen chod", "behen Chod", "bhen ka", "bhen Ka", "bhen ki", "Bhen ka", "Bhen ki", "Bhen Ka", "behen ka", "behen ki"]
preachings = ["Targetting female relatives of the person you are attacking is a Mughal mindset. There's no difference between them and you, if you do the same thing...even without any ill intention or as a joke. This is strictly not allowed on this server. Repeated use can get you kicked or banned."]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$patthar'):
    await message.channel.send('Habibi!! Begum can be seen doing Pattharbazi')
  if any(word in message.content for word in words):
    await message.channel.send(random.choice(preachings))

keep_alive()
client.run(os.getenv('key'))
