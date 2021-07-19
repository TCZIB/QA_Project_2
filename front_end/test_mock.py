from sub_programs import app
from flask import requests

colours = ["Red","Blue","Green","Yellow","White"]

def tests_colour():
    colour = requests.get('http://colour_api:5000/get_colour').text
    assert Colour in colours
