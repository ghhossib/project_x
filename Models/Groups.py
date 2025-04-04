from Models.Base import *

class Groups(Base):
    id = PrimaryKeyField
    name = CharField()

    class Meta:
        table_name = 'Groups'

if __name__ == "__main__":
    pass