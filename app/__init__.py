# Import flask and template operators
from flask import Flask, render_template,session

from flask_session import Session
import os

from flask import app as app

import tempfile
from werkzeug.utils import secure_filename



# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy, BaseQuery

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')





# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


app.secret_key = 'super-secret-key'

app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_SQLALCHEMY'] = db

session = Session(app)
session.app.session_interface.db.create_all()



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_test.controllers import mod_test as test_module

# Register blueprint(s)
app.register_blueprint(test_module)

# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

