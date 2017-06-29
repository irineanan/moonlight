import datetime

from os import path
from peewee import *
from  datetime import datetime
ROOT= path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"my_database.db"))

class User(Model):
    names = CharField()
    email = CharField()
    age = IntegerField()
    password = CharField()
    class Meta:
        database = db

class Product(Model):
    names = CharField()
    quantity = IntegerField()
    price = IntegerField()
    owner = IntegerField()
    date_added = DateField( default = datetime.today())
    class Meta:
        database = db


# User.create_table()
# Product.drop_table()
# Product.create_table()
# Product.create(names = "Books", quantity = 125, price = 70, owner = 1)
