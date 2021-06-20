import discord
import os

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
  
  if any(em in message.content for em in ['😈','dewol','hehe']):
    await message.add_reaction('😈')

  if any(sad_indicator in message.content for sad_indicator in ['<:sadgeraz:792469326304509973>','sad','sadge','rip','F']):
    await message.add_reaction('<:sadgeraz:792469326304509973>')
  
  if message.role_mentions:
    rms = ' ,   '.join(list(map(lambda R: R.name, message.role_mentions)))
    await message.channel.send(f"{'Role' if len(message.role_mentions)<2 else 'Roles'}   {rms}   {'was' if len(message.role_mentions)<2 else 'were'} mentioned.")

  print(message.content)

client.run(os.environ['TOKEN'])
