import mysql.connector
from sql_connect import get_sql_connect

#It retries only data from db
def get_user_details(connection):
    cursor = connection.cursor()
    query = ("SELECT username, password FROM users")
    cursor.execute(query)
    response = []
    for (username, password) in cursor:
        response.append({
            'username': username,
            'password': password
        })
    cursor.close()  # Close the cursor, not the connection
    return response

#retrevies and insert data from user and to db
def register(connection,username,email,password):
    cursor = connection.cursor()
        # insert the sql statments to database
    sql = "insert into users(username,password,email) values (%s,%s,%s)"
    val = (username, password, email)
    cursor.execute(sql,val)
    connection.commit()
    cursor.close()


if __name__ == '__main__':
    connection = get_sql_connect()
    print(get_user_details(connection))