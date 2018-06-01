import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='I play he man forever')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="He-Man bot", description="Plays Hey Yeah Yeah by He Man", color=0x146eff)
    embed.add_field(name="Author", value="[LRAbbade](http://www.github.com/LRAbbade)")
    embed.add_field(name="Source code", value="[He_Man_Bot](http://www.github.com/LRAbbade/He_Man_Bot)")
    await ctx.send(embed=embed)
