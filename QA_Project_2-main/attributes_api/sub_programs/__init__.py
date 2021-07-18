from flask import Flask, render_template

app = Flask(__name__)

from sub_programs import routes