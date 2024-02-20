from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

#connect to mysql
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="project@123",
    database="grocery"
)

@app.route('/login', methods=['POST'])
def login():
    data = request.json()
    username = data.get('username')
    password = data.get('password')

#query the database
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from users wehre username=%s and password=%s",(username,password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({'message': 'Login sucessful'}),200
    else:
        return jsonify({'message': 'Login sucessful'}),401

if __name__ == '__main__':
    app.run(debug=True)
