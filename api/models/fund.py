import peewee as p

from . import PeeWeeBaseModel


class Fund(PeeWeeBaseModel):
    id = p.BigAutoField()
    totalamount = p.IntegerField()
