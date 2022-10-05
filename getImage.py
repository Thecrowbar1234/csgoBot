import urllib.request
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def ConvertToList(string, parse):
	li = list(string.split(parse))
	return(li)
						
def getImage(url) :
	#to prevent error, remove StatTrak™%20 or Souvenier%20 from url
	request_url = urllib.request.urlopen(url)
	with request_url as response:
	  html_response = response.read()
	  encoding = response.headers.get_content_charset('utf-8')
	  decoded_html = html_response.decode(encoding)
	return ConvertToList(ConvertToList(ConvertToList(ConvertToList(decoded_html, '<div id="largeiteminfo">')[0], '<div class="market_listing_largeimage">')[1], '<img src="')[1], '" alt="" />')[0]