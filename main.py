import discord
import steammarket as steam
from discord.ext import commands
import os
import searchFunction as searchMod
import getImage
discordToken = os.environ['DiscordToken']

client = commands.Bot(command_prefix='c$', intents=discord.Intents.all())

@client.event
async def on_ready() :
  print("Bot is ready")

#, weapon, wear, statTrak, Souvenir, *args
@client.command()
async def searchMarket(ctx, condition, statTrakAndSouvenir, weapon, *args) :
	imgQuery = "https://steamcommunity.com/market/listings/730/"
	if int(statTrakAndSouvenir) == 1 :
		search = "https://steamcommunity.com/market/listings/730/StatTrak™%20"
	elif int(statTrakAndSouvenir) == 2:
		search = "https://steamcommunity.com/market/listings/730/Souvenir%20"
	else :
		search ="https://steamcommunity.com/market/listings/730/"

	item = searchMod.replaceWeaponName(weapon)[1] + " | "
	#if statTrak == 1 :
	#	search = search + "StatTrak™%20"
	search = search + searchMod.replaceWeaponName(weapon)[0] + "%7C%20"
	imgQuery = imgQuery + searchMod.replaceWeaponName(weapon)[0] + "%7c%20"
	#%28Factory%20New%29
	for word in args :
		imgQuery = imgQuery + word + "%20"
		search = search + word + "%20"
		item = item + word + " "
	link = search + searchMod.replaceWeaponWear(condition)[0]
	imgQuery = imgQuery + searchMod.replaceWeaponWear(condition)[0]
	item = item + searchMod.replaceWeaponWear(condition)[1]
	price = steam.get_csgo_item(item, currency='USD')
	message = "Currently at a price of " + price['lowest_price'] + "."
	embed = discord.Embed(title=item, url=link, description=message, color=0xffffff)
	embed.set_image(url=getImage.getImage(imgQuery))
	await ctx.channel.send(embed=embed)

@client.command()
async def test(ctx) :
	getImage.getImage()

client.run(discordToken)