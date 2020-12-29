import json
from flask import request , jsonify , Blueprint , abort
from flask.views import MethodView
from my_app import db , app
from my_app.catalog.model import Tick
from my_app.src.web import TickWeb

catalog = Blueprint('catalog',__name__)
@catalog.route('/')

class TickView(MethodView):

    def get(self,name=None,keyAlphaVantage=None):
        res = {}
        if name == None and keyAlphaVantage != None:
            ticks = Tick.query.all()
            for tick in ticks:
                res[tick.Name] = {
                    "Company"  : tick.Company,
                    "Sector"   : tick.Sector,
                    "Subsector": tick.Subsector,
                    "Price"    : str(tick.Price),
                    "Max"      : str(tick.Max),
                    "Min"      : str(tick.Min),
                    "Open"     : str(tick.Open),
                    "Close"    : str(tick.Close)
                }

        elif keyAlphaVantage != None:
                tick = Tick.query.filter_by(Name=name).first()
                if tick is None:
                    #Metodos Web para busca de Valores e propriedades da Acao
                    tickWeb = TickWeb(name,keyAlphaVantage)
                    [Company,Sector,Subsector] = tickWeb.getStaticInfo()
                    [Open,Close,Max,Min] = tickWeb.getDinamicInfo()
                    Price  = tickWeb.getPrice()

                    #Metodos do Banco para persistir os dados
                    tick = Tick(Name=name,Company=Company,Sector=Sector,Subsector=Subsector,Price=Price,Max=Max,Min=Min,Close=Close,Open=Open)
                    db.session.add(tick)
                    db.session.commit()
                res[tick.Name] =  {
                        "Company"  : tick.Company,
                        "Sector"   : tick.Sector,
                        "Subsector": tick.Subsector,
                        "Price"    : str(tick.Price),
                        "Max"      : str(tick.Max),
                        "Min"      : str(tick.Min),
                        "Open"     : str(tick.Open),
                        "Close"    : str(tick.Close)
                        }
        else: abort(404)
        #Resposta da Api 
        return jsonify(res)
        

tick_view = TickView.as_view('tick_view')

app.add_url_rule(
    '/tick/<string:keyAlphaVantage>', view_func = tick_view, methods = ['GET']
)

app.add_url_rule(
    '/tick/<string:name>/<string:keyAlphaVantage>' , view_func = tick_view , methods = ['GET']
)