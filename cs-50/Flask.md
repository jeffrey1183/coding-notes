We start building some dynamic web applications using a programming language called Python in order to build web applications that are a little more powerful.

# Concepts
* [Explanation of HTTP and Flask in this course](https://youtu.be/j5wysXqaIV8?t=2358)
* [Intro of Flask, Werkzeug, WSGI and Jinga2](https://www.tutorialspoint.com/flask/flask_overview.htm)


# Example 1: hello.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=106)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/hello.py)

## I've Learned:
* Intro of function and argument.
* How to run a Python file.


# Example 2: name.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=208)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/name.py)

## I've Learned:
* The syntax of [Python 3's f-Strings](https://realpython.com/python-f-strings/) which is the latest feature in Python 3.6.0.
* Choose the Python version in Mac by [pyenv](https://github.com/pyenv/pyenv#choosing-the-python-version). Rememer to load pyenv automatically by appending `eval "$(pyenv init -)"` and set up the environment by `pyenv local 3.6.0` and run your python file. Depending on your requirements, you will have different setup. This is a great [Chinese guideline](https://www.jianshu.com/p/0fa2c7045de8) to referrence. 
 

# Example 3: variables.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=429)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/variables.py)


## I've Learned:
* Python can store integers, floating point values, boolean values and none type as variables.
* A none type is just a way in Python to represent the idea that a variable has no value.
* I never told my program that i is going to be an integer, or f is going to be a floating point number. Python figures this out for itself. And so if you're familiar with other languages like C or Java, where you're used to having to explicitly write out the name of the type for any particular variable. Python doesn't require you to do that.

# Example 4: conditions.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=612)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/conditions.py)


## I've Learned:
* Check a number whether is a positive or negative number by `IF...ELIF...ELSE` statement. And print the result out.
* In Python, indentation is necessary. This is how you tell the Python interpreter this is the code that is contained inside of this if statement. This is the code that should run if this if statement is true.


# Example 5: sequences.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=772)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/sequences.py)


## I've Learned:
* Python is very good at also supporting storing sequences of data where we have multiple values that are combined together under one name.
* String is a sequence of characters.
* Python tuple is a way of grouping a couple of values together in a single name.
* Python list is a data type that lets us store a bunch of different values all together in one. And so a list in Python is denoted by the square brackets. And each of the elements in the list are separated by commas.
* [Python has a sort of a live interpreter that lets me type code and see the result of it happening in real time.](https://youtu.be/j5wysXqaIV8?t=924) Use exit() or Ctrl-D to exit. 


# Example 6: loops0.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=1129)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/loops0.py)


## I've Learned:
* To loop through a set of code a specified number of times, we can use the [range() function](https://www.w3schools.com/python/python_for_loops.asp).


# Example 7: loops1.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=1416)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/loops1.py)


## I've Learned:
* [A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).]((https://www.w3schools.com/python/python_for_loops.asp))
* Sequences not need to be all the same data type. [But It's often good design to have elements of the list to be of the same type.](https://youtu.be/j5wysXqaIV8?t=1282)


# Example 8: sets.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=1423)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/sets.py)


## I've Learned:
* A set is just a collection of items where no item shows up twice. And in particular, a set doesn't have any particular order to it.

# Example 9: dictionaries.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=1500)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/dictionaries.py)


## I've Learned:
* A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
* An example to store the ages of different people that I'm keeping track of.


# Example 10: functions.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=1679)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/functions.py)


## I've Learned:
* [Perform a string formatting operation by using str.format()](https://realpython.com/python-f-strings/#option-2-strformat)
* In general, Python needs to know about the existence of some name before you use it.

# Example 11: modules.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2158)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/modules.py)


## I've Learned:
* Import a function from a file. [Consider a module to be the same as a code library.](https://www.w3schools.com/python/python_modules.asp)
* Nice thing about functions in Python is that once you write them once in one file, you can use them in other files as well. And so you can use Python functions that you've written yourself in other files, and you can also use functions that other people have written in their own files in your own files by referring to a function that exists in some other file.
* Prevent to run all of code automatically by adding `if __name__ == "__main__":`


# Example 11: classes.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2159)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/classes.py)


## I've Learned:
* [Python classes are a way of defining entirely new types in Python.](https://www.w3schools.com/python/python_classes.asp)


From the example 12, we start to use [Flask](https://www.tutorialspoint.com/flask/index.htm).

Flask is a very popular framework for making web based applications using Python. It's generally considered a micro framework.

# Example 12: application.py
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2464)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/application.py)


## I've Learned:
* Importing flask, which is going to be a way of creating a flask web server from this flask module that exists somewhere else. The flask code is generally stored inside of a file called `application.py`.
* What do the code do? [Here is the official explanation.](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)
* If you enter the command `flask run` and there is an `Error: Could not locate Flask application. You did not provide the FLASK\_APP environment variable.` 

This is because flask relies on what's called an environment variable, a variable that's set inside of your terminal to know what file to be looking for as the source of the application. If you're running for the first time, you need a line like export flask underscore app equals application dot py. 

 To run in development mode, set the `FLASK_ENV=development` environment variable.

```
export FLASK_APP=application.py
export FLASK_ENV=development
flask run
```

And all that line is doing is saying set the environment variable flask app to be application dot py.

In other words, tell flask that the file that I want to run this application from is a file called application do py, which is just the general convention.

* If you get a warning of not found flask command, [remember to install pip.](https://code.visualstudio.com/docs/python/tutorial-flask#_create-a-project-environment-for-flask)
* If you get a warning of production environment, please [change the environment variable](http://flask.pocoo.org/docs/1.0/config/#eenvironment-and-debug-features).



## Adavanced Learning: 
* [To select an specific environment in VS code, use the `Python: Select Interpreter` command from the Command Palette (⇧⌘P).](https://code.visualstudio.com/docs/python/environments)
* [Changing the display language in VS code.](https://code.visualstudio.com/docs/getstarted/locales)
* The display language of Python extension is determined by your system preference language.
* [Lint or linter](https://en.wikipedia.org/wiki/Lint_(software)), is a tool that analyzes source code to flag programming errors.
* [Run linter in VS code.](https://code.visualstudio.com/docs/python/linting#_run-linting) It is the solution when I met a E0401 error of Pylinter.


# Example 13: route0
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2817)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/route0)


## I've Learned:
* Set up two separate routes running on my web application. Go to the default route, it says hello world. If I go to slash David, then it says hello David.

# Example 14: route1
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2817)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/route0)


## I've Learned:
* In the last case, when I type in a route that my applicaiton not deal with. It shows up the "Not Found" in my webpage. In this case, it's able to take any string that I type in.
* [Adding variable sections to a URL by marking sections with `<variable_name>`.](http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules)
* Capitalizes the first letter through [captitalize method](https://www.tutorialspoint.com/python/string_capitalize.htm).

# Example 15: templates
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=3147)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/templates)


## I've Learned:
* Tell flask to use html files that we've already created, firstly importing a function in a flask called render template and creating a folder called "templates" which contains an index.html file.
* [In exmaple 14, the hello() function will render ‘Hello {name}’ with <h1> tag attached to it. In this example, a HTML file can be rendered by the render_template() function. Flask will try to find the HTML file in the templates folder.](https://www.tutorialspoint.com/flask/flask_templates.htm)

# Example 16: variable0
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=3147)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/templates)


## I've Learned:
* I have a variable called headline inside the html file. [The headline variable is an argument of render_template function.](http://flask.pocoo.org/docs/1.0/api/#flask.render_template) I can change variable in the application.py. The html file is dynamically rendered by flask, depending upon what I pass into it as variables.
* The syntax of double-curly braces is the templating language called jinja2 that flask uses in its html templates. In order to make it easy to dynamically generate web pages. When you install flask, Jinja2 come along with it.
* [The double-curly braces are Jinja2's way of saying substitute something here.](http://jinja.pocoo.org/docs/2.10/templates/#variables)
* I add a new function called Goodbye. The headline is "Goodbye!". In this case, I've used the same index.html template. The only difference is I've changed what value I pass in the headline.

# Example 17: condition
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=3858)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/conditions)


## I've Learned:
* Write a website like [isitchristmas.com](https://isitchristmas.com/), writing a isitnewyear's.com to check whether today is New Year.
* Python has a bunch of different modules. In this case, [the datetime module has a very easy way to get the current date.](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)
* We were able to conditionally determine what to display on the HTML page by the boolean value of `new_year` through the [if statement in HTML file](http://jinja.pocoo.org/docs/2.10/templates/#if).
* [Why do I put the if else inside the index.html instead of of inside of the Python code?](https://youtu.be/j5wysXqaIV8?t=4155)


# Example 18: loops
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=4314)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/loops)


## I've Learned:
* Loop over each item in a sequence using [for loop](http://jinja.pocoo.org/docs/2.10/templates/#for).

# Example 19: urls
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=4466)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/urls)


## I've Learned:
* [To build a URL to a specific function, use the url_for() function.](http://flask.pocoo.org/docs/1.0/quickstart/#url-building).


# Example 20: inheritance
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=4668)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/inheritance)


## I've Learned:
* The most powerful part of Jinja is [template inheritance](http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/). Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

# Example 21: forms
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=4980)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/forms)


## I've Learned:
* Get the user's name from the form and save it a variable called name.
* The request object is a Request subclass and provides the attributes including the [form attribute](http://flask.pocoo.org/docs/1.0/api/#flask.Request.form) which is a [MultiDict instances](http://werkzeug.pocoo.org/docs/0.14/datastructures/#werkzeug.datastructures.MultiDict). I can access value through the
[get method](https://docs.python.org/3/library/stdtypes.html#dict.get) that is available for all Python dictionaries. Here is [an explanation](https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request) in the Stack Overflow. 

https://docs.python.org/3/library/stdtypes.html#dict.get

# Example 22: [notes](https://jeffrey1183.github.io/coding-notes/My%20Practice/Flask/templates/index.html)
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=5631)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/notes)


## I've Learned:
* [The syntax of setting up the basic configuration values.](http://flask.pocoo.org/docs/1.0/config/#configuration-basics) and [how to initialize Session instance with a very specific Flask application](https://pythonhosted.org/Flask-Session/#api).
* [The cofiguration values of session.](https://pythonhosted.org/Flask-Session/#configuration). Basically it is necessary to configure `SESSION_TYPE`. About the `SESSION_PERMANENT` value, default to be `True`.
* The request object has the [method attribute](http://flask.pocoo.org/docs/1.0/api/#flask.Request.method) to judge the post or get method.
* [Python list append() method](https://www.w3schools.com/python/ref_list_append.asp)
* When I refresh this page, now my notes are gone because the server was shut down. In the SQL lecture, we will learn how to store the data user submitting.
* The variable of "notes" is a global variable in this case, accessing by entire application. I want to be able to take my own notes without seeing someone else's notes. that's where the concept of sessions begins to come in next example.

# Example 23: session
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=5961)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/session)


## I've Learned:
* Ｗhen you log in to the web site, you have access to some [session](https://www.tutorialspoint.com/flask/flask_sessions.htm) that is data specific to your user account. I want to be able to take my own notes without seeing someone else's notes.
* Setting up my particular session to have an empty list of notes firstly. Instead of `notes.append(note)`, the code changes into `session[notes].append (note)`. Rather than append this new note to the entire global variable representing all of the notes, I only want to append the note to the notes specific to my particular session, to my interaction with this page. If I close the browser now and then go back to it, I get to keep my notes. Because it's still stored inside of the session.
* [The null keyword is commonly used in many programming languages, such as Java, C++, C# and Javascript. The equivalent of the null keyword in Python is None.](https://www.pythoncentral.io/python-null-equivalent-none/) Using the `is` keyword to check if two variables are exactly is a better way in Python.
* Unlike a Cookie, Session data is stored on server. Session is the time interval when a client logs into a server and logs out of it. Session object is a [dictionary object](https://www.w3schools.com/python/python_dictionaries.asp) containing key-value pairs of session variables and associated values.

## Adavanced Learning: 
Error Title: jinja2.exceptions.TemplateSyntaxError
Error Description: jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got 'note'
* [The reason is my for loop syntax is wrong.](http://jinja.pocoo.org/docs/2.10/templates/#synopsis) I written with double curly brackets.


