import discord
import steammarket as steam
from discord.ext import commands
import os
import searchFunction as searchMod
discordToken = os.environ['DiscordToken']

client = commands.Bot(command_prefix='c$', intents=discord.Intents.all())

@client.event
async def on_ready() :
  print("Bot is ready")

#, weapon, wear, statTrak, Souvenir, *args
@client.command()
async def searchMarket(ctx, weapon, condition, statTrakAndSouvenir, *args) :
	if int(statTrakAndSouvenir) == 1 :
		print("true")
		search = "https://steamcommunity.com/market/listings/730/StatTrak™%20"
	elif int(statTrakAndSouvenir) == 2:
		search = "https://steamcommunity.com/market/listings/730/Souvenir%20"
	else :
		search ="https://steamcommunity.com/market/listings/730/"
	print(search)
	#if statTrak == 1 :
	#	search = search + "StatTrak™%20"
	search = search + searchMod.replaceWeaponName(weapon) + "%7C%20"
	#%28Factory%20New%29
	print(search)
	for word in args :
		search = search + word + "%20"
	link = search + searchMod.replaceWeaponWear(condition)
	print(link)
	item = steam.get_csgo_item("AK-47 | Frontside Misty (Factory New)", currency='USD')
	print(item)

@client.command()
async def test(ctx, weapon) :
	print(searchMod.replaceWeaponName(weapon))

client.run(discordToken)