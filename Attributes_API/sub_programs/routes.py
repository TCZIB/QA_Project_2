from sub_programs import app
import random

attributes = ["Intelligence","Madness","Anger","Ego","Likeability"]

@app.route("/get_attributes")
def get_attributes():
    output = {}
    
    for attribute in attributes:
        output[attribute] = f"{random.randint(1,100)}%"
    
    return output