from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import traceback

bot = commands.Bot(debug_guilds=[879288794560471050])
load_dotenv()
TOKEN = os.getenv('TOKEN')
print(TOKEN)

path = "./cogs"


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(error)
        await bot.get_partial_messageable(1009731664412426240).send(error)#traceback.format_exc())
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond(content="管理者限定やで", ephemeral=True)
    else: 
        await bot.get_partial_messageable(1009731664412426240).send(error)#traceback.format_exc())
        raise error


@bot.event
async def on_ready():
    print(f"Bot名:{bot.user} On ready!!")

bot.load_extension('cogs.controle')

bot.run(TOKEN)