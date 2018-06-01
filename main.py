from api_token import get_token
import discord
from discord.ext import commands

song_url = 'https://www.youtube.com/watch?v=ZZ5LpwO-An4'

bot = commands.Bot(command_prefix='$', description='I play he man forever')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info():
    embed = discord.Embed(title="He-Man bot", description="Plays Hey Yeah Yeah by He Man", color=0x146eff)
    embed.add_field(name="Author", value="[LRAbbade](http://www.github.com/LRAbbade)")
    embed.add_field(name="Source code", value="[He_Man_Bot](http://www.github.com/LRAbbade/He_Man_Bot)")
    await bot.say(embed=embed)

@bot.command()
async def start():
    await bot.say('HEYYEYAAEYAAAEYAEYAA')

bot.run(get_token())
