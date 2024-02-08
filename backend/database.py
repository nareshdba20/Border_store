import mysql.connector
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'project@123',
    'database': 'grocery'
}


def authenticate_user(username, password):
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result and result[0] == password:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False
