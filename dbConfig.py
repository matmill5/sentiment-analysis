from flask_app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'capstone'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'capstone$mydb'
app.config['MYSQL_DATABASE_HOST'] = 'capstone.mysql.pythonanywhere-services.com'
mysql.init_app(app)