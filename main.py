import random
import discord
from discord.ext import commands

config = {
    'token': 'your-token',
    'prefix': '$',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
@commands.has_role("Хозяин")
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

bot.run(config['token'])
