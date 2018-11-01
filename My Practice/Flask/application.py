from flask import Flask

#We're importing flask, which is just going to be a way of creating a flask web server from this flask module that exists somewhere else.

app = Flask(__name__)

#I want to create web application to be a flask application. __name__ is presenting the current file
#So I created this flask variable called app.

@app.route("/")
def index():
    return "Hello World"

#So flask is designed in terms of routes, where a route is just part of the URL you type in order to determine which page you want to request.
#And so this slash just represents the default page. The function immediately below it.
