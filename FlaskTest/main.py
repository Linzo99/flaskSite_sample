#!/usr/bin/env python3
import os
from models import app, User, Admin, db
from flask import Flask, render_template, request, flash, url_for, redirect, session
from forms import LoginForm, RegisterForm, AdminForm
from werkzeug import generate_password_hash, check_password_hash, secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, user_logged_in
from flask_bootstrap import Bootstrap 




BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
Bootstrap(app)





@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
#---------------------------- Page accueil --------------------------------------------------
@app.route('/')
def index():
	return render_template('home.html')

#---------------------------- Page de Connectionb -------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=request.form['username']).first()
		if user:
			if check_password_hash(user.password, request.form['password']):
				login_user(user)
				session['loged_in'] = True
				flash('You are Loged In')
				return redirect(url_for('index'))
			else:
					flash('Username or Password Invalid')
		else:
			flash('Username or Password Invalid')
	
	return render_template('login.html', form=form)

#---------------------------------------------- Login Admin Page ----------------------------
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
	form = AdminForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			user = Admin.query.filter_by(username=request.form['username']).first()
			if user:
				if check_password_hash(user.password, request.form['password']):
					login_user(user)
					session['admin'] = True
					flash('Welcome Admin')
					return redirect(url_for('index'))
				else:
					flash('Username or Password Invalid')
			else:
				flash('Username or Password Invalid')
	return render_template('admin-login.html', form=form)

#---------------------------------------------- Page d'Enregistrement ------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			hashed_pass = generate_password_hash(request.form['password'], method='sha256')
			new_user = User(username=request.form['username'], password=hashed_pass,\
				email=request.form['email'])
			db.session.add(new_user)
			db.session.commit()
			flash('Vous etes Enregister')
			return redirect(url_for('login'))
	return render_template('signup.html', form=form)
#--------------------------------------- About Website Page ------------------------------------
@app.route('/about')
def about():
	return

#---------------------------------------- Pour se Deconnecter -----------------------------------
@app.route('/logout')
@login_required
def logout():
	logout_user()
	session.clear()
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)
	