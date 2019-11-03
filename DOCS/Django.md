# 05_Django :meat_on_bone: :fire: :fried_egg:

- 초보몽키 Django

`https://wayhome25.github.io/django/2017/03/20/django-ep5-model/`

- 장점

```
다용도, 완결성, 안전, 확장성, 쉬운유지보수, 포터블
```

- 성격

```
Opinionated : 독선적

framework가 제작한 규칙이 많다 
>> 사용자가 지켜야할 규칙이 많다. 
but 규칙을 익힌 후 유지보수가 쉽다. 
```

- MTV 방식 

```
MVC랑 사실상 같은 것 
Model Template View 
Model : 데이터관리 : 내용물
Template : 사용자가 보는 화면 
View : 중간 관리자  *중요* : M과 T를 관리 
```

- project 단위

```
ex) logic 별로 app을 구분해서 사용 
Project
 - app1 : 게시판 
 - app2 : 회원관리
 - app3 : 영화평점
```

## 상식

- Scrimba

```
- https://scrimba.com/
  HTML/CSS 등 코딩 연습 
  사이트에서 바로 실행 및 연습 가능 
```

### `Shell embed function`

- embed() 호출을 통해 쉬운 디버깅
- Ipython을 통해 사용 가능 : `from IPython import embed`
- https://stackoverflow.com/questions/45014239/how-to-embed-python-console-like-pythonanywhere-in-django-website

- `embed()` 사용

1. `views.py`에 `from IPython import embed`

2. `settings.py`의 `INSTALLED_APPS` : `'django_extensions'` 등록

3. `views.py`의 함수 중간에 `embed()` 코드라인 삽입

4. `runserver`후 함수 실행시 Ipython shell 자동 실행
   - 실행된 Ipython에서 `form` 입력 시 현재시점까지 `form`에 있는 값이 나옴 
   - `request.POST` 작성 시 현재 QueryDict에 들어있는 값이 저장되어있음  
   - `form.is_valid()`등 으로 값의 유효성도 판별 가능 

### `ORM` : Object-Relational Mapping

```
- DB의 행,테이블도 객체로 취급 

  "Object-Relational-Mapping 은 객체 지향 프로그래밍 언어를 사용하
  여 호환되지 않는 유형의 시스템간에(Django - SQL)데이터를 변환하는
  프로그래밍 기술이다. 이것은 프로그래밍 언어에서 사용할 수 있는 '가상
  객체 데이터베이스'를 만들어 사용한다.”
```

### DTL

- 파이썬과 유사한 연산/조건문 기능을 html에서!

```
for
if
helper
 - lorem
 - str : length, truncatechars 
 - int 
datetime
 - Y / m / d / H / i
```

### Template Inheritance 

- 공통적으로 쓸 템플릿을 서로 다른 페이지에서 모두 공유하도록 하는 것 
- 모두 공통적으로 적용해야할 Navbar 등에 사용가능 

```
1. 공통 템플릿(코드) 작성 : 해당 파일을 따로 만들고 
2. 활용할 다른 파일에서 불러온다. 
```

```
1. 공통 템플릿 작성 
모두 공유할 코드 (템플릿) 작성후, 
서로 다른 페이지의 내용이 들어갈 부분을 block처리한다. 

{% block body %} <!-- 만약 body부분만 각 파일에서 따로 처리할 경우-->
   - - 내용 - - 
{% endblock %}
```

```
2. 활용할 다른 페이지에서 

{% extends 'base.html' %}
{% block body %}
	- - 내용 - - 
{% endblock %}
```

- Partial Template

```
템플릿의 일부분을 나눈 것을 각각 '_(파일명)'으로 나눈 후, 
base가 되는 html문서에 
{% include '_(파일명).html'%}
```

- os.path 

```
import os 후 사용하면 
경로 보여줌  
```

## 기본 `Django project` 

```
project 생성:
생성할 directory에서 git bash 명령 

$ django-admin startproject first_app .

# first_app 이라는 프로젝트를 '.'현재 디렉토리에 생성 
# django-admin startproject <프로젝트이름> <경로>
```

```
폴더구조 >> 대문자 구분폴더 속에 구분폴더와 동일한 이름의 프로젝트명을 소문자로 생성한다. 
```

```
서버 구동: git bash
$ python manage.py runserver
```

```
app 생성:
$python manage.py startapp <앱 이름>
```

- `urls.py`

```
#url(주문서) 관리

urlpatterns = [
	# path()
    # 첫번째 인자 : 주문서(url)경로
    # 두번째 인자 : view 함수의 위치
    path('index/', pages.index)
]
```

- `views.py`

```
함수 관리
```

- app 추가

