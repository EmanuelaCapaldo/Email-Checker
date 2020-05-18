from flask import Flask, redirect, url_for#FLASK class imported
#instance of the class - Flask knows where to look for static files..
app = Flask(__name__)

import re #module for regex

#assing URLs to functions of app easily
@app.route('/')
def home():
	return "<h1>Email checker web page<h1>"


@app.route("/admin")
def admin():
	return redirect(url_for("home"))#redirecting to function home


@app.route("/email/<email_address>")
def email_checker(email_address): 
	pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|it|edu)"
	if(re.search(pattern, email_address)):
		return "Valid email"
	else:
		return "Invalid email"


if  __name__ == "__main__":
	app.run()
