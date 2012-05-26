from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from dataissues import default_settings

app = Flask(__name__)
app.config.from_object(default_settings)
db = SQLAlchemy(app)
