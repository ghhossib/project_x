from Models.Document_practice import *

class Document_practiceController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Documents_practice.select()



    @classmethod
    def show(cls, id):
        return Documents_practice.get_or_none(id)

if __name__ == "__main__":
    pass
