from datetime import datetime
from flask import Flask, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#For getting template data
#import get_data

app = Flask(__name__)

#app.config['SECRET_KEY'] = ' '
#app.config['SQLALCHEMY_DATABASE_URI'] = 'capstone.mysql.pythonanywhere-services.com'

#db = SQLAlchemy(app)

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    username = db.Column(db.String(20), unique=True, nullable=False)
#    ...
#    def __repr__(self):
#       return f"User('{self.username}','{self.email}'...)"

#class Transaction(db.Model):
#    ...
#   def __repr__(self):
#       return f"Use

#class Body(db.Model):
#    ...
#   def __repr__(self):
#       return f"Use

#class Body(db.Model):
#    ...
#   def __repr__(self):
#       return f"Use

@app.route('/')
def index():
    return redirect("/static/TODO.html")

@app.route("/about")
def about():
    return(render_template("TODO.html", name="about" , n=12))

@app.route("/doc")
def anon():
    return(render_template("TODO.html", name=None , n=0))

@app.route("/import")
def anon():
    return(render_template("TODO.html", name=None , n=0))

@app.route("/export")
def anon():
    return(render_template("TODO.html", name=None , n=0))

@app.route("/report")
def anon():
    return(render_template("TODO.html", name=None , n=0))

@app.route("/analytics")
def anon():
    return(render_template("TODO.html", name=None , n=0))