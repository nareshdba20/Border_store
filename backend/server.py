from flask import Flask, request, jsonify
from sql_connect import get_sql_connect
from users import get_user_details,register
from flask_cors import CORS
# global declaration
connection = get_sql_connect()

# Create a Flask application
app = Flask(__name__)
CORS(app)
# Define a route and its handler
@app.route('/getuserdetails', methods=['POST'])
def users():
    users = get_user_details(connection)
    response = jsonify(users)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response  # Added return statement

#define route for user registration
@app.route("/register", methods=["POST"])
def register_user():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    #validataion of users details
    if not (username and email and password):
        return jsonify({"error": " please provide username,email and password"})

        #Register the user
    register(connection, username, email, password)
    return jsonify({"message": "User registered successfully!"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
