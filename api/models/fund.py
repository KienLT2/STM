import peewee as p

from . import PeeWeeBaseModel


class Positions(PeeWeeBaseModel):
    id = p.BigAutoField(null=True)
    totalAmount = p.IntegerField()