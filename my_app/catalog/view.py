import json
from flask import request , jsonify , Blueprint , abort
from flask.views import MethodView
from my_app import db , app
from my_app.catalog.model import Tick

catalog = Blueprint('catalog',__name__)
@catalog.route('/')

class TickView(MethodView):

    def get(self,name=None):
        if not name:
            ticks = Tick.query.all()
            if not ticks:
                abort(404)
            res = {}
            for tick in ticks.items:
                res[tick.Name] = {
                    "Company"  : tick.Company,
                    "Sector"   : tick.Sector,
                    "Subsector": tick.Subsector,
                    "Price"    : tick.Price,
                    "Max"      : tick.Max,
                    "Min"      : tick.Min,
                    "Open"     : tick.Open,
                    "Close"    : tick.Close
                }
        else:
            try:
                tick = Tick.query.filter_by(Name=name)
                if not tick:
                    abort(404)
                res = {
                    "Company"  : tick.Company,
                    "Sector"   : tick.Sector,
                    "Subsector": tick.Subsector,
                    "Price"    : tick.Price,
                    "Max"      : tick.Max,
                    "Min"      : tick.Min,
                    "Open"     : tick.Open,
                    "Close"    : tick.Close
                }
            except:
                abort(404)

tick_view = TickView.as_view('tick_view')

app.add_url_rule(
    '/tick/', view_func = tick_view, methods = ['GET']
)

app.add_url_rule(
    '/tick/<string:name>' , view_func = tick_view , methods = ['GET']
)