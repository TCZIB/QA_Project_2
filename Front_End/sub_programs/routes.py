from sub_programs import app
import requests
from flask import render_template, request, url_for, redirect

@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():

    attributes = requests.get('http://attributes_api:5000/get_attributes')
    colour = requests.get('http://colour_api:5000/get_colour')
    
    output = requests.post('http://object_manipulation:5000/generate_object', data =f"{attributes.text} Colour:{colour.text}")
    
    return output.text