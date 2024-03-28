from flask import jsonify


# Save game user details
def save_game_user(connection, data):
    username = data.get('username')
    user_game = data.get('user_game')
    game_money = data.get('game_money')

    # Insert game user details into database
    cursor = connection.cursor()
    cursor.execute("INSERT INTO game_users (username, user_game, game_money) VALUES (%s, %s, %s)",
                   (username, user_game, game_money))
    connection.commit()
    cursor.close()
    return jsonify({'message': 'Game user details saved successfully'}), 200


# Get game user details
def get_game_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM game_users")
    users = cursor.fetchall()
    cursor.close()

    user_list = []
    for user in users:
        user_dict = {
            'id': user[0],
            'username': user[1],
            'user_game': user[2],
            'game_money': user[3]
        }
        user_list.append(user_dict)

    return jsonify(user_list)
