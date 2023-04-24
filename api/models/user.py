import peewee as p

from . import PeeWeeBaseModel


class User(PeeWeeBaseModel):
    id = p.BigAutoField(null=True)
    name = p.TextField()
    phoneNumber = p.TextField()
    email = p.TextField()
    password = p.TextField()
    fund = p.IntegerField()
    role = p.TextField(choices=['0', '1'])
