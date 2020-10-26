import sys, discord
from discord.ext import commands
import mysql.connector
from datetime import datetime

sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="discord_logger"
    )
cursor = sql.cursor()
print(sql)


client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    print('logging servers')

@client.event
async def on_message(message):
    sql_msg = "INSERT INTO logged_messages (guild, time_stamp, discord_username, discord_id, discord_message) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.guild.name}", datetime.today().strftime("%Y-%m-%d"), f"{message.author}", f"{message.author.id}", f"{message.content}")
    cursor.execute(sql_msg, val)
    sql.commit()
    print("Logged Message :D")

client.run("PUT YOUR TOKEN HERE", bot=False)