```python
#url.py "path('index/', views.index)," 수정 > 
#settings.py 에서 'INSTALLED_APPS 최상단에 앱 추가' > 
#urls.py에서 'from 앱이름 import views' > 
#pages/views.py에서 

def index(request):
    return render(request, 'index.html')

    
```

- HttpResponse 확인 : `views.py`

```python
from django.http import HttpResponse
def home (request):
    return HttpResponse()

* django Documnetation 확인 
* django library에서 내장된 http 클래스 중 HttpResponse 끌어오는 것이다. 
```

## Django: DB

### RDBMS 관계형 DB관리 

```
Oracle, AWS redshift, excel 등 
행/열 데이터 묶음 
```

- `Django`: `settings.py` 의 Database
  - 자동으로 db.sqlite3 생성 : SQL lite 
  - App -> models.py 
  - 데이터 레코드, 테이블을 객체로 : 클래스로! 
  - `https://inloop.github.io/sqlite-viewer/` : sqlite viewer 


### Migration

```
APP의 models.py에서 
새로운 column = 새로운 클래스의 객체 

$ python manage.py makemigrations
$ python manage.py migrate 

클래스에서 추가하면 
    def __str__(self):
        return f'글번호 : {self.id} | 제목 : {self.title}'
-> 터미널에서 출력 변경 가능 
```

```
$ python manage.py sqlmigrate articles 0002
```

```
$ python manage.py shell
>>> from articles.models import Article
>>> Article.objects.all()
>>> article = Article() # 새로운 데이터 생성 
```

```
path('', articles.index, name="index")
이후 
return redirect('index') : name입력한 path로 redirect됨 
```

- 관리자 계정 만들기 (visualcode에서 터미널실행 후 )

```
$ python manage.py createsuperuser
```

```
* app에서 admin.py -> 입력 
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

## Practice Projects

### `PJT: CRUD`

- workflow

```
1. Model : 연산용
2. Workflow
 - url
 - view : 로직 분리 후 연산 최소화, 모델에서 연산
 - template 
```

- `base.html`

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'board','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

settings.py TEMPLATES 수정 
```

- `_nav`

```
<a class="nav-link" href="{% url 'post:new' %}">새글쓰기</a>
{% DTL 언어 %}
: 변수화하여 저장 
>> 앱 : 기능 
```

- 데이터를 삭제해도, id는 당겨지지 않는다. 

```
즉 이전 글의 아이디가 5라면 모든 글을 삭제하고 새로 생성해도 id는 6부터 생성됨. 
```

### `PJT: WUNDERLIST`

- `views.py` 함수 기능 합치기

```python
# new()와 create()는 선형적으로 작동이 연결되어있음 

# http method에 따라서 다른 기능을 하도록 설정 

def create(request):
    if request.method == 'GET':
        return render(request,'todos/new.html')
    else:
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todos:index')
```



## `Form Class`

- Form 클래스를 통해 새로운 문서작성을 위한 페이지를 쉽게 작성할 수 있다. 
- input 등을 쉽게 만들 수 있음, bootstrap을 사용해 바로 작성 가능

### 주요역할 (custom form class)

- 입력폼 html 생성 : as_table(), as_p(), as_ul() 기본 제공
- 입력폼 값 검증 (validation)
- 검증에 통과한 값을 `사전타입`으로 제공 (cleaned_data)

### Django Forms

https://wayhome25.github.io/django/2017/05/06/django-form/

https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form

### Django bootstrap forms

`pip install django-bootstrap4`

https://wayhome25.github.io/django/2017/05/06/django-form/

### Forms Widget

- Form의 속성값을 수정가능

```python
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자 이내로 입력해주세요',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요',
                'rows':5,
            }
        )
    )
    
# 각 항목의 Field에서 widget과 attrs를 사용한다.
```

### Form vs Model Form (폼과 모델폼의 차이점)

- Form (일반 폼) : 직접 필드 정의, 위젯 설정이 필요
- Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성

```python
from django import forms
from .models import Post

# Form (일반 폼)
class PostForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)

# Model Form (모델 폼)
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
```

[초보몽키 https://wayhome25.github.io/django/2017/05/06/django-form/]

### Form Comment

https://opentutorials.org/module/4034/24999











# 191014 

## 10 ~ 11월 plan

- form  -  Model form
- 재사용성 높은 코드를 짜는 법 

- Auth (Authentification)
- Javascript를 이용한 웹 개발 및 배포 
- TDD : Test driven development
- mtv 모델 / mvc 모델 / mvvm모델 :  https://beomy.tistory.com/43  

## React & Vue & Angular

- React 사용량이 높다 
- Vue는 simple

