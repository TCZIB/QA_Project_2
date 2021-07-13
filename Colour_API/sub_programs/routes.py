from sub_programs import app
import random

colours = ["Red","Blue","Green","Yellow","White"]

@app.route("/get_colour")
def get_attributes():
    return random.choice(colours)