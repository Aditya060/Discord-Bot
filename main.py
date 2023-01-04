import discord
import os
import json # to work with the zen quotes api
import requests
from jinda import jinda
import openai
# openai.organization = "org-EaMgZykySWR982RwKgf7Xz6G"
# openai.api_key = os.getenv("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")
# openai.Model.list()
openai.api_key = "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"



client=discord.Client()

def get_chatgpt_response(prompt):
  # print(prompt)
  response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
  )
  return response['choices'][0]['text']
  

  
  
def get_dog_image():

  response =         requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  dog_image=json_data['message']
  return (dog_image)


def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text) 
  quote = json_data[0]['q'] + " -" + json_data[0]['a'] #q for quote, a for author
  return(quote)

def get_advice():
  response = requests.get('https://api.adviceslip.com/advice')
  myobj=json.loads(response.text)
  # print(myobj['slip']['advice'])
  return myobj['slip']['advice'] #spent hours to get this part right, kms
  
  # fetch('	https://api.adviceslip.com/advice').then(response => {
  #   return response.json();}).then(adviceData => {const AdviceObj =  adviceData.slip;
  #   })
  # })
# return AdviceObj.advice


  # def get_liked_songs():
  #   	response = requests.get(https://api.spotify.com/v1/me/tracks)
  #   myobj = json.load(respose.text)
  #   return 

  
  
  
  

@client.event
async def on_ready():
  print ('Logged in  as{0.user}'.format(client))

@client.event
async def on_message(message):#these namees are from discord documentation
  print('Message here2')
  print(message.content[2:])
  if message.author == client.user:
    return #if message is from the bot itself, ignore
  # if message.content.startswith('$hello'):
  #   await message.channel.send('Hi there! What\'s up?')
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$advice'):
    advice = get_advice()
    await message.channel.send(advice)

  if message.content.startswith('$dog'):
    dog_image = get_dog_image()
    await message.channel.send(dog_image)

  if message.content.startswith('$g'):
    response = get_chatgpt_response(message.content[2:])
    await message.channel.send(response)

jinda()
client.run(os.environ['TOKEN'])
