import os
import discord
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depresed", "unhappy", 
"mad", "depressing"]
sEncouragements = ["You got this bro", "hang in there bro", "You are a great bro!"]

mad_words = ["mad", "angry","annoyed", "pissed"]
mEncouragements = ["Chill bro", "I know.. bro", "Like bro, whateven bro.", "I hate it to bro."]

tired_words = ["tired", "sleepy", "exhausted"]
tEncouragements = "maybe its time for a bro nap snuggle sesh bro?"

def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return(quote)

def updateEncouragements(eMsg):
	if "encouragements" in db.key():
		encouragements = db["encouragements"]
		encouragements.append(eMsg)
		db["encouragements"] = encouragements
	else:
		db["encouragements"] = [eMsg] 

def deleteEncouragements(index):
	encouragements = db["encouragements"]
	if len(encouragements) > index:
		del encouragements[index]
		db["encouragements"] = encouragements



@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client) )

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	msg = message.content
	
	if message.content.startswith('$hello bro'):
		await message.channel.send("Sup Bro!");

	if msg.startswith('$brospire'):
		curQuote = get_quote()
		await message.channel.send('"' + curQuote + '"' + '"'"bro - brobot")

	if any(word in msg for word in sad_words):
		await message.channel.send(random.choice(sEncouragements))
	
	if any(word in msg for word in mad_words):
		await message.channel.send(random.choice(mEncouragements))

	if any(word in msg for word in tired_words):
		await message.channel.send(random.choice(tEncouragements))

	

client.run(os.environ['Token'])