import peewee as p

from user import User
from . import PeeWeeBaseModel
from playhouse.postgres_ext import ArrayField


class Positions(PeeWeeBaseModel):
    id = p.BigAutoField(null=True)
    date = p.DateField()
    time = p.TimeField()
    fieldfee = p.IntegerField()
    participants = ArrayField(p.ForeignKeyField(User))
