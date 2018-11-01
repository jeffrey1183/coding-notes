import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    # In the datetime module is the datetime class (along with a date and time class)... you can do from datetime import datetime, then you don't need to repeat yourself.
    new_year = now.month == 1 and now.day == 1
    # Propertys of datetime object: https://docs.python.org/3/library/datetime.html#datetime.datetime
    return render_template("index.html", new_year=new_year)
