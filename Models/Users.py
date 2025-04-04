from Models.Base import *
from Models.Roles import Roles


class Users(Base):
    id = PrimaryKeyField
    login = CharField
    password = CharField
    role_id = ForeignKeyField(Roles)

    class Meta:
        table_name = 'Users'

if __name__ == "__main__":
    pass