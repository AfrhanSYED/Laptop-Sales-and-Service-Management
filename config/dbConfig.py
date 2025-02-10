import mysql.connector

# Create a connection pool
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Forsaken*90",
    "database": "lapassistant",
}

pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="lapassistant_pool", pool_size=5, **db_config)

# Get a connection from the pool
def get_connection():
    return pool.get_connection()

# Export the connection pool
db = get_connection()