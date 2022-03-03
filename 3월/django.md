# 03.02
## Django 준비
```
python -m venv venv
source venv/Scripts/activate (중요)

vscode ctrl+shift+p
python select inter...
venv 선택

pip install django==3.2.12
django-admin startproject firstpjt .
python manage.py runserver
python manage.py startapp articles (이름 복수형)
```
### views.py
```py
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    context={
        'message' : request.GET.get("message")
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context={
        "name":name
    }
    return render(request, 'hello.html',context)
```
### throw.html
```html
{% block content %}
  <h1>throw</h1>
  <form action="/catch">
    <label for="message">입력</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
{% endblock content %}
```
### catch.html
```html
{% block content %}
  {{message}}
  <a href="/throw">돌아가기</a>
{% endblock content %}
```
### Variable routing
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>hello world!{{name}}</h1>
</body>
</html>
``` 
# 03.03
### random
```py
import random

def lotto(request):
    number = random.sample(range(1,46), 6)
    context = {
        'number' : number
    }
    return render(request, 'lotto.html', context)
```
### 반복문 숫자세기
```html
{% for post in posts %}
  <p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
{% endfor %}
```
### list가 비어있을때
```html
{% for user in users %}
  <p>{{ user }}</p>
{% empty %}
  <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```
### 날짜 표현
```html
```html
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{ today|date:"Y년 m월 d일 (D) A h:i" }}
```
## App URL mapping
각 app에 urls.py를 생성
### 프로젝트 urls.py
```py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]
```
### articles app의 urls.py
```py
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>', views.hello),
]
```
## Naming URL patterns
링크에 url을 직접 입력하는게 아닌 name인자 사용
### views.py
```py
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>', views.hello),
]
```
### throw.html
```html
{% extends 'base.html' %}
{% block content %}
  <h1>throw</h1>
  <form action="{% url 'catch' %}">
    <label for="message">입력</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  <p>{{ today|date:"Y년 m월 d일 (D) A h:i" }}</p>
{% endblock %}
```
