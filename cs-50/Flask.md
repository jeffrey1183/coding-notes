Flask is a very popular framework for making web based applications using Python.It's generally considered a micro framework.

we start building some dynamic web applications using a programming language called Python in order to build web applications that are a little more powerful than what we can have just by describing the contents of a web page using HTML, for instance.


# Example 1: [hello.py](https://jeffrey1183.github.io/coding-notes/My%20Practice/Flask/hello.py)
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=106)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/hello.py)

## I've Learned:
* Intro of function and argument.
* How to run a Python file.


# Example 2: [name.py](https://jeffrey1183.github.io/coding-notes/My%20Practice/Flask/name.py)
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=208)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/name.py)

## I've Learned:
* The syntax of [Python 3's f-Strings](https://realpython.com/python-f-strings/) which is the latest feature in Python 3.6.0.
* Choose the Python version in Mac by [pyenv](https://github.com/pyenv/pyenv#choosing-the-python-version). Rememer to load pyenv automatically by appending `eval "$(pyenv init -)"` and set up the environment by `pyenv local 3.6.0` and run your python file. Depending on your requirements, you will have different setup. This is a great [Chinese guideline](https://www.jianshu.com/p/0fa2c7045de8) to referrence. 
 

# Example 3: [variables.py](https://jeffrey1183.github.io/coding-notes/My%20Practice/Flask/variables.py)
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=429)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/variables.py)


## I've Learned:
* Look at the different types of information that we can store inside of a Python variable.



* python 不用設定變數型態
* Note that I never told my program that i is going to be an integer, or f is going to be a floating point number, or b is going to be a Boolean value.
* Python figures this out for itself.
* When I say i equals 28, Python knows that if I'm assigning the number 28 to i, then i must be in integer value. And so if you're familiar with other languages like C or Java, where you're used to having to explicitly write out the name of the type for any particular variable, know that Python doesn't require you to do that, and just lets you take a variable and assign it to any given value without needing to specify explicitly what the type of that value actually is.


#### 安裝 Anaconda 後

安裝後，電腦會預設使用的默認的 Python 是 Anaconda 附帶的 Python。

建立 python 36 的環境

```text
JunyuandeMacBook-Air:~ junyuanwang$ conda create --name python36 python=3.6
Fetching package metadata .......
Solving package specifications: ..........

Package plan for installation in environment //anaconda/envs/python36:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    xz-5.2.3                   |                0         225 KB
    zlib-1.2.11                |                0          98 KB
    python-3.6.2               |                0        11.7 MB
    certifi-2016.2.28          |           py36_0         213 KB
    wheel-0.29.0               |           py36_0          87 KB
    setuptools-36.4.0          |           py36_1         559 KB
    pip-9.0.1                  |           py36_1         1.7 MB
    ------------------------------------------------------------
                                           Total:        14.6 MB

The following NEW packages will be INSTALLED:

    certifi:    2016.2.28-py36_0
    openssl:    1.0.2l-0
    pip:        9.0.1-py36_1
    python:     3.6.2-0
    readline:   6.2-2
    setuptools: 36.4.0-py36_1
    sqlite:     3.13.0-0
    tk:         8.5.18-0
    wheel:      0.29.0-py36_0
    xz:         5.2.3-0
    zlib:       1.2.11-0
```

列出你的環境

```text
conda env list
```

Python 環境設定

