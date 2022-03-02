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