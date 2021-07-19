from sub_programs import app
import ast
import operator
from flask import request, Response

colours = ["Red","Blue","Green","Yellow","White"]
attributes = ["Intelligence","Madness","Anger","Ego","Likeability"]

@app.route("/generate_object", methods=["POST"])
def generate_object():
    input = str(request.data.decode('utf-8'))

    dictionary = ast.literal_eval(input)

    colour = dictionary["Colour"].lower()

    dictionary.pop('Colour', None)

    if colour == "red":
        dictionary["Anger"] = dictionary["Anger"] + 10
        statBoost = "Anger"
    elif colour == "blue":
        dictionary["Intelligence"] = dictionary["Intelligence"] - 10
        statBoost = "Intelligence"
    elif colour == "green":
        dictionary["Ego"] = dictionary["Ego"] + 10
        statBoost = "Ego"
    elif colour == "yellow":
        dictionary["Likeability"] = dictionary["Likeability"] + 10
        statBoost = "Likeability"
    elif colour == "white":
        dictionary["Madness"] = dictionary["Madness"] + 10
        statBoost = "Madness"

    emotion = max(dictionary.items(), key=operator.itemgetter(1))[0]

    out = "This is a " + colour + " core with the emotion " + emotion.lower() + " their colour has an effect on " + str(statBoost)

    return Response(out, mimetype='text/plain')
