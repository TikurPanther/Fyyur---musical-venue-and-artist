import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database


# IMPLEMENT DATABASE URL
# to run inside the udacity machine change the configeration
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/fyyur'

SQLALCHEMY_DATABASE_URI = 'postgresql://zach:password@localhost:5432/fyyur'