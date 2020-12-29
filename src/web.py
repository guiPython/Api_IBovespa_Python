import requests
import bs4

class Tick():

    def __init__(self,Name):
        self.Name = Name

    def getPrice(self):
        data = requests.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{self.Name}.SA?region=US&lang=en-US&includePrePost=false&interval=2m&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance')
        price = data.json()['chart'] ['result'] [0] ['meta'] ['regularMarketPrice']
        return price
    
    def getStaticInfo(self):
        data = requests.get(f"https://statusinvest.com.br/acoes/{self.Name}")
        soup = bs4.BeautifulSoup(data.text,"html.parser")
        Company = soup.find('h1',{'class':'lh-4'})['title']
        Sector = soup.find('div',{'class':'info pr-md-2'}).find("strong",{'class':'value'}).text
        Subsector = soup.find('div',{'class':'pl-md-2'}).findAll("strong",{'class':'value'})[0].text
        return [Company,Sector,Subsector]

    def getDinamicInfo(self):
        return ...


acao = Tick('itub4')
print(acao.getStaticInfo())
print(acao.getPrice())