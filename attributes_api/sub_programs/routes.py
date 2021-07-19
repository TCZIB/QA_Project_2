from sub_programs import app
from flask import jsonify
import random

attributes = ["Intelligence","Madness","Anger","Ego","Likeability"]

@app.route("/get_attributes")
def get_attributes():
    output = {}
    for attribute in attributes:
        output[attribute] = random.randint(1,90)
    
    return jsonify(output)