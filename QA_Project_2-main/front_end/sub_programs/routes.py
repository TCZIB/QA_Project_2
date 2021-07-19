from sub_programs import app
from flask import render_template
import requests
import json
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Cores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    core = db.Column(db.String(100), nullable=False)

db.drop_all()
db.create_all()

@app.route("/")
def home():
    colour = requests.get('http://colour_api:5000/get_colour')
    attributes = requests.get('http://attributes_api:5000//get_attributes')

    dictionary = json.loads(attributes.text)

    dictionary["Colour"] = colour.text

    final = requests.post('http://object_manipulation:5000/generate_object', data=str(dictionary))
    
    entry = Cores(core=str(final.text))

    db.session.add(entry)
    db.session.commit()

    return render_template('main.html', items=Cores.query.all(), currentCore=final.text)