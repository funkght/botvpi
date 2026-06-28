import discord # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='!', intents=intents) 

# С помощью декоратора создаём первую команду
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('MTUyMDg3NjU1MDc5MzMzNDg3NA.Gq5Ob4.8E8ShhLeR2J2ebB-ILNJR1YSqPtSQa9Yf70SVQ')
