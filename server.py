from flask import Flask
from flask_cors import CORS
from routes.authRoute import auth_routes
from routes.complaintRoute import complaint_routes
from config.dbConfig import db

app = Flask(__name__,static_url_path='', static_folder='public')
CORS(app)
PORT = 8081

# Middleware
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config['JSON_SORT_KEYS'] = False
# app.config['JSONIFY_MIMETYPE'] = 'application/json'
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['CORS_SUPPORTS_CREDENTIALS'] = True

# Routes
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(complaint_routes, url_prefix='/complaints')

# Start the server
if __name__ == '__main__':
    app.run(port=PORT, debug=True)

# Handle MySQL connection events
@db.event_listeners_for('error')
def handle_db_error(*args, **kwargs):
    print('MySQL error:', kwargs['exception'].message)

# Event listener for when a MySQL connection is closed
@db.event_listeners_for('close')
def handle_db_close(*args, **kwargs):
    print('MySQL connection closed')
