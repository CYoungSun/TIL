## model form
pip install django-bootstrap-v5
- 여러 목록중 하나를 고르게 하는 필드를 만들고 싶으면 아래와 같이 만들면 된다.
```py
genre = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        )
        ,choices=[('코미디','코미디'),('공포','공포'),('로맨스','로맨스')], required=True)
```
```
주의할 점
choices=[] 안에 들어가는 값은 튜플로 해야한다. 요소가 2개가 필요하다. 앞에를 ''로하면 화면상으로 출력될 때 빈칸으로 나온다.
```
- score와 같이 최대, 최소, step이 있는경우 widget을 만들때 NumberInput을 사용해 max_value, min_value를 사용하고 attrs에 step을 설정한다.
```py
 score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Score',
                'step' : '0.5',
                'type' : 'number',
            },
        ), max_value=5, min_value=0
    )
```
- 날짜 필드를 만들고 싶으면 DateTimeField로 만들고 widget을 NumberInput을 사용한 다음 type을 date로 해주면 된다.
```py
release_date = forms.DateTimeField(
        widget = forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'type' : 'date',
            }
        )
```
## Login
```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```