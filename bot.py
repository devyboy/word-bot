import requests
import sys
import discord
import json
import time

TOKEN = ""
client = discord.Client()
file = open('./words.txt')

@client.event
async def on_message(message):
    if message.content == "!word":
        word = next(file).replace("\n", "")
        if word == "end":
            await client.send_message(discord.Object(id='497129379952853002'), "The end of the word list has been reached! Please reload and restart the script.".format(message$
            return 0
        app_id = ''
        app_key = ''

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word
        wordResponse = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}).json().get("results")[0]["lexicalEntries"][0]

        defin = wordResponse["entries"][0]["senses"][0]["definitions"][0]
        audio = wordResponse["pronunciations"][0]["audioFile"]
        pronun = wordResponse["pronunciations"][0]["phoneticSpelling"]
        part = wordResponse["lexicalCategory"]
        example = wordResponse["entries"][0]["senses"][0]["examples"][0]["text"]

        embed = discord.Embed(title="Word of the Day:", description=word, color=0x4286f4)
        embed.add_field(name="Part of Speech:", value=part, inline=False)
        embed.add_field(name="Definition:", value=defin, inline=False)
        embed.add_field(name="Pronunciation:", value=pronun, inline=False)
        embed.add_field(name="Pronunciation: Audio", value=audio, inline=False)
        embed.add_field(name="Example:", value=example, inline=False)

        await client.send_message(discord.Object(id='497129379952853002'), embed=embed)

client.run(TOKEN)
