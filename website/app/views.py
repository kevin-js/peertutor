from app import app
from flask import url_for, redirect, render_template

# homepage
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', pagename="Home")


@app.route('/registration')
def registration():
	return render_template('registration.html', pagename="registration");