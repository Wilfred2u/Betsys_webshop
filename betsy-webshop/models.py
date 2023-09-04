# Models go here
from peewee import *

db = SqliteDatabase("webshop.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    adress = CharField()
    city = CharField()
    billing_info = IntegerField()


class Product(BaseModel):
    name = CharField()
    description = CharField(null=True)
    price_per_unit = DecimalField(decimal_places=2, default=0)
    quantity = IntegerField()
    owner = ForeignKeyField(User)


class Tag(BaseModel):
    product_name = CharField()
    tag = CharField()


class Transaction(BaseModel):
    purchaser = CharField()
    seller = CharField()
    product = CharField()
    quantity = IntegerField()
