import bcrypt
import jwt
from model.userModel import create_user, login_user
from flask import request, jsonify

# Secret key for JWT (use a more secure one in production)
SECRET_KEY = "sbnsbd"

# ---------------------- REGISTER USER ---------------------- #
def register_user_controller():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        role = data.get('role', 'user')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Hash the password before storing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store hashed password in DB
        user_id = create_user(username, hashed_password.decode('utf-8'), role)

        return jsonify({'message': 'User registered successfully', 'userId': user_id}), 201

    except Exception as error:
        print("Error in register_user_controller:", error)
        return jsonify({'message': 'Internal server error'}), 500

# ---------------------- LOGIN USER ---------------------- #
def login_user_controller():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Fetch user from database
        user = login_user(username)
        print("User fetched from DB:", user)  # Debugging output

        if not user:
            return jsonify({'message': 'Invalid username or password'}), 401

        stored_hashed_password = user['password'].encode('utf-8')

        # Compare entered password with stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            role = user['role']  # Fetch role from DB

            # Generate JWT token
            token = jwt.encode({'username': username, 'role': role}, SECRET_KEY, algorithm='HS256')

            return jsonify({'message': 'Login successful', 'token': token, 'username': username}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401

    except Exception as error:
        print("Error in login_user_controller:", error)
        return jsonify({'message': 'Internal server error'}), 500
