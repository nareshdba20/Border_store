import mysql.connector

__cnx = None

def get_sql_connect():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='project@123',
                                        host='127.0.0.1',
                                        database='grocery')
    return __cnx
