from flask import Blueprint, request, jsonify
from controllers.authController import register_user_controller, login_user_controller

auth_routes = Blueprint('auth_routes', __name__)

# Register endpoint
@auth_routes.route('/register', methods=['POST'])
def register():
    return register_user_controller()

@auth_routes.route('/login', methods=['POST'])
def login():
    return login_user_controller()


# @auth_routes.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     return login_user(username)
