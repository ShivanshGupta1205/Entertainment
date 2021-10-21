import discord
from discord.ext import commands

class Music(commands.Cog):

  def __init__(self , client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("\nThe file music.py has been loaded")

  @commands.command()
  async def play_music(self,ctx):
    await ctx.send("> We will be playing now")


def setup(client):

  client.add_cog(Music(client))