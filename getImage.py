import urllib.request
#<img src="https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpopamie19f0Ob3Yi5FvISJkJKKkPj6NbLDk1RC68phj9bN_Iv9nGu4qgE7Nnf3LISddw5taAzQ8lm6xOq9gZTpuZ6fyXA3syIltHffnxbkhxEYOLZtm7XAHgXm-xFt/360fx360f" alt="">
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def ConvertToList(string, parse):
	li = list(string.split(parse))
	return(li)
						
def getImage() :
	request_url = urllib.request.urlopen('https://steamcommunity.com/market/listings/730/M4A1-S%20%7C%20Night%20Terror%20%28Field-Tested%29')
	with request_url as response:
	  html_response = response.read()
	  encoding = response.headers.get_content_charset('utf-8')
	  decoded_html = html_response.decode(encoding)
	print(ConvertToList(ConvertToList(ConvertToList(ConvertToList(decoded_html, '<div id="largeiteminfo">')[0], '<div class="market_listing_largeimage">')[1], '<img src="')[1], '" alt="" />')[0])