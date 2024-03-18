import mysql.connector

__cnx = None

def get_sql_connect():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='12345',
                                        host='127.0.0.1',
                                        port='3307',
                                        database='grocery')
    return __cnx