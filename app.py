from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"