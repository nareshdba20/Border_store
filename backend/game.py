from flask import jsonify

# Save game user details
def save_game_user(connection, data):
    username = data.get('username')
    user_game = data.get('user_game')
    game_money = data.get('game_money')
    date_created = data.get('date_created')  # Get date_created from data

    # Validate data (Example: Check if required fields are present)
    if not all([username, user_game, game_money, date_created]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO game_users (username, user_game, game_money, date_created) VALUES (%s, %s, %s, %s)",
                       (username, user_game, game_money, date_created))
        connection.commit()
        cursor.close()
        return jsonify({'message': 'Game user details saved successfully'}), 200
    except Exception as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Get game user details
def get_game_users(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT username, user_game, game_money, date_created FROM game_users")
        users = cursor.fetchall()
        cursor.close()

        user_list = []
        for user in users:
            user_dict = {
                'username': user[0],
                'user_game': user[1],
                'game_money': user[2],
                'date_created': str(user[3])
            }
            user_list.append(user_dict)

        return jsonify(user_list), 200
    except Exception as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
