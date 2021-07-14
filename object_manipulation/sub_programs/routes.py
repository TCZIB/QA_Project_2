from sub_programs import app
import json
import operator
from flask import render_template, request, url_for, redirect

colours = ["Red","Blue","Green","Yellow","White"]

@app.route("/generate_object", methods=["POST"])
def generate_object():
    input = str(request.data.decode('utf-8'))
    position = input.find("Colour")
    
    dictionary = json.loads(input[:position])
    colour = input[position+7:]

    max_stat = max(dictionary.items(), key=operator.itemgetter(1))[0]

    out = "This is a " + str(colour.lower()) + " core with the main trait of " + max_stat

    return out
