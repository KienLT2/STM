import peewee as p

from . import PeeWeeBaseModel


class Fund(PeeWeeBaseModel):
    totalamount = p.IntegerField()
    editeddate = p.DateTimeField()