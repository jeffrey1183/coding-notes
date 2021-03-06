from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    
    return render_template('index.html', notes = session["notes"])

