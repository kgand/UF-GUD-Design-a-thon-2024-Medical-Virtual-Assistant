import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random
from dotenv import load_dotenv
import webbrowser
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

stressed_words = ["stressed", "too much work", "too busy", "no time", "everything sucks",
                  "I hate everything", "I have so much", "I have so much to do", "I have no time",
                  "I will never get this done", "Why is there so much work", "I can't even sleep", "I literally can't sleep", "I hate this",
                  "why always me", "why me", "so much work", "so busy", "don't have time for anything", "im buried", "i'm buried",
                  "i literally cant sleep", "Overwhelmed", "Under pressure", "Exhausted", "Burnt out",
                  "Swamped", "Frazzled", "Stretched thin", "On edge", "At my limit", "On the brink",
                  "Stressed out", "On the verge", "Feeling maxed out", "Tapped out", "Flooded with work",
                  "Suffocating under tasks", "At the breaking point", "Drowning in responsibilities",
                  "Feeling suffocated", "In over my head", "Barely hanging on", "Feeling overwhelmed and hopeless"]
suicidal_words = ["I want to die", "I wanna die", "I actually want to die", "I actually wanna die", 
                  "I can't do this", "I actually want to die rn", "I actually wanna die rn",
                  "I cant do this", "kill myself", "kms", "end my life", "I dont want to wakeup",
                  "goodbye world", "I dont want to live", "I never want to wake up", "this is the end", "i cant do this anymore",
                  "I dont want to be alive", "i dont wanna be alive", "i can't do this anymore", "i can't keep going", "i cant go on anymore",
                  "I feel hopeless", "Life isn't worth living", "I'm a burden", "I want to disappear",
                  "I can't go on like this", "There's no point", "I'm tired of living", "I feel empty inside",
                  "I wish I were dead", "I feel like giving up", "I'm better off dead", "I'm in too much pain",
                  "I feel trapped", "I'm considering ending it all", "I feel worthless", "I'm tired of struggling",
                  "I don't see a way out", "I'm done with everything", "I'm at the end of my rope", "I'm ready to end it"]

# Empathetic and uplifting messaging
suicidal_message_dm = discord.Embed(
    color=0x6A5ACD,  # New color: Lavender
    title='MediPal is here to support you, my friend! 💜',
    description='Howdy,\n\nWe noticed that you might be struggling with some difficult thoughts or feelings. Please know that you are not alone in this journey. Your life is precious, and we want you to know that there are always alternatives, even when the path ahead seems darkest.\n\nWe have included some helpful resources below that you might find useful. Take your time to explore them, and do not hesitate to reach out if you need someone to talk to. You matter, and we are here to support you every step of the way.'
)

suicidal_message_dm.set_author(name='MediPal', icon_url='https://i.imgur.com/4S06GQP.png')
suicidal_message_dm.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqIVgEg4VfJbf1TZL4iQXptkoJDRg7wyYeP1Qcr8mfyA&')
suicidal_message_dm.add_field(name='National Suicide Prevention Lifeline', value='**Call:** 988\n**Website:** https://suicidepreventionlifeline.org/')
suicidal_message_dm.add_field(name='Crisis Text Line', value='**Text:** HOME to 741741\n**Website:** https://www.crisistextline.org/')
suicidal_message_dm.add_field(name='Finding Hope and Healing', value='[Effective Strategies for Finding Hope and Healing](https://www.myflr.org/6-effective-strategies-to-find-hope-and-healing/)')
suicidal_message_dm.set_footer(text="React with 👍 if you need assistance, 🗣️ to open MediPal, or 👎 if you're not ready yet.")

new_member_dm = discord.Embed(
    color=0x6A5ACD,
    title='Welcome to the MediChat community, friend! 🤗',
    description='Hello there, I am MediPal, and I am here to provide a supportive and caring environment for everyone. My goal is to help identify and support any individual who might be struggling with their mental health, whether it is stress, anxiety, or something more serious.\n\nFeel free to reach out to me anytime you need a listening ear or some helpful resources. I will do my best to provide a safe space for you to express yourself and find the support you need. Together, let us build a community of kindness, understanding, and compassion.'
)
new_member_dm.set_author(name='MediPal', icon_url='https://i.imgur.com/4S06GQP.png')
new_member_dm.set_thumbnail(url='https://i.imgur.com/uzFQ57u.png')
new_member_dm.add_field(name='Get to know MediPal', value='I am an AI assistant created to support the mental health and well-being of our community. I am always here to listen, provide resources, and offer a compassionate voice when you need it most.')

