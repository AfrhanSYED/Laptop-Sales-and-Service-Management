import mysql.connector
from config.dbConfig import get_connection

# ---------------------- REGISTER USER FUNCTION ---------------------- #
def create_user(username, hashed_password, role):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_password, role))
        connection.commit()
        return cursor.lastrowid  # Return new user ID

    except mysql.connector.Error as error:
        print("Error in create_user:", error)
        return None

    finally:
        cursor.close()
        connection.close()

# ---------------------- LOGIN USER FUNCTION ---------------------- #
def login_user(username):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()  # Get user details
        return user

    except mysql.connector.Error as error:
        print("Error in login_user:", error)
        return None

    finally:
        cursor.close()
        connection.close()
