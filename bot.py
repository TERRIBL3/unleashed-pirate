import os

from discord.errors import Forbidden
from discord.ext.commands import Bot

bot = Bot(command_prefix='%')
TOKEN = os.environ.get('TOKEN')


@bot.event
async def on_ready():
    print('Bot ready!')
    print(f'Logged in as @{bot.user.name}#{bot.user.discriminator} ({bot.user.id})\n')


@bot.command()
async def send(ctx, channel_id, *, content):
    try:
        channel = bot.get_channel(int(channel_id[2:-1]))
        title, link = content.split('|')
    except ValueError:
        return await ctx.send('There is a syntax error!')

    try:
        return await channel.send(f'**{title}**\n\n{link}')
    except Forbidden:
        return await ctx.send("I can't send messages on that channel!")


bot.run(TOKEN) if TOKEN else print('TOKEN environment variable not set!')
