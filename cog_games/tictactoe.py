# gameover -> newgame

import discord
from discord.ext import commands
import random


gameOver  = True
count = 0
board = []
player1 = ""
player2 = ""
turn = ""

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


#function to print the board at any condition
async def print_board(ctx):
  line = ""
  for x in range(len(board)):
    if x == 2 or x == 5 or x == 8:
      line += " " + board[x]
      await ctx.send(line)
      line = ""
    else:
      line += " " + board[x]

def checkWinner(mark):
  global gameOver
  global board
  global winningConditions
  for condition in winningConditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      gameOver = True

def reset():
  global count
  global player1
  global player2
  global turn
  global gameOver
  global board
  player1 = ""
  player2 = ""
  turn = ""
  gameOver  = True
  count = 0
  board = []


# cog declaration
class tictactoe(commands.Cog):

  # init function
  def __int__(self,client):
    self.client = client

  # on ready function
  @commands.Cog.listener()
  async def on_ready(self):
    print("Tictactoe is online")

  #command to see tictactoe rules 
  # @commands.command()
  # async def tictactoe(self,ctx):
  #   embed = discord.Embed(
  #     title='TIC-TAC-TOE', 
  #     description="Tic-Tac-Toe is fun ! But its even more fun when you play with a friend ! So come on ! Play with a friend and try to beat them in an exciting game of one of the oldest yet one of the best ganes of all time, CLassic Tic-Tac-Toe\n\n"
  #   )
  #   embed.set_footer(text="To start a new game type .p [@mention @mention] and mention 2 player names then press ENTER\neg: .p @Bot1 @Bot2")
  #   await ctx.send(embed=embed)


  #function to play tictactoe
  @commands.command()
  async def play(self,ctx,p1:discord.Member,p2:discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    global board

    if gameOver:
      board = [
      ":white_large_square:", ":white_large_square:", ":white_large_square:",
      ":white_large_square:", ":white_large_square:", ":white_large_square:",
      ":white_large_square:", ":white_large_square:", ":white_large_square:"
      ]
      gameOver = False
      await print_board(ctx)
      player1 = p1
      player2 = p2
      num = random.randint(1,2)
      turn = player1 if num==1 else player2
      await ctx.send("> It is <@" + str(turn.id) + ">'s turn.")
    else:
      embed = discord.Embed(description="A game is already in progress! Finish it before starting a new one.")
      embed.add_footer(text="To end the current game type .end\nTo start a new game type .play @mention @mention")
      await ctx.send(embed=embed)

  #command to play a turn 
  @commands.command()
  async def place(self,ctx,pos:int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    str = ""

    if not gameOver:
      if turn == ctx.author:
        mark = ":regional_indicator_x:" if turn==player1 else ":o2:"
        if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
          board[pos - 1] = mark
          count += 1
          await print_board(ctx)
          checkWinner(mark)

          if gameOver == True:
            str = f"Great Job ! {ctx.author} wins!"
            reset()
          elif count >= 9:
            gameOver = True
            str = "It's a tie ! Good game guys ! Go on play another (woof) !"
            reset()

          turn = player2 if turn==player1 else player1

        elif pos<0 or pos>10:
          str = "Be sure to choose an integer between 1 and 9 (inclusive)"

        elif board[pos - 1] != ":white_large_square:" :
          str = "> Be sure to choose an unmarked tile !"

      else:
        str = "It is not your turn."
    else:
      await ctx.send("> Please start a new game using the .play [@mention @mention] command.")

    embed = discord.Embed(description=str)
    await ctx.send(embed=embed)

  ##command to end the game
  @commands.command()
  async def end(self,ctx):
    reset()
    await ctx.send("> Thank You for playing ! Hope to see you again soon ! Woof Woof ")
   
  #if any play error occurs
  @play.error
  async def tictactoe_error(self,ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("> Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
      await ctx.send("> Please make sure to mention/ping players (ie. <@688534433879556134>).")

  #if any place error occurs
  @place.error
  async def place_error(self,ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("> Please enter a position you would like to mark.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send("> Please make sure to enter an integer.")


def setup(client):
  client.add_cog(tictactoe(client))


  