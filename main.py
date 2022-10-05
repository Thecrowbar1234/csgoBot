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
async def searchMarket(ctx, condition, statTrakAndSouvenir, weapon, *args) :
	#ddddd
	if int(statTrakAndSouvenir) == 1 :
		print("true")
		search = "https://steamcommunity.com/market/listings/730/StatTrak™%20"
	elif int(statTrakAndSouvenir) == 2:
		search = "https://steamcommunity.com/market/listings/730/Souvenir%20"
	else :
		search ="https://steamcommunity.com/market/listings/730/"

	item = searchMod.replaceWeaponName(weapon)[1] + " | "
	print(search)
	#if statTrak == 1 :
	#	search = search + "StatTrak™%20"
	search = search + searchMod.replaceWeaponName(weapon)[0] + "%7C%20"
	#%28Factory%20New%29
	print(search)
	for word in args :
		search = search + word + "%20"
		item = item + word + " "
	link = search + searchMod.replaceWeaponWear(condition)[0]
	item = item + searchMod.replaceWeaponWear(condition)[1]
	print(link)
	price = steam.get_csgo_item(item, currency='USD')
	print(item)
	print(price)
	message = item + " is currently at a price " + price['lowest_price'] + "\n" + link
	await ctx.channel.send(message)

@client.command()
async def test(ctx, weapon) :
	print(searchMod.replaceWeaponName(weapon))

client.run(discordToken)