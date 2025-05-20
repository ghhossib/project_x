from Models.Base import *

class Documents_practice(Base):
    id = PrimaryKeyField()
    Document = BlobField()
    Name_Document = CharField()

    class Meta:
        table_name = 'Documents_practice'

if __name__ == "__main__":
    pass