﻿from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
	return "Hello, this is Johnny Cheng!"