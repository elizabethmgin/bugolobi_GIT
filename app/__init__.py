from flask import Flask
from peewee import *

app = Flask(__name__)
app.config.from_object('config')

database = SqliteDatabase(DATABASE, threadlocals=True)
database.connect()

from app import views, models


