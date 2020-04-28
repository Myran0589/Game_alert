import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import colorsys

client = commands.Bot(command_prefix='?')
client.remove_command('help')

@client.event
async def on_ready():
    print('online')
    print('----------')
    
	    
@client.command()
async def q(ctx,que: str):
	     embed=discord.Embed(title="", description=f"``Question {que} Is Comming On 📱``", color=discord.Color.red())
	     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/702945721610928219/704569122956247131/700566617456902146.gif")
	     embed.set_image(url="https://cdn.discordapp.com/attachments/691596509539598379/692639381109997618/HmjViJc.gif")
	     embed.set_footer(text="©Server Manager | Myran#0001")
	     await ctx.send(content="@everyone",embed=embed)

client.run('Bot token')
