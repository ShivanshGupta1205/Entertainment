import discord
from discord.ext import commands
import random
from words import word_list


word = random.choice(word_list)
word_completed = '#' * len(word)
guessed = False
guessed_letters = []
guessed_words = []
tries = 6
playing = False


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   \-\-\-\-\-\-\-
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   \-\-\-\-\-\-\-
                   |\t|
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

async def checkMSG(ctx,guess):
    guess = guess.lower()
    global tries
    global guessed_letters
    global guessed_words
    global guessed
    global word
    global word_completed
    str = ""

    if len(guess) == 1 and guess.isalpha():

      if guess in guessed_letters:
        str = f"You already guessed the letter {guess}!"

      elif guess not in word:
        str = f"Oops! '{guess}' is not in the word!"
        tries -= 1
        guessed_letters.append(guess)

      else:
        guessed_letters.append(guess)

        var = word_completed
        word_completed = ""
        for i in range(len(word)):
          if word[i] == guess:
            word_completed += guess
          elif var[i] != '#':
            word_completed += var[i]
          else:
            word_completed += '#'

        # word_as_list = list(word_completed)
        # indices = [i for i, letter in enumerate(word) if letter == guess]

        # for index in indices:
        #   word_as_list[index] = guess
        # word_completed = "".join(word_as_list)

        if "#" not in word_completed:
          guessed = True
          await word_guessed(ctx)
        str = f"Good job ! '{guess}' is in the Word !"

    elif len(guess) == len(word) and guess.isalpha():

      if guess in guessed_words:
        str = f"You already guessed the word {guess}"

      elif guess != word:
        str = "It is not the word"
        tries -= 1
        guessed_words.append(guess)

      else:
        guessed = True
        word_completed = word
        await word_guessed(ctx)

    else:
      str = "Not a valid guess !"

    
    # this is causing multiple outputs
    return str


async def word_guessed(ctx):

  embed = discord.Embed(title="HANGMAN", description="Voila ! You have won the game ! Let's play again shall we ? Woof !")
  embed.set_footer(text="To play again type .play and press ENTER")
  await ctx.send(embed = embed)
  # this is causing problems !
  #reset()


def reset():
  global tries
  global guessed_letters
  global guessed_words
  global guessed
  global word
  global word_completed
  global playing
  word = random.choice(word_list)
  word_completed = '* ' * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  playing = False

  

class hangman(commands.Cog):

  #init fuction
  def __init__(self,client):
    self.client = client

  # on_ready function !! Doesnt word for some reason !!
  @commands.Cog.listener()
  async def on_ready(self):
    print('hangman is online')

  # command to see hangman rules 
  # @commands.command()
  # async def hangman(self,ctx):
  #   embed = discord.Embed(
  #     title='HANGMAN', 
  #     description="Hello there (Woof Woof) !! Lets test your guessing skills and see if you can crack the word (that I choose) in under 6 moves !!\n\n PS: I'm pretty competitive so I wont make it easy! Gear Up. Woof Woof !\n\nRULES:\n\n1. I'll choose a random word.\n2. You have to choose an alphabet or a word.\n If you choose correctly I'll fill it, else you HANG !\n\n! ALL THE BEST ! WOOF WOOF !\n\n"
  #   )
  #   embed.set_footer(text="To start a new game type .play and press ENTER")
  #   await ctx.send(embed=embed)

  #command to play hangman !
  @commands.command()
  async def play(self,ctx):
    global playing
    global word_completed
    global word
    print(word)
    print(word_completed)
    if not playing:
      str = f'Your word is {len(word)} letters long ! Start Guessing !\n\n{display_hangman(tries)}'
      embed = discord.Embed(
        title='LETS PLAY HANGMAN', 
        description = str
      )
      embed.set_footer(text="To start playing type .g [your guess] and press ENTER")
      await ctx.send(embed=embed)
      playing = True
    else:
      await ctx.send("> A game is already being played ! finish that first !")

  #command to end the current game
  @commands.command()
  async def end(self,ctx):
    reset()
    await ctx.send("> Thank You for playing ! Hope to see you again soon ! Woof Woof ")

  #command to guess word or letter
  @commands.command()
  async def g(self,ctx,message):

      global playing
      global guessed
      global tries
      global word
      global word_completed

      if playing:
        str = await checkMSG(ctx,message)
        if not guessed and tries>0:
          #if not guessed:
          embed = discord.Embed(title="HANGMAN" , description = str + "\n\n" + display_hangman(tries))
          embed.set_footer(text=f"You have {tries} tries left (Woof) !")
          await ctx.send(embed = embed)
          await ctx.send("> Word : " + word_completed)

        elif not guessed and tries==0:
          embed = discord.Embed(title="HANGMAN" , description = display_hangman(tries))
          embed.set_footer(text=f"Sorry the game is over ! You have 0 tries left ! The word was {word} ! Play Again ! Let's see if you can win this time ! Woof Woof")
          await ctx.send(embed = embed)
          reset() 

        elif guessed:
          reset()     
      else:
        await ctx.send("> Start a New Game first !")



def setup(client):
  client.add_cog(hangman(client))
