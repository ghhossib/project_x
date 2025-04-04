from Connection.Connect import *

class Base(Model):
    class Meta:
        database = connect()