* [參考 1](https://foofish.net/anaconda-install.html)
* [參考 2](https://www.zhihu.com/question/58033789)



### Indentation

The indentation in Python is actually required. Unlike several other programming languages where indentation is a style thing.

it's not strictly necessary, in Python this indentation is necessary.

[秘笈](https://www2.cs.arizona.edu/people/mccann/errors-python)

Python is very good at also supporting storing sequences of data where we have multiple values that are combined together under one name.

* sequence.py

#### Python Interpretor

Just type Python in the command line. You've opened up the Python interpreter. which is a place where I can line at a time type of line of Python code and immediately see the result.

用 quit\(\) 離開

#### Loops

loops0.py

loops1.py

* the question is, do sequences need to be all of the same data type?
* The short answer is no. it's a good idea if different things in the list are of the same type.
* 我們沒辦法去記哪一個位置是什麼 data type，全部一樣會比較好處理

sets.py

dictionaries.py

functions.py

* define a new function, this is a slightly older way of plugging in values into Python strings.
* [string format](https://www.programiz.com/python-programming/methods/string/format)
* 自定義一個 function 為輸入數字的平方，要先定義過後才能使用

modules.py

* 如何引用 function，並且指定某個 function
* 為了避免沒有要用的 function 也執行，在 functions.py 裡建立 main function

classes.py

* define a new class and create a object
  * 參考資料：[https://www.w3schools.com/python/python\_classes.as](https://www.w3schools.com/python/python_classes.asp)p 包含什麼是 self

### HTTP

If I type google.com and press Return, I'm sending an HTTP request to Google's server. Google's server receives that request, needs to figure out some way to interpret that request.

### Flask

And so what we're going to be doing now as we go about building web applications, is writing code that will take care of that server side processing. Receiving requests, figuring out what those requests they're dealing with and what they're asking for, and figuring out what response to then give back to the user.

And in order to do that, we're going to be using flask. Flask as a micro framework written in Python.

What that effectively means is that flask is some code already written for us in Python that makes it easy to get up and running with a simple web application that has a lot of features that can be useful as we go about developing web applications, as we'll soon see in a moment.

application.py

* main file of application
* command line 要輸入  `flask run`

結果出現 Error: Could not locate Flask application. You did not provide the FLASK\_APP environment variable.

這是因為 flask relies on what's called an environment variable, a variable that's set inside of your terminal to know what file to be looking for as the source of the application. If you're running for the first time, you need a line like export flask underscore app equals application dot py. And all that line is doing is saying set the environment variable flask app to be application dot py.

```text
export FLASK_APP=application.py
flask run
```

In other words, tell flask that the file that I want to run this application from is a file called application do py, which is just the general convention.

如果在跑 flask 時出現

WARNING: Do not use the development server in a production environment.

可以參考：[https://stackoverflow.com/questions/50284753/warning-message-while-running-flask](https://stackoverflow.com/questions/50284753/warning-message-while-running-flask)

不用理他

How to import Python modules?

* [https://www.w3schools.com/python/python\_modules.asp](https://www.w3schools.com/python/python_modules.asp)

如果只要輸入部分 module 就會用到 from

設定不同的 route 回傳不同的文字

* route0/application.py

route1/application.py

* app route [官方教學](http://exploreflask.com/en/latest/views.html)
* Say hello to anyone 在不同的 route 裡
* 學習怎麼用 Formatted string literals，[第二個回答](https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string-in-python)
* 要切到要執行的資料夾再跑 flask run
* [capitalize method ](https://www.tutorialspoint.com/python/string_capitalize.htm)
  * Capitalizes the first letter of it

#### Render HTML File

How to tie those html files into flask? Tell flask to use those html files that we've already created in order to return something back to the user.

Let's import a function in flask called render\_template to solve it.

* [官方教學](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates)

templates folder

* import template\_rener 和使用 render\_template
* 另外寫一個 index.html 的檔案，讓 flask render
* 要注意資料夾結構，在 templates 裡面再塞了一個 templates ，才放 index.html。application.py 另外放。
  * 這跟 how does flask find index.html, Where does it know to look?
  * Flask is only going to look immediately inside of a subdirectory called templates. 所以我們的資料夾才要這樣放。

variable0

* The text in HTML is dynamically generated, rendered by flask, depending upon what I pass into it as variables
* [如果資料夾的架構有問題](https://stackoverflow.com/questions/15053790/jinja2-exceptions-templatenotfound-error)
* what is this double curly brace index? In fact, it's entirely different, what's called a templating language, an entirely separate language called Jinja1, which is a standalone language. But it's a language that flask uses in its html templates in order to make it easy to dynamically generate web pages. And so we'll see a couple of examples of this Jinja2 syntax.
* 當 route 是 bye 的時候，畫面顯示指定的文案
* Does this Python file come as back end? Yes, What I've written here is Python code for a back end web server, that is listening for a request like, me typing in URL slash bye. It processes that request and returns some response, in this case the HTML. So yes, this back end Python code as you would term it.

codition.py

* import python module datetime to get the current date.
* [import 的語法](https://medium.com/pyladies-taiwan/python-的-import-陷阱-3538e74f57e3)，包含為何要寫
* [jinja 2 syntax](http://jinja.pocoo.org/docs/2.10/templates/#list-of-control-structures)

  ```python
  now = datetime.datetime.now()
  ```

* Question: So why did I put the if else inside the index.html instead of inside of the Python code?
  * I certainly could have put it inside the Python code. But as we start to deal with more complicated websites where I might want entire sections of HTML to appear depending upon the value of some variable, the conditioning inside of the template will become very, very helpful.
* Question: Do you need to install Jinja2 in order to make any of this work?
  * What you will need to do is you'll need to install flask, which is the micro framework that we've been using in order to generate these web applications. And when you install flask, Jinja2 come along with it.

Loops.py

* 練習使用 jinja for loop 的語法：[http://jinja.pocoo.org/docs/2.10/templates/\#for](http://jinja.pocoo.org/docs/2.10/templates/#for)
* 不用寫死資料，it's going to dynamically generate the list items as I need them.

Let's try and use Python to begin to add some new features to this website

urls 資料夾

* One thing that might immediately be helpful is figuring out how you link to different parts of your web application. You might have one route that links to another route and that route needs to link back to the original route.
* 實作功能：Link to another route，設定 index 和 more 頁面裡的連結可以讓兩個頁面連來連去
* 兩個頁面都要放在 templates 的資料夾裡

inheritance

* instead of writing the same code twice, I can just write the basic template from my web site once and fill in the blanks with whatever additional details that I have.
* templates 裡有 3 個 html 檔案，index.html, more.html 和新增加的 layout.html
* 先設定 layout 檔案，讓 index.html 沿用
* index.html 與 urls 的 index.html 內容相同，但用新的寫法
* 如果我在 layout.html 加了一行，index.html 和 more.html 都會變動
* 官方參考資料：[http://jinja.pocoo.org/docs/2.10/templates/\#template-inheritance](http://jinja.pocoo.org/docs/2.10/templates/#template-inheritance)

form

* Now that we have a back end server, a Python flask server that's running and listening to requests, we can begin to take the results of those forms and do something interesting with them.
* get and post methods
* 首頁讓用戶輸入他的名字，接著讓名字顯示在頁面上
* 如果出現 jinja2.exceptions.UndefinedError: 'layout' is undefined  
表示我的 `extends "layout.html"`忘記加雙引號

notes

* 把用戶輸入的資料，每一筆都呈現在頁面上
* session keeps variables and values that are specific
* 未實作