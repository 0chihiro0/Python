

from flask import Flask, request, render_template, make_response, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('login'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
	return "User %s" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %s" % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == "POST":
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	return render_template('login.html',error=error) 
	about(401)
	this_is_never_executed()
