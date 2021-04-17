# Django
Django is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of.

[不錯的學習指南](https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/)


[Creating Virtual Environments before Installing Django](https://docs.python.org/3/tutorial/venv.html)
* Change current path to where you want to create virtual environment and activate it.
* The [detail](https://docs.python.org/3/library/venv.html#module-venv) of creating virtual environments.



* The path you run `pip3 install Django` will influence the command of `django-admin startproject PROJECT_NAME` to create a number of starter files for Django project. For example, I run `pip3 install Django` on the path of `/Users/jeffreywang/`, it influence my command become `/Users/jeffreywang/Library/Python/3.8/bin/django-admin startproject lecutre3` due to the path I install django-admin like below [picture](/Users/jeffreywang/Desktop/Coding/Development/coding-notes/Install_Django_1).


After installing Django, 
1. create a project
2. create an app


# Example 1: 
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=2159)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Python/classes.py)


## I've Learned:
* Dealing with httprequest and httprospnse in Django.

# Example : views.py
* [Tutorial](https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/views_and_urlconfs.html)
* [Official document](https://docs.djangoproject.com/en/1.8/ref/request-response/#httpresponse-objects)

Thinking a view as something user might want to see.

When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.


## I've Learned:
* The relationship of URL and views. When someone browses http://127.0.0.1:8000/hello/, the view function of executes.

# Example : views.py

## I've Learned:
* Now, we need to somehow associate this view we have just created with a specific URL. To do this, we’ll create another file called urls.py in the same directory as views.py. We already have a urls.py file for the whole project, but it is best to have a separate one for each individual app.
* Set up the connection of views and urls. It os URL conf (URL configuration).
* The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. Name is giving a name to a particular URL pattern, making it easy to reference it from other parts of this appication.
* Anytime I use variable name like views, I'm using that name, I need to import it from where.



設定 request 和 response

```
def index(request):
    return HttpResponse("Hello, world!")
```

## I've Learned:

* [request class](https://www.django-rest-framework.org/api-guide/requests/)


為新增的 App 新增 url.py 的檔案，雖然整個專案已經有一個

We already have a urls.py file for the whole project, but it is best to have a separate one for each individual app.

在 url.py 把剛剛寫的 view.py 的 function 輸入進來，建一個 urlpatterns 的 list，list 裡用 path function，path function 有幾個 arguments，一個是 url 路徑，用字串表示，第二個是 view，就是頁面，像 views 裡 index function，我們希望載入頁面時可以 call 這個 function，最後是 path 的名稱，這個可加可不加。

Create a list called `urlpatterns`. For each desired URL, add an item to the urlpatterns list that contains a call to the path function with two or three arguments: A string representing the URL path, a function from views.py that we wish to call when that URL is visited, and (optionally) a name for that path, in the format name="something". For example, here’s what our simple app looks like now:

* [path fucntion](https://docs.djangoproject.com/en/3.2/ref/urls/)

設定完單一 app 的 url 後，還要去整個專案的 url 檔案進行設定。一樣是 path function，但跟之前不同的不是用 views.py 裡的 index function，我們要 include 所有在 urls.py 的路徑。為此要 import include 這個 fucntion，下面這行

`from django.urls import path, include`

我們期待用戶在我們 domain 下輸入 /myapp 會出現我們 coding 好的頁面

* By doing this, we’ve specified that when a user visits our site, and then in the search bar adds /hello to the URL, they’ll be redirected to the paths inside of our new application.

如果我的網址是 localhost:8000/myapp/jeffrey 頁面會顯示 Hello Jeffrey
可以在 views.py 定義下面的 function

```
def jeffrey(request):
    return HttpResponse("Hello Jeffrey!")

```

在 urls.py 加入這個路徑

```

urlpattern = [
    path("jeffrey/", views.jeffrey, name="jeffrey")

]

```

如果為了每個人去加路徑太麻煩了，要用參數去解決這個問題，在 views.py 寫含有字串變數的 function

```

def greet(request, name):
    return HttpResponse(f"Hello {name}!")

```

在 urls.py 新增 path

```
urlpattern = [
    path("<str:name>, views.greet", name="greet")
]

```


HTML 和 Python 的結合可以在 Django 裡做，像課程裡的 templates 這一塊。