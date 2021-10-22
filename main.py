# HangMan, Tictactoe, Jokes

import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')

loaded_hangman = False
loaded_tictactoe = False


@client.event
async def on_ready():
  print("The Bot is online !")

#load and display hangman
@client.command()
async def hangman(ctx):

  global loaded_tictactoe
  global loaded_hangman

  if loaded_tictactoe == True: client.unload_extension("cog_games.tictactoe")
  client.load_extension("cog_games.hangman")
  loaded_hangman = True

  embed = discord.Embed(
      title='HANGMAN', 
      description="Hello there (Woof Woof) !! Lets test your guessing skills and see if you can crack the word (that I choose) in under 6 moves !!\n\n PS: I'm pretty competitive so I wont make it easy! Gear Up. Woof Woof !\n\nRULES:\n\n1. I'll choose a random word.\n2. You have to choose an alphabet or a word.\n If you choose correctly I'll fill it, else you HANG !\n\n! ALL THE BEST ! WOOF WOOF !\n\n"
    )
  embed.set_footer(text="To start a new game type .play and press ENTER")
  await ctx.send(embed=embed)


#load and display tictactoe
@client.command()
async def tictactoe(ctx):

  global loaded_tictactoe
  global loaded_hangman

  if loaded_hangman == True: client.unload_extension("cog_games.hangman")
  client.load_extension("cog_games.tictactoe")
  loaded_tictactoe = True

  embed = discord.Embed(
    title='TIC-TAC-TOE', 
    description="Hello there (Woof Woof) !! Tic-Tac-Toe is fun ! But its even more fun when you play with a friend ! So come on ! Play with a friend and try to beat them in an exciting game of one of the oldest yet one of the best games of all time, Classic Tic-Tac-Toe\n\n"
  )
  embed.set_footer(text="To start a new game type .play [@mention @mention] and mention 2 player names then press ENTER\neg: .play @Bot1 @Bot2")
  await ctx.send(embed=embed)

# @client.command()
# async def load(ctx , extension):
#   client.load_extension(f"cogs.{extension}")

# @client.command()
# async def unload(ctx , extension):
#   client.unload_extension(f"cogs.{extension}")


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


my_secret = os.environ['TOKEN']

client.run(my_secret)
