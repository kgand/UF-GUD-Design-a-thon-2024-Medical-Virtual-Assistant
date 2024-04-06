import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
# Set up the bot
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

