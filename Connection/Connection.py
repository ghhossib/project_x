from peewee import *
#функция подключения к БД
def connect():
    mysql_db = MySQLDatabase('project_x',
                             user='site111',
                             password='',
                             host='localhost',
                             port=3306)
    return mysql_db

if __name__ == "__main__":
    print(connect().connect())