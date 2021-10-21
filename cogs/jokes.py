import discord
from discord.ext import commands
import pyjokes

class jokes(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Joke is online")

  @commands.command()
  async def joke(self,ctx):
    joke = pyjokes.get_joke(language="en",category="all")
    embed = discord.Embed(description=joke)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(jokes(client))
