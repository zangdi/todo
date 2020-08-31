import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get directory path of our file
db_string = os.environ['dbstring']
params = urllib.parse.quote_plus(db_string)

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Wrap our Flask Alchemy instance around our Flask Application
db = SQLAlchemy(app)

from app import routes