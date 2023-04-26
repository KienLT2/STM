import peewee as p

from . import PeeWeeBaseModel


class Position(PeeWeeBaseModel):
    position = p.TextField()