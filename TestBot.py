import discord
from discord.ext import commands

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def hello(ctx):
     await ctx.send("Hi")

client.run ("Nzg4NDAwNDYyNjYzMTIyOTU1.X9i9Jg.teJZtHKh7DygWM7WpbHnrOUbfZ8")     