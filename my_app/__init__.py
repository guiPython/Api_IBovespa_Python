from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

from my_app.catalog.view import catalog
app.register_blueprint(catalog)

db.create_all()