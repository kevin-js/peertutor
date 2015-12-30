from app import app
from flask import url_for, redirect, render_template, request

# homepage
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', pagename="Home")

# profile page
@app.route('/profile/<username>')
def profile(username):
	# TODO: find user info in database
	user_info = {
		'firstname' : 'test user',
		'username' : 'lololol',
		'major' : ['computer science', 'economics'],
		'class_year' : '2016',
		'bio' : ['lorem ipsum', 'blahblahblah']
	}
	return render_template('profile.html', pagename=username, user_info=user_info)

@app.route('/registration')
def registration():
	return render_template('registration.html', pagename="registration")

"""TODO: register form data into database """
@app.route('/signup', methods=['POST'])
def signup():
	return render_template('registration.html', pagename="Thanks for signing up!")