stressed_message_dm = discord.Embed(
    color=0x6A5ACD,
    title='MediPal is here to support you, my friend! 🌱',
    description='Howdy,\n\nWe noticed that you might be feeling a bit stressed lately. That is totally understandable, especially with the demands of school and life. Just remember, it is okay to take a break and focus on your self-care. You are doing the best you can, and that is what matters.\n\nBelow, you will find some resources that might help you manage stress and find a little more balance. Take a look, and do not hesitate to reach out if you need anything else. We are here for you, always.'
)
stressed_message_dm.set_author(name='MediPal', icon_url='https://i.imgur.com/4S06GQP.png')
stressed_message_dm.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRu5E0PahjL-kd7K89-gDhtNaCOHULP8rVosFqgdhmew&s')
stressed_message_dm.add_field(name='Mindfulness Meditation for Stress Relief', value='[Headspace - Guided Meditation for Stress](https://www.headspace.com/meditation/stress)')
stressed_message_dm.add_field(name='Understanding and Overcoming Anxiety', value='[Verywellmind - Overcoming Anxiety](https://www.verywellmind.com/overcoming-anxiety-2584196)')
stressed_message_dm.add_field(name='5-Minute Yoga Routine for Relaxation', value='[5-Minute Yoga Routine for Relaxation](https://www.youtube.com/watch?v=nvFm30ZAZRY)')
stressed_message_dm.add_field(name='Journaling Prompts for Emotional Wellbeing', value='[Journaling Prompts for Mental Health](https://www.charliehealth.com/post/20-journaling-prompts-for-mental-health)')
stressed_message_dm.set_footer(text="React with 👍 if you need assistance, 🗣️ to open MediPal, or 👎 if you're not ready yet.")
# On ready event
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

# On new member join event
@bot.event
async def on_member_join(member):
    await member.send(embed=new_member_dm)

# Check loop
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    suicidal_word_found = False
    stressed_word_found = False

    for word in suicidal_words:
        if word.lower() in message.content.lower():
            suicidal_word_found = True
            break

    if not suicidal_word_found:
        for word in stressed_words:
            if word.lower() in message.content.lower():
                stressed_word_found = True
                break

    if suicidal_word_found:
        try:
            msg = await message.author.send(embed=suicidal_message_dm)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
            await msg.add_reaction('🗣️')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['👍', '👎', '🗣️']

            reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == '👍':
                await message.author.send("Thank you for letting us know. Please remember, you are not alone.")
                channel = bot.get_channel(1226278093279465565)  # Replace with the channel ID for bot notifications
                await channel.send(f"{message.author.mention} has expressed thoughts that may signal a need for support. Please reach out.")
            elif str(reaction.emoji) == '🗣️':
                await message.author.send("Open MediPal")
                webbrowser.open('http://127.0.0.1:5000')
            else:
                await message.author.send("We are here if you change your mind. Do not hesitate to reach out.")

        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, I cannot direct message you. Please enable direct messages from server members.")
            
    elif stressed_word_found:
        try:
            msg = await message.author.send(embed=stressed_message_dm)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
            await msg.add_reaction('🗣️')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['👍', '👎', '🗣️']

            reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == '👍':
                await message.author.send("Feel free to share your thoughts with us. We are here to listen and support you.")
                channel = bot.get_channel(1226278093279465565)
                await channel.send(f"{message.author.mention} has expressed feelings of stress. Please check in and offer support.")
            elif str(reaction.emoji) == '🗣️':
                await message.author.send("Opening MediPal!")
                webbrowser.open('http://127.0.0.1:5000')
            else:
                await message.author.send("We are here if you change your mind. Do not hesitate to reach out.")
        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, I cannot direct message you. Please enable direct messages from server members.")

    # Check for commands
    if message.content.startswith('!hotline'):
        embed = discord.Embed(
            title = 'The National Suicide Prevention Lifeline',
            description="**Call:** 988\n**Website:** https://suicidepreventionlifeline.org/",
            color=0x6A5ACD
        )
        embed.set_image(url="https://namica.org/wp-content/uploads/2020/09/988-social-graphic-2.png")
        await message.channel.send(embed=embed)

    if message.content.startswith('!hi'):
        embed = discord.Embed(
            title = 'Hello there, I am MediPal! 👋',
            description="I am here to support you and your mental health. Feel free to reach out anytime you need a listening ear or some helpful resources.",
            color=0x6A5ACD
        )
        embed.set_image(url="https://www.icegif.com/wp-content/uploads/2022/05/icegif-1059.gif")
        await message.channel.send(embed=embed)

# Run the bot
bot.run(TOKEN)