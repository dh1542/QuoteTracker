import bs4
from bs4 import BeautifulSoup
import urllib3
import requests

def validate(StockCode):
	code = StockCode.replace(" ", "")
	code = code.upper()
	return code 

def getQuote(StockCode):
	url = requests.get('https://finance.yahoo.com/quote/' + StockCode +'?p=' + StockCode)
	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
	price = price.replace(",", "")
	return float(price)
	






stockCode = validate(input("Stocke Code: "))

oldPrice = 0

while True:
	price = getQuote(stockCode)
	if(oldPrice == price):
		print(str(price) + "$")
		print("=")
	elif(oldPrice > price):
		print(str(price) + "$")
		print("-")
	else:
		print(str(price) + "$")
		print("+")

	oldPrice = price 

	







