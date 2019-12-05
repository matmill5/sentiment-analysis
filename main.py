import os
import json
import urllib.request
import pymysql
from tables import Results
from dbConfig import mysql
from flask_app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from processUploads import processUploads
from userUploadSize import getuserUploadSize

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login', methods=["GET","POST"])
def user_login():
	conn = None
	cursor = None
	try:
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM user WHERE name=userName AND password=userPassword")
		rows = cursor.fetchall()
		if(len(rows) == 1):
			flash('User Logged In Successfully')
			return redirect('/')
		else:
			flash('Login Unsuccessful')
		table = Results(rows)
		table.border = True
		return render_template('login.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signup', methods=["POST"])
def add_user():
	conn = None
	cursor = None
	try:		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		#We arent actually using this
		_check = request.form['inputCheck']
		# validate the received values
		if _name and _email and _password and _check and request.method == 'POST':
			#do not save password as a plain text
			#sike, we save plain text.  We live on the edge of danger.
			#_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _password)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Delete users
@app.route('/delete/<int:id>')
def delete_user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM user WHERE user_id=%s", (id,))
		conn.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/users')
def users():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM user")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/pricing')
def pricing():
	return render_template('pricing.html')

@app.route('/process')
def process():
	status = processUploads()
	return render_template('process.html', status=status)

@app.route('/results')
def results():
	with app.open_resource('user/userResults_d3/testD3Resultpi.json') as f:
		piResults = json.load(f)
	with app.open_resource('user/userResults_d3/testTBlobD3Resultpi.json') as f:
		piTBlobResults = json.load(f)
	with app.open_resource('user/userResults_d3/testD3Result.json') as g:
		bubbleResults = json.load(g)
	with app.open_resource('user/userResults_d3/testD3Resultcloud.json') as h:
		cloudResults = json.load(h)
	return render_template('results.html', piResults=piResults, bubbleResults=bubbleResults, cloudResults=cloudResults, piTBlobResults=piTBlobResults)

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
			# 'up_' is concatinated to mark un-processed files
			# All files are un-processed, by default, on upload.
			print(getuserUploadSize())
			if(getuserUploadSize() < 500,000,000):
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], ('up_' + filename)))
				flash('File successfully uploaded')
				return redirect('/upload')
		else:
			flash('Allowed file types are csv')
			return redirect(request.url)

if __name__ == "__main__":
    app.run()