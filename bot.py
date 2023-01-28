# website: http://stoketech.club - email: stoke@stoketech.club
import discord
from course_anaconda import *
from private.config import token

print("...imports successful...")
working = False
file_name = token
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} reporting for duty Sir! ')

# SET OUR VARIABLES FOR EASIER DISPLAY IN BOT...
overview_01 = (conda_course + '\n\n' + outline_1)
overview_02 = (conda_course + '\n\n' + outline_2)
overview_03 = (conda_course + '\n\n' + outline_3)
overview_04 = (conda_course + '\n\n' + outline_4)
overview_05 = (conda_course + '\n\n' + outline_5)
overview_06 = (conda_course + '\n\n' + outline_6)
overview_07 = (conda_course + '\n\n' + outline_7)
lesson1 = (conda_course + '\n' + lesson_1)
lesson2 = (conda_course + '\n' + lesson_2)
lesson3 = (conda_course + '\n' + lesson_3)
lesson4 = (conda_course + '\n' + lesson_4)
lesson5 = (conda_course + '\n' + lesson_5)
lesson6 = (conda_course + '\n' + lesson_6)
lesson7 = (conda_course + '\n' + lesson_7)

client.run(token)