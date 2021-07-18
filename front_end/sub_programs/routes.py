from sub_programs import app
import random

@app.route("/")
def home():
    return "Home"