"""Flask Application"""

# load libaries
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
import sys

# load modules
from src.blueprints.db_populate import db_populate
from src.blueprints.user_blueprint import user_blueprint
from src.blueprints.book_blueprint import book_blueprint
from src.blueprints.transaction_blueprint import transaction_blueprint

# init Flask app
app = Flask(__name__)

# database connection
app.config['MONGODB_SETTINGS'] = {
    'db':'library_database',
    'host': 'Paste URI here',
}
db = MongoEngine()
db.init_app(app)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(db_populate, url_prefix="/api/v1")
app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")
app.register_blueprint(book_blueprint, url_prefix="/api/v1/book")
app.register_blueprint(transaction_blueprint, url_prefix="/api/v1/transaction")
