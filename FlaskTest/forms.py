from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
	username = StringField('utilisateur', validators=[InputRequired(), Length(5,20)])
	password = PasswordField('mot de passe', validators=[InputRequired(), Length(5,20)])
	remember_me = BooleanField('se souvenir')

class RegisterForm(FlaskForm):
	username = StringField('utilisateur', validators=[InputRequired(), Length(5,20)])
	password = PasswordField('mot de passe', validators=[InputRequired(), Length(5,20),\
		EqualTo('confirm', 'mots de passe differents')])
	confirm = PasswordField('confirmer')
	email = StringField('email', validators=[InputRequired(), Email()])

class AdminForm(FlaskForm):
	username = StringField('admin user', validators=[InputRequired()])
	password = PasswordField('password', validators=[InputRequired()])