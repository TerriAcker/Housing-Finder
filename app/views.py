# -*- coding: utf-8 -*- 

from app import app 
from flask import render_template 



@app.route('/')
def index():
	return render_template("Housingfinder.html")


@app.route('/hello')
def hello(): 
	return "Hello World this is Terri"


@app.route('/search')
def search():
	return render_template("search.html")

@app.route('/location')
def location():
	return render_template(location.html)
	
			