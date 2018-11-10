from flask import Flask, render_template, request
#import a object of request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
#It means the only request methods I should accept is the request method post.
# HTTP methods: http://flask.pocoo.org/docs/1.0/quickstart/#http-methods
def hello():
    name = request.form.get("name")

# I'm defining a new variable called name. And I'm saying name should be equal to what? I'm going to take that request that the user made. Access the form, request.form.
# Request object syntax: https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
# "name" is the name value of input tag in HTML file.
    return render_template("hello.html", name=name)
    #Going to render a template called hello.html, passing in that name as a variable into the template.
