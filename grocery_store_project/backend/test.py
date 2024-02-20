import mysql.connector

cnx = mysql.connector.connect(user='root', password='project@123',
                              host='127.0.0.1',
                              database='grocery')

cursor = cnx.cursor()

query = ("select username,password from users")

cursor.execute(query)

for (username,password) in cursor:
  print(username,password)

cursor.close()
cnx.close()



