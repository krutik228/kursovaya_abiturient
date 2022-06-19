import pymysql
from config import host, user, db_name, password

class Connection(object):
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")

        except Exception as ex:
            print("not connected...")
            print(ex)