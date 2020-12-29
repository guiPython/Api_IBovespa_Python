from my_app import db

class Tick (db.Model):

    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(6),unique=True)
    Company = db.Column(db.String(30))
    Sector = db.Column(db.String(15))
    Subsector = db.Column(db.String(15))
    Price = db.Column(db.Float(asdecimal=True))
    Max = db.Column(db.Float(asdecimal=True))
    Min = db.Column(db.Float(asdecimal=True))
    Open = db.Column(db.Float(asdecimal=True))
    Close = db.Column(db.Float(asdecimal=True))

    def __init__(self,Name,Company,Sector,Subsector,Price,Max,Min,Open,Close):
        self.Name = Name
        self.Company = Company
        self.Sector = Sector
        self.Subsector = Subsector
        self.Price = Price
        self.Max = Max
        self.Min = Min
        self.Open = Open
        self.Close = Close

    def __repr__(self):
        return f'<Tick {self.id}>'