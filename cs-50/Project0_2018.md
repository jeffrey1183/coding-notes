In project 0, you'll have more of an opportunity to experiment with some of this, to use Bootstrap, to make your web page mobile-responsive, and to begin to use Sass in order to create more advanced, more sophisticated stylesheets.

Project page: https://docs.cs50.net/web/2018/x/projects/0/project0.html


What I learned
* How to use SCSS variable, SCSS nesting, and SCSS inheritance to improve my code.
* April 4, 2019. 
 * [Adding the margin and to help browsing in mobile.](https://github.com/jeffrey1183/jeffrey1183.github.io/commit/ee750d3ff0959216c55c6a90c4590c9022e2e3ba), here is [the document](https://www.w3schools.com/css/css_margin.asp).
 * [Learn how to type hypen, em dash and en dash.](https://www.zhihu.com/question/19715623) and [when to use](https://www.punctuationmatters.com/hyphen-dash-n-dash-and-m-dash/).
 * [Adding the sentence spacing.](https://hea-www.harvard.edu/~fine/Tech/html-sentences.html)Here are some [alternative ways](https://www.lifewire.com/html-space-tag-3466504).
 * Specifies how words should break when reaching the end of a line. Learn the difference between CSS property of [word-break, word-wrap and white-space](https://www.puritys.me/docs-blog/article-31-CSS-%E8%AA%9E%E6%B3%95%EF%BC%8C%E6%96%87%E5%AD%97%E6%8F%9B%E8%A1%8C%EF%BC%8C%E5%BC%B7%E8%BF%AB%E4%B8%8D%E6%8F%9B%E8%A1%8C%E3%80%82.html).


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