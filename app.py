import os
from flask import Flask, request, jsonify
from flask.logging import default_handler

import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# Set the log level
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('app.log')

# Add the file handler to the logger
logger.addHandler(file_handler)

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configure logging
app.logger.removeHandler(default_handler)
app.logger.addHandler(logging.FileHandler('app.log'))
app.logger.setLevel(logging.INFO)

# Use environment variables
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/mydatabase'

# Define routes
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


