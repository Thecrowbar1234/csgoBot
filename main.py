import discord
import steammarket as steam
from discord.ext import commands
import os
import searchFunction
discordToken = os.environ['DiscordToken']

client = commands.Bot(command_prefix='c$', intents=discord.Intents.all())

@client.event
async def on_ready() :
  print("Bot is ready")

#, weapon, wear, statTrak, Souvenir, *args
@client.command()
async def searchMarket(ctx, weapon) :
	search ="https://steamcommunity.com/market/listings/730/"
	#print(search)
	#if statTrak == 1 :
	#	search = search + "StatTrak™%20"
	search = search + searchFunction.replaceWeaponName(weapon) + "%7C%20"
	print(search)
	#if args.length > 1 :
	#	search = search + args[0] + "%20"
	item = steam.get_csgo_item("AK-47 | Frontside Misty (Factory New)", currency='USD')
	print(item)

@client.command()
async def test(ctx, weapon) :
	print(searchFunction.replaceWeaponName(weapon))

client.run(discordToken)