from django.shortcuts import render
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("base.html")

@app.route("/<name>/")
def home(name):
    return render_template("index.html")

@app.route("/ved/")
def ved():
    return render_template("temp.html")


if __name__ == "__main__":
    app.run(debug=True)