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
### TMDB와 연계
```py
def recommendations(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/278/recommendations'
    params = {
        'api_key': '6ee28199be1bbcf8ca5e34de5bc25219',
        'language': 'ko',
    }

    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    n = random.choice(range(len(results)))
    context = {
        'photo' : results[n]['poster_path'],
        'title' : results[n]['title'],
        'overview' : results[n]['overview'],
        'id' : results[n]['id'],
    }

    return render(request, 'recommendations.html', context)
```
```html
{% extends 'base.html' %}
{% block content %}
<article class="container-fluid pb-5">
  <h1 class="text-center">쇼생크 탈출과 비슷한 영화 추천받기</h1>
  <div class="card row mx-3 px-4" style="flex-direction : row;">
    <img src="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/{{ photo }}" class="col-12 col-md-3" alt="...">
    <div class="card-body col-12 col-md-8">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ overview }}</p>
      <a href="https://www.themoviedb.org/movie/{{ id }}" class="card-link bg-primary text-decoration-none text-light btn">상세정보</a>
    </div>
  </div>
</article>
{% endblock  %}
```
# 03.08
## model
- 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
### Database의 기본 구조
- 스키마
  - 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조
- 테이블
  - 열 : 필드 or 속성
  - 행 : 레코드 or 튜플

### 명령어
```
select * from 광주3반
pip freeze > requirements.txt
pip install django-extensions
netstat -nao |  findstr "port번호" (포트번호 찾기)
taskkill /f /pid (cmd에서 해야함)
python manage.py migrate
python manage.py makemigrations (model이 변경되면)
python manage.py sqlmigrate articles 0001
----------------------------------
pip install ipython
python manage.py shell_plus
Article.objects.all()
article = Article()
article.title = "first"
article.content = "django"
article.save()
```
SQLite
vscode-icons
### ORM
- Object-Relational-Mapping
- 장점
  - SQL을 알지 못해도 DB조작 가능
  - 객체 지향적 접근으로 높은 생산성
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 현대 웹 프레임워크의 요즘은 웹 개발의 속도를 높이는 것
- 우리는 DB를 객체로 조작하기위해 ORM을 사용한다.

```
django-extentions 설치
settings.py 에 django_extentions 추가
python manage.py migrate (migrations 폴더 생성될거임)
models.py에 class생성 (models.Model 상속)
python manage.py makemigrations (models가 변경되면)
python manage.py migrate 
```
### create하는 방법 3가지
```
article = Article()
article.title = "first"
article.content = "django"

article = Article(title="second" , content="django")

Article.objects.create(ttile="third", content="django")
```
### Read하는 방법
```
Article.objects.all()
Article.objects.get(title="first")
Article.objects.filter(content="django")
```

## 입력 받은 데이터를 데이터베이스에 추가하는법
```html
<!-- new.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'new' %}" method="POST">
    <label for="title">Title</label>
    <input type="text" id="title" name="title">
    <label for="content">Content</label>
    <input type="text" id="content" name="content">
    <input type="submit">
  </form>
  <a href="{% url 'index' %}">back</a>
{% endblock %}
```
```html
<!-- article.html -->
{% extends 'base.html' %}
{% block content %}
<h1>INDEX</h1>
<a href=" {% url 'new' %}">NEW</a>
  {% if articles %}
    {% for article in articles %}
      <p>
        제목 : {{ article.title }}
      </p>
      <p>
        내용 : {{ article.content }}
      </p>
    {% endfor %}
  {% endif %}
{% endblock %}
```
```py
from django.shortcuts import render
from .models import Article
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles' : article
    }
    return render(request, 'article.html', context)

@csrf_exemp
def new(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article(title=title, content=content)
        article.save()
    return render(request, 'new.html')
```