from flask import Flask, request, render_template, session
from flask_session import Session

app=Flask(__name__)

app.config["SESSON_PERMANENT"] = False
app.config["SESSON_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    
    return render_template("index.html", notes = notes)
