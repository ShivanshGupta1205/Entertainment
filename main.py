# HangMan, Jokes

import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print("The Bot is online !")

@client.command()
async def hangman(ctx):

  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      client.unload_extension(f'cogs.{filename[:-3]}')

  client.load_extension("cogs.hangman")
  embed = discord.Embed(
      title='HANGMAN', 
      description="Hello there (Woof Woof) !! Lets test your guessing skills and see if you can crack the word (that I choose) in under 6 moves !!\n\n PS: I'm pretty competitive so I wont make it easy! Gear Up. Woof Woof !\n\nRULES:\n\n1. I'll choose a random word.\n2. You have to choose an alphabet or a word.\n If you choose correctly I'll fill it, else you HANG !\n\n! ALL THE BEST ! WOOF WOOF !\n\n"
    )
  embed.set_footer(text="To start a new game type .play and press ENTER")
  await ctx.send(embed=embed)
   

@client.command()
async def load(ctx , extension):
  client.load_extension(f"cogs.{extension}")

# @client.command()
# async def unload(ctx , extension):
#   client.unload_extension(f"cogs.{extension}")


# for filename in os.listdir('./cogs'):
#   if filename.endswith('.py'):
#     client.load_extension(f'cogs.{filename[:-3]}')


my_secret = os.environ['TOKEN']

client.run(my_secret)
