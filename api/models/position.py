import peewee as p

from . import PeeWeeBaseModel


class Position(PeeWeeBaseModel):
    id = p.BigAutoField(null = True)
    position = p.TextField()