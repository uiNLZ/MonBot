import os
import discord
from discord.ext import commands

TOKEN = os.getenv("MTUzNDM3MjEzMjc3ODI3ODk4Mw.GNyakq.P-WJB2tqNAZlNeAMbgCXox6yI95AK5oFkbJeNk")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

bot.run("MTUzNDM3MjEzMjc3ODI3ODk4Mw.GNyakq.P-WJB2tqNAZlNeAMbgCXox6yI95AK5oFkbJeNk")