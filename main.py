import discord
from discord.ext import commands
from datetime import datetime, timedelta

TOKEN = "MTUxOTA4NjI3MTQwMDUwOTYzMg.GRL8kU.8G3l8fHbfx1OSydOR_bOSO1wir4nglxV7lWwIc"

START_REAL = datetime(2026, 6, 29, 18, 0)
START_GAME = datetime(1280, 1, 1)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def date(ctx):
    now = datetime.now()

    # seconds since start
    seconds_passed = (now - START_REAL).total_seconds()

    # 1 real day = 365 in-game days
    game_days = seconds_passed / 86400 * 365

    game_date = START_GAME + timedelta(days=game_days)

    formatted = game_date.strftime("%d %B %Y")

    await ctx.send(f"📅 Current server date: {formatted}")

bot.run(TOKEN)
