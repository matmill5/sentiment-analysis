from flask import Flask, redirect, render_template

#For getting template data
#import get_data

app = Flask(__name__)

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