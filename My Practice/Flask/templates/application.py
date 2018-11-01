from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    # And what that's telling flask to do is take an index.html file and render that and display it to the user
