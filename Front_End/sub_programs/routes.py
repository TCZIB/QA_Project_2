from sub_programs import app
import requests
from flask import render_template, request, url_for, redirect

@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    attributes = requests.get('http://attributes_api:5000/get_attributes')
    colour = requests.get('http://colour_api:5000/get_colour')
    return str(attributes.text) + str(colour.text)