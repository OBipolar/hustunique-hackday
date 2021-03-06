from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import bondup.views

db.create_all()
