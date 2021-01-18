import requests
import bs4

class TickWeb():

    def __init__(self,Name,KeyAlphaVantage):
        self.Name = Name
        self.KeyAlphaVantage = KeyAlphaVantage

    def getPrice(self):
        data = requests.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{self.Name}.SA')
        price = data.json()['chart'] ['result'] [0] ['meta'] ['regularMarketPrice']
        return float(price)
    
    def getStaticInfo(self):
        data = requests.get(f"https://statusinvest.com.br/acoes/{self.Name}")
        soup = bs4.BeautifulSoup(data.text,"html.parser")
        Company = soup.find('h1',{'class':'lh-4'})['title']
        Sector = soup.find('div',{'class':'info pr-md-2'}).find("strong",{'class':'value'}).text
        Subsector = soup.find('div',{'class':'pl-md-2'}).findAll("strong",{'class':'value'})[0].text
        return [Company,Sector,Subsector]

    def getDinamicInfo(self):
        data = requests.get(f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.Name}.SAO&apikey={self.KeyAlphaVantage}")
        res = data.json()['Global Quote']
        return [float(x) for x in [res['02. open'] , res['08. previous close'], res['03. high'] , res['04. low']]]

    def getJSON(self):
        data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.Name}.SAO&outputsize=full&apikey={self.KeyAlphaVantage}")
        return data.json()
