# -*- coding: utf-8 -*- 

from app import app 
from flask import render_template 

@app.route('/')
def index(): 
	return "Hello World this is Terri"