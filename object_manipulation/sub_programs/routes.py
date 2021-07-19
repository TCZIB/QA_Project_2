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
        dictionary["Anger"] = dictionary["Anger"] + 20
        statBoost = "Anger"
        statBoostPoint = "+20"
    elif colour == "blue":
        dictionary["Intelligence"] = dictionary["Intelligence"] - 10
        statBoost = "Intelligence"
        statBoostPoint = "-10"
    elif colour == "green":
        dictionary["Ego"] = dictionary["Ego"] + 15
        statBoost = "Ego"
        statBoostPoint = "+15"
    elif colour == "yellow":
        dictionary["Likeability"] = dictionary["Likeability"] + 25
        statBoost = "Likeability"
        statBoostPoint = "+25"
    elif colour == "white":
        dictionary["Madness"] = dictionary["Madness"] + 8
        statBoost = "Madness"
        statBoostPoint = "+8"

    emotion = max(dictionary.items(), key=operator.itemgetter(1))[0]

    out = "This is a " + colour + " core with the emotion " + emotion.lower() + " their colour has a " + str(statBoostPoint) + " effect on " + str(statBoost) + "\n" + str(dictionary).strip(" { } ' ")

    return Response(out, mimetype='text/plain')
