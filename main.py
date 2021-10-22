# HangMan, Tictactoe, Jokes

import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix='.',help_command=None)

loaded_hangman = False
loaded_tictactoe = False


@client.command()
async def help(ctx):
  embed = discord.Embed(
  description = """Hello there (woof woof)!\n
  My name is <@900271061193601024>. Yes you got that right! I'm the cute dog in the movie ENTERTAINMENT. And yes, Akshay Kumar was also in the movie but I dont think anyone noticed him over me !
  \nAnyways, enough about me ! Let's talk about what I'm doing here ! 

  I'm here to make your discord server veryyyyy interesting ! I am a wholesome package of interesting games and would even tell some nerdy jokes for all you coders out there ! I have the following games:

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

  """)

  embed.set_author(name="ENTERTAINMENT" , icon_url="https://cdn.discordapp.com/attachments/900244576458117130/901036028750598144/dog-modified.png")

  embed.add_field(name="\nHangman" , value = "Want to test how good your guessing game is ? Well I'm here to help you out ! Load a game of Hangman and test your guessing skills\n\nTo know more type .hangman !\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_")
  
  embed.add_field(name="\nTic-Tac-Toe" , value = "Remember Tic-Tac-Toe ?\nWell who doesn't !\nNow you can enjoy a fun game of tic-Tac-Toe with your friends\n\nTo know more type .tictactoe !\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_")
  
  embed.add_field(name="Jokes" , value = "Getting bored ? Don't Worry I'm here for you ! I have the best collection of super nerdy jokes for you coders out there ! Just type .joke to get some laugh ! \n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\n\n" , inline = False)

  await ctx.send(embed = embed)
  


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
      description="Hello there (Woof Woof) !! Lets test your guessing skills and see if you can crack the word (that I choose) in under 6 moves !!\n\n PS: I'm pretty competitive so I wont make it easy! Gear Up. Woof Woof !\n\nRULES:\n\n1. I'll choose a random word.\n2. You have to choose an alphabet or a word.\n If you choose correctly I'll fill it, else you HANG !\n\n! ALL THE BEST ! WOOF WOOF !\n"
    )
  embed.set_image(url="https://cdn.discordapp.com/attachments/900244576458117130/901038492539314226/hangman.png")
  embed.set_footer(text="To start a new game type .play and press ENTER\nTo exit from the game type .exit and press ENTER")
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
    description="Hello there (Woof Woof) !! Tic-Tac-Toe is fun ! But its even more fun when you play with a friend ! So come on ! Play with a friend and try to beat them in an exciting game of one of the oldest yet one of the best games of all time, Classic Tic-Tac-Toe"
  )
  embed.set_footer(text="To start a new game type .play [@mention @mention] and mention 2 player names then press ENTER\neg: .play @Bot1 @Bot2\n\nTo exit from the game type .exit and press ENTER")
  embed.set_image(url="https://st2.depositphotos.com/1024849/7268/v/600/depositphotos_72683411-stock-illustration-hand-drawn-tic-tac-toe.jpg")
  await ctx.send(embed=embed)

@client.command()
async def exit(ctx):
  global loaded_hangman
  global loaded_tictactoe
  str = ""
  if loaded_hangman : 
    client.unload_extension("cog_games.hangman")
    str = 'You have left Hangman ! To play again first load the game using .hangman'
    loaded_hangman = False
  if loaded_tictactoe : 
    client.unload_extension("cog_games.tictactoe")
    str = 'You have left Tic-Tac-Toe ! To play again first load the game using .tictactoe'
    loaded_tictactoe = False
  embed = discord.Embed(description = str)
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

keep_alive()
client.run(my_secret)
