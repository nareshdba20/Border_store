import mysql.connector

cnx = mysql.connector.connect(user='root', password='project@123',
                              host='127.0.0.1',
                              database='grocery')
cnx.close()



