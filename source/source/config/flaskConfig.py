from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os
from os import path

import warnings
from sqlalchemy.exc import SAWarning

# Отключение предупреждений SQLAlchemy
warnings.filterwarnings('ignore', category=SAWarning)


kis = Flask(__name__)

kis.config['rootDir'] = os.getcwd()


kis.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@localhost:5432/KIS_MAIN'
kis.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(kis)
Session(kis)
