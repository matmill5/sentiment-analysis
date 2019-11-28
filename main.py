import os
#import magic
import json
import urllib.request
from flask_app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
#from vader import vaderGo

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/pricing')
def pricing():
	return render_template('pricing.html')

@app.route('/process')
def process():
	return render_template('process.html')

@app.route('/process', methods=['POST', 'GET'])
def do_process():
	return "Starting data processing"

#@app.route('/vader')
# def vader():
#     vaderGo()
#	return "success"

#@app.route('/textblob')
# def textblob():
#     textBlobGo()
#
#	return "textblob"

#@app.route('/ai')
#def ai():
#	if(successful)
#		return "success", 200
#	else
#		return "failure", 403

@app.route('/results')
def results():
	with app.open_resource('static/d3Results/testD3Resultpi.json') as f:
		piResults = json.load(f)
	with app.open_resource('static/d3Results/testD3Result.json') as g:
		bubbleResults = json.load(g)
	with app.open_resource('static/d3Results/testD3Resultcloud.json') as h:
		cloudResults = json.load(h)
	return render_template('results.html', piResults=piResults, bubbleResults=bubbleResults, cloudResults=cloudResults)

@app.route('/contact')
def contact():
	return render_template('contact.html')
@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_form():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/upload')
		else:
			flash('Allowed file types are csv')
			return redirect(request.url)

if __name__ == "__main__":
    app.run()