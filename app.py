from flask import Flask,request, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "our-secret"
debug = DebugToolbarExtension(app)
