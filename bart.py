import discord
import os
from dotenv import load_dotenv as ldv

ldv()

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$echo'):
    await message.delete()
    await message.channel.send(message.content[len('$echo')+1:])
  
  if any(dem in message.content for dem in ['😈','dewol','hehe']):
    await message.add_reaction('😈')

  if any(sad_indicator in message.content for sad_indicator in ['<:sadgeraz:792469326304509973>','sad','sadge','rip','F']):
    await message.add_reaction('<:sadgeraz:792469326304509973>')
  
  if message.role_mentions:
    rms = ' ,   '.join(list(map(lambda R: R.name, message.role_mentions)))
    await message.channel.send(f"{'Role' if len(message.role_mentions)<2 else 'Roles'}   {rms}   {'was' if len(message.role_mentions)<2 else 'were'} mentioned.")

  if any(em in message.content for em in ['🚀','rocket']):
    await message.add_reaction('🚀')

  print(message.content)

client.run(os.environ['BART_TOKEN'])