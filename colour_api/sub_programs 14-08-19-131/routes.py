from sub_programs import app
from flask import render_template, request, url_for, redirect

@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    return "Test"