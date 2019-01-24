In project 0, you'll have more of an opportunity to experiment with some of this, to use Bootstrap, to make your web page mobile-responsive, and to begin to use Sass in order to create more advanced, more sophisticated stylesheets.

Project page: https://docs.cs50.net/web/2018/x/projects/0/project0.html


What I learned
* How to use SCSS variable, SCSS nesting, and SCSS inheritance to improve my code.


Advanced Learning:
* [The Open Graph protocol](http://ogp.me/)


Submit 50
[submit50](https://cs50.readthedocs.io/submit50/) is a command-line tool helping you submit your project to CS50. When I install it, I learn a lot knowledge about Python as below.



* [What is the difference between pyenv, virtualenv, anaconda?](https://stackoverflow.com/questions/38217545/what-is-the-difference-between-pyenv-virtualenv-anaconda)

## Introduction of [pyenv](https://github.com/pyenv/pyenv)
* [Intro](https://wwpw.jianshu.com/p/2b0b652eaa50)
* [Basic commands](http://blog.codylab.com/python-pyenv-management/)
* [Command lists](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-commands)

## Introduction of pip
* [The difference between pip and pip3](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/412233/)
* The pip installing problem I met in this project.
I met a problem about installing submit50. When I want to run the command of `pip3 install submit50`.


```
You are using pip version 10.0.1, however version 18.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

And I run the command of 'pip install --upgrade pip'.

The result is:
```
Requirement already up-to-date: pip in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
Although I have installed the Python 3.6, it still can't work.
```
The Solution is reading [Using pip3 to install Python3 modules](https://help.dreamhost.com/hc/en-us/articles/115000699011-Using-pip3-to-install-Python3-modules). 
and using the command of `$ python3 -m pip install --upgrade pip` and the reason is pip refers to the 2.7 version, so you'll have to use pip3 to let your system know you want to run the Python 3 version instead.