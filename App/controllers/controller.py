from App.src.web import TickWeb
from App.index import db
from datetime import datetime , timedelta
from App.models.model import Tick


class TickController():
    def __init__(self,Name,KeyAlphaVantage):
        self.Name = Name
        self.KeyAlphaVantage = KeyAlphaVantage

    def getTick(self):
        try:
            return Tick.query.filter_by(Name=self.Name).first()
        except Exception as e:
            return e

    def getTicks(self):
        try:
            return Tick.query.all()
        except Exception as e:
            return e

    def insertTick(self):
        try:
            tickWeb = TickWeb(self.Name,self.KeyAlphaVantage)
            [Company,Sector,Subsector] = tickWeb.getStaticInfo() ; [Open,Close,Max,Min] = tickWeb.getDinamicInfo() ; Price = tickWeb.getPrice()
            Json = tickWeb.getJSON() ; Date_Json = datetime.now()
            tick = Tick(self.Name,Company,Sector,Subsector,Price,Max,Min,Open,Close,Json,Date_Json)
            db.session.add(tick)
            db.session.commit()
            return True
        except Exception as e:
            return e


    def updateTick(self):
        tick = Tick.query.filter_by(Name=self.Name).first()
        try:
            self.updateInfo(tick.Date_Updated)
            self.updateJson(tick.Date_Json)
            self.updatePrice(tick.Date_Updated)
        except Exception as e:
            return e


    def updateJson(self,date):
        dateNow = datetime.now()
        dateAtt = datetime.strftime(date,"%d/%m/%Y %H:%M:%S") + timedelta(hours=24)
        if ( dateAtt < dateNow):
            try:
                tickweb = Tick(self.Name,self.KeyAlphaVantage)
                Json = tickweb.getJSON()
                tick = Tick.query.filter_by(Name=self.Name).update(dict(Json=Json,Date_Json=datetime.now()))
                db.session.commit()
            except Exception as e:
                return e
    
    def updatePrice(self,date):
        dateNow = datetime.now()
        dateAtt = (datetime.strftime(date,"%d/%m/%Y %H:%M:%S") + timedelta(minutes=10))
        if ( dateAtt <= dateNow ):
            try:
                tickweb = TickWeb(self.Name,self.KeyAlphaVantage)
                Price = tickweb.getPrice()
                tick = Tick.query.filter_by(Name=self.Name).update(dict(Price=Price))
                db.session.commit()
            except Exception as e:
                return e
    
    def updateInfo(self,date):
        dateNow = datetime.now()
        dateAtt = f'{dateNow.strftime("%d")}/{dateNow.strftime("%m")}/{dateNow.strftime("%Y")} 18:00:00'
        if ( dateNow >= datetime.strptime(dateAtt,"%d/%m/%Y %H:%M:%S") and datetime.strptime(date,"%d/%m/%Y %H:%M:%S") <= dateAtt):
            try:
                tickWeb = TickWeb(self.name,self.KeyAlphaVantage)
                [Open,Close,Max,Min] = tickWeb.getDinamicInfo()
                print([Open,Close,Max,Min])
                tick = Tick.query.filter_by(Name=self.Name).update(dict(Open=Open,Close=Close,Max=Max,Min=Min))
                db.session.commit()
            except Exception as e:
                return e

    def __repr__(self):
        return f'{self.Name} {self.KeyAlphaVantage}'

