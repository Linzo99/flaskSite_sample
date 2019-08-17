from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
app.secret_key = "helloladiesandgentleman"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/linzo/Desktop/FlaskTest/Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	password = db.Column(db.String(80))
	email = db.Column(db.String(50), unique=True)

	def __str__(self):
		return self.username +" | "+self.email+" | "+self.password 

class Admin(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	password = db.Column(db.String(80))
	email = db.Column(db.String(50), unique=True)

	def __str__(self):
		return self.username +" | "+self.email+" | "+self.password