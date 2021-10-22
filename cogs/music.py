import discord
from discord.ext import commands

class Music(commands.Cog):

  def __init__(self , client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("music in online")

  @commands.command()
  async def play_music(self,ctx):
    await ctx.send("playing music")


def setup(client):

  client.add_cog(Music(client))