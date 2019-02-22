from flask import Flask, render_template, request
#import a object of request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
# It means the only request methods I should accept is the request method post.
def hello():
    if request.method == "GET":
        return "Please submit the form instead" 
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
#Going to render a template called hello.html, passing in that name as a variable into the template.
# "name" is the name value of input tag in HTML file.