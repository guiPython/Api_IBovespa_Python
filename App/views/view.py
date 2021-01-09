import json
from flask import request , jsonify , Blueprint , abort
from flask.views import MethodView
from App.index import db , app
from time import sleep
from App.src.web import TickWeb
from App.controllers.controller import TickController


tick = Blueprint('tick',__name__)
@tick.route('/')

class TickView(MethodView):

    def get(self,name=None,keyAlphaVantage=None):
        res = []

        if name == None and keyAlphaVantage != None:
            controller = TickController("",keyAlphaVantage)
            ticks = controller.getTicks()
            for tick in ticks:
                controller = TickController(tick.Name,keyAlphaVantage)
                controller.updateTick()
            ticks = controller.getTicks()
            for tick in ticks:
                res.append({
                    "Nome" : tick.Name,
                    "Values" : {
                        "Company"  : tick.Company,
                        "Sector"   : tick.Sector,
                        "Subsector": tick.Subsector,
                        "Price"    : f'{tick.Price:.2f}'.replace(".",","),
                        "Max"      : f'{tick.Max:.2f}'.replace(".",","),
                        "Min"      : f'{tick.Min:.2f}'.replace(".",","),
                        "Open"     : f'{tick.Open:.2f}'.replace(".",","),
                        "Close"    : f'{tick.Close:.2f}'.replace(".",","),
                        "Date_Updated" : tick.Date_Updated
                        }
                })

        elif keyAlphaVantage != None:
            controller = TickController(name,keyAlphaVantage)
            tick = controller.getTick()
            if tick is None:
                controller.insertTick()
                tick = controller.getTick()
            else:
                controller.updateTick()
                tick = controller.getTick()
            res.append({
                "Nome" : tick.Name,
                "Values" : {
                    "Company"  : tick.Company,
                    "Sector"   : tick.Sector,
                    "Subsector": tick.Subsector,
                    "Price"    : f'{tick.Price:.2f}'.replace(".",","),
                    "Max"      : f'{tick.Max:.2f}'.replace(".",","),
                    "Min"      : f'{tick.Min:.2f}'.replace(".",","),
                    "Open"     : f'{tick.Open:.2f}'.replace(".",","),
                    "Close"    : f'{tick.Close:.2f}'.replace(".",","),
                    "Date_Updated" : tick.Date_Updated
                    }
                })

        else: abort(404)

        return jsonify(res)

tick_view = TickView.as_view('tick_view')

app.add_url_rule(
    '/tick/<string:keyAlphaVantage>', view_func = tick_view, methods = ['GET']
)

app.add_url_rule(
    '/tick/<string:name>/<string:keyAlphaVantage>' , view_func = tick_view , methods = ['GET']
)