import peewee as p

from . import PeeWeeBaseModel


class User(PeeWeeBaseModel):
    name = p.TextField()
    phonenumber = p.TextField()
    email = p.TextField()
    password = p.TextField()
    fund = p.IntegerField()
    role = p.TextField()
