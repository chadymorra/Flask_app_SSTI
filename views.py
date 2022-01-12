from flask import Blueprint, request
from flask.templating import render_template, render_template_string

views = Blueprint(__name__,"views")

@views.route("/")
def Home():
    return render_template("index.html")

