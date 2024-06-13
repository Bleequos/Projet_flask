from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b162111c585dde467b64f0536c6a5cd0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://anonyme:Admin@localhost:5432/PlateformeEducative'

db = SQLAlchemy(app)

from . import routes