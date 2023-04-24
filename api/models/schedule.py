import peewee as p

from user import User
from . import PeeWeeBaseModel


class Positions(PeeWeeBaseModel):
    id = p.BigAutoField(null=True)
    date = p.DateField()
    time = p.TimeField()
    fieldfee = p.IntegerField()
    participants = p.ForeignKeyField(User)



