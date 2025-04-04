from Models.Base import *

class Roles(Base):
    id = PrimaryKeyField
    name = CharField


    class Meta:
        table_name = 'Roles'

if __name__ == "__main__":
    pass