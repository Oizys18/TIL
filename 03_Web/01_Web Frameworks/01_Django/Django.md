# Django :meat_on_bone: :fire: :fried_egg:

## 개요

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

### 참고링크

- #### Restful API

https://meetup.toast.com/posts/92

https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

- Django REST Framework

https://www.django-rest-framework.org/

<hr>

- #### Django Forms

https://wayhome25.github.io/django/2017/05/06/django-form/

https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form

- Django bootstrap forms

`pip install django-bootstrap4`

https://wayhome25.github.io/django/2017/05/06/django-form/

<hr>

- #### Django 쿠키와 세션

[https://ssungkang.tistory.com/entry/Django%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%9C%A0%EC%A7%80%ED%95%98%EA%B8%B0-%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98](https://ssungkang.tistory.com/entry/Django로그인-유지하기-쿠키와-세션)

- 쿠키와 세션의 차이, 용도, 사용법

https://jeong-pro.tistory.com/80

<hr> 

- GraphQL

[https://medium.com/@FourwingsY/graphql%EC%9D%84-%EC%98%A4%ED%95%B4%ED%95%98%EB%8B%A4-3216f404134](https://medium.com/@FourwingsY/graphql을-오해하다-3216f404134)

- URL reverse

https://wayhome25.github.io/django/2017/05/05/django-url-reverse/

- `Auth0`개인정보 대리보호 사이트

 https://auth0.com/ 

- list_display

https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/

https://tutorial.djangogirls.org/ko/django_admin/

- Django girls : https://tutorial.djangogirls.org/ko

<hr>

- `settings.py`의 i18n과 i10n
  - `i18n`: == internationalization, 국제화 툴, 자동 번역 렌더링 등을 위해 설정 
  - `i10n`: == localization
- Server side(django)에 모든 데이터를 올리고 하나로 만드는 사이트 : monolithic design
- SPA: (single page web application),단일 페이지 웹 어플리케이션. 
  - 웹에서는 웹브라우저가 모든 HTML, CSS, JS파일을 해석하고 이들을 화면에 렌더링해주는 방식을 취한다.http://hong.adfeel.info/frontend/spa-2/
  - 단일 페이지 어플리케이션은 소스코드가 브라우저에 처음 로딩되었을때 로드 되었다가 필요한 데이터만(JSON,XML) 서버 통신으로 요청해서 데이터만 변경해서 사용할 수 있는 웹 어플리케이션을 의미함
- NoSQL: https://ko.wikipedia.org/wiki/NoSQL
  - 모바일 시대에 유행
  - **NoSQL** 데이터베이스는 전통적인 [관계형 데이터베이스](https://ko.wikipedia.org/wiki/관계형_데이터베이스) 보다 덜 제한적인 [일관성 모델](https://ko.wikipedia.org/w/index.php?title=일관성_모델&action=edit&redlink=1)을 이용하는 데이터의 저장 및 검색을 위한 매커니즘을 제공한다.
- MERN: MongoDB, ExpressJS, ReactJS, Node.js   // 프로그래밍 스택 / 웹 개발

- Scrimba

```
- https://scrimba.com/
  HTML/CSS 등 코딩 연습 
  사이트에서 바로 실행 및 연습 가능 
```

- HTTP error code : 401 Unauthorized

- https://developer.mozilla.org/ko/docs/Web/HTTP/Status

- ```
  401 Unauthorized
  비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다.
  ```

### `Shell embed function?`

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



### DTL(Django Template Language)

- 파이썬과 유사한 연산/조건문 기능을 html에서!
- `{% %}` 

```
for

if / else if / else 

helper
 - lorem
 - str : length, truncatechars 
 - int 

datetime
 - Y / m / d / H / i
```



### 쿠키와 세션의 차이, 용도, 사용법

- **쿠키와 세션을 사용하는 이유**:bulb: 
  - HTTP(Hypertext Transfer Protocol)의 특징이자 약점을 보완하기 위해서 
  - HTTP의 특징 
    - 1) 비연결지향 Connectionless
      - 클라이언트 request < ㅡ > response 서버 : 이후 접속을 끊는 특성  
    - 2) 상태정보유지안함 Stateless 
      - 연결을 끊는 순간 통신이 끝나며 상태 정보를 유지하지 않는 특성.
      - 비연결지향 속성 덕분에 리소스 낭비가 줄어들지만 통신할 때마다 클라이언트가 자기 자신을 인증해야하는 단점이 생김. 

- `Cookie`: 클라이언트인 웹 브라우저 로컬에 저장하는 키와 값이 들어있는 작은 데이터 파일

  - 서버가 클라이언트 (유저) 각각에게 부여한 후 다른 유저와 구분하기 위해 사용

  - 과거 로그인 / 유저인증에 사용되었지만 이젠 보안이 너무 낮아서 로그인에 사용하지 않음 

  - 장바구니에 담긴 물품과 관련된 팝업광고 등 여러 방법으로 사용 

  - 최근 로그인 인증은 서버 측에서 접속된 유저의 [IP,디바이스의 MAC, Cookie]를 모두 검증함 

  - Response Header에 Set-Cookie 속성을 사용해 만들 수 있음

  - 쿠키는 사용자가 따로 요청하지 않아도 브라우저가 자동으로 서버에 전송

    - 쿠키 프로세스

      1. 브라우저에서 웹페이지 접속

      2. 클라이언트가 요청한 웹페이지를 받으면서 쿠키를 클라이언트 로컬(하드)에 저장

      3. 클라이언트가 재 요청시 웹페이지 요청과 함께 쿠키값도 전송

      4. 지속적으로 로그인 정보를 가지고 있는 것처럼 사용

    - 쿠키의 제한 

      1. 클라이언트에 300개까지 저장 가능
      2. 하나의 도메인 당 20개의 값만 가질 수 있음
      3. 하나의 쿠키값은 최대 4KB

- `Session`: 

  - **일정 시간 동안 같은 사용자, 같은 브라우저**로부터 들어오는 일련의 요구를 하나의 상태로 보고 **그 상태를 일정하게 유지시키는 기술** 
  - 사용자의 정보를 서버에서 관리한다고 볼 수 있다.
  - 웹 브라우저를 통해 웹 서버에 접속한 후 브라우저를 종료할 때까지 유지되는 상태
  - 쿠키를 기반, 차이점은 사용자 정보를 브라우저에 저장하지 않고 서버에서 관리
    -   세션을 구별하기 위해 ID가 필요하고 그 ID만 쿠키를 이용해서 저장해놓는다.
  - https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-cookie-based-sessions
    - 세션 프로세스
      1. 클라이언트가 서버에 접속시 세션ID 발급
      2. 서버에서는 클라이언트로 발급해준 세션 ID를 쿠키를 사용해 저장 (JSESSIONID)
      3. 클라이언트는 다시 접속할 때, 이 쿠키(JSESSIONID)를 이용해서 세션ID값을 서버에 전달

- `Cookie`와 `Session`의 차이점 

|                          | 쿠키                                  | 세션                         |
| ------------------------ | ------------------------------------- | ---------------------------- |
| 저장위치                 | 클라이언트(브라우저)에 파일로 저장    | 서버에 저장                  |
| 보안                     | 보안에 취약                           | 보안성이 좋다                |
| **라이프 사이클** :bulb: | 만료기간까지 브라우저를 종료해도 유지 | 브라우저가 종료되면 자동삭제 |
| 속도                     | 속도가 빠름                           | 처리 필요, 비교적 느린 속도  |

- cf) `Cache`: 
  - Cache는 데이터나 값을 미리 복사해놓는 임시장소를 가리킨다. (CPU에 저장되는 데이터 등)
  - 웹에서의 Cache는, 이미지나 css, js파일 등이 사용자의 브라우저에 저장이 되는 것이다.
  - 즉, 한 번 사용하기 위해 불러온 정보를 다음사용에도 다시 불러오지 않도록 임시저장해두는 것.
  - 자원을 아낄 수 있다.
- cf) `Registry`:
  - cache보다도 더 CPU에 가까운 DB
- `Caching`: https://opentutorials.org/course/697/3839

**참고사이트** 

```
https://jeong-pro.tistory.com/80
https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-cookie-based-sessions
https://ssungkang.tistory.com/entry/Django로그인-유지하기-쿠키와-세션
```



## 기본 `Django project` 

### 프로젝트 시작

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

### `urls.py`

```
#url(주문서) 관리

urlpatterns = [
	# path()
    # 첫번째 인자 : 주문서(url)경로
    # 두번째 인자 : view 함수의 위치
    path('index/', pages.index)
]
```

### `views.py`

```
Function view, Class view 둘 다 사용 가능하다.
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



### `admin.py`

- Django admin 페이지에서 관리할 모델을 추가한다. 

```
from django.contrib import admin
from .models import Artist, Music, Comment

admin.site.register(Artist)
```

### `forms.py`

```
- Form 클래스를 통해 새로운 문서작성을 위한 페이지를 쉽게 작성할 수 있다. 
- input 등을 쉽게 만들 수 있음, bootstrap을 사용해 바로 작성 가능
```

- #### 주요역할 (custom form class)

```
- 입력폼 html 생성 : as_table(), as_p(), as_ul() 기본 제공
- 입력폼 값 검증 (validation)
- 검증에 통과한 값을 `사전타입`으로 제공 (cleaned_data)
```

- #### Forms Widget

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

- ### Form vs Model Form (폼과 모델폼의 차이점)

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

- ### Form Comment

https://opentutorials.org/module/4034/24999



## Database 

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

- `Models.py`에서 정의한 모델을 DB로 반영 

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

### Django model 1:N 관계 설정

https://tothefullest08.github.io/django/2019/06/10/Django19_relations1_comment_CRUD1/

- 1:N 관계 설정을 통해 각 게시글에 댓글을 쓰는 코드를 작성해보자. 유저와 댓글간의 1:N 및 게시글과 댓글 간의 1:N, 이중 1:N 관계를 띄도록 코드를 작성 할 수 있음.

## DB :scream: M:N 관계

```
Article table, User table이 있을 때 
'like'를 구현하려면 
각각의 table에서 새로운 column을 만드는 방식은 불가하다. 

따라서 새로운 table Like table을 만들어서 

4개의 column, 
user_id / pk / article_id 
1  		/ 1  /  2 : 1번 유저가 2번 글을 좋아한다.
1		/ 2  /  3 : 1번 유저가 3번 글을 좋아한다.
2 		/ 3  /  2 : 2번 유저가 2번 글을 좋아한다.
3		/ 4  /  1 : 3번 유저가 1번 글을 좋아한다. 
```

- `models.py` : like_users 

```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
```

- 중복은 자동 처리 







## Sample Projects

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













## 기능별 정리

### A. 회원가입, 로그인 모듈화 - Authentication

- ##### Process

  1. `python manage.py startapp accounts`  # `accounts` typo 조심
  2. `settings.py` `INSTALLED_APPS`등록 
  3. main app의 `urls.py` : `path('accounts/', include('accounts.urls')),` 등록
  4. `accounts` app의 `urls.py` 생성 및 `app_name`, `views.py` import,  url 패턴 등록  


- 회원가입(== User CRUD) , 로그인(cookie,session) + 권한설정

```
https://wayhome25.github.io/django/2017/05/18/django-auth/ 		#갓몽갓키
https://docs.djangoproject.com/en/2.2/topics/auth/ 				#Django Documentation	
```

- **django.contrib.auth**에 Django Authentication support가 들어있다.
- ModelForm을 이용함 
- Admin 계정,페이지를 사용하는 것과 비슷



- ### 1. 회원가입 : `UserCreationForm`

- #### User에 대한 CRUD: https://github.com/django/django/tree/master/django

- `django.contrib.auth.models.py` : `class User` < `class AbstractUser` < `class AbstractBaseUser`
  
- Documentation을 확인하면 세부사항별로 모듈화되어있다. 
  
- `forms.py` 의  UserCreationForms (model form)을 사용한다.
- `UserCreationForms`: user creation을 위한 여러 preset ModelForm 기능이 있다.
  
  - validation check ->is_valid False일 때 flash message() 생성 및 redirection





- ### 2. 로그인 : `AuthenticationForm`

- Session에 대한 CRUD (사용자의 로그인여부를 DB로 관리)

  - 사실상 회원가입과 구조는 동일하다. 

- 체크리스트

  - 회원가입이 되어있는가?
  - db저장된 id, pw와 일치하는가?

- `django.contrib.auth`의 `login`함수 사용

  - `from django.contrib.auth import login as auth_login`

  - login 함수와 변수명 겹치지 않도록 조심

  - `AuthenticationForm(request,request.POST)`: 첫번째 인자로 `requset`가 필요하다.

  - ```
    def login(request):
        if request.method =='POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context ={
            'form':form,
        }
        return render(request, 'accounts/login.html',context)
    ```

- `django login decorators`

  - https://docs.djangoproject.com/ko/2.2/_modules/django/contrib/auth/decorators/

  - ```
    from django.contrib.auth.decorators import login_required
    @login_required
    def create(request):
    ```

  - 설정시, 로그인이 안되어있을 때 함수를 호출하려고하면 로그인 페이지로 redirect

  - `http://127.0.0.1:8000/accounts/login/?next=/articles/create/`: next로 redirection

  - cf) 만약 views.py의 login함수의 함수명을 login말고 다른 것으로 바꿨다면 자동으로 보내지지 않음.

    - ```
      # views.py에서 
      @login_required(login_url='/accounts/log_in') # 으로 설정해주거나
      
      # settings.py에서
      LOGIN_URL = '/accounts/log_in/' # loginurl을 설정해줘야함
      ```

### B. Template Inheritance 

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



### C. 쿠키 사용

- #### 1. Django로 쿠키 보내기
  - 브라우저가 request / response를 도와준다. 
  - 크롬 기준 `F12` 후 네트워크 탭을 확인하면 `Request Headers`를 통해 브라우저로 전송되는 데이터를 확인할 수 있다. 

  - 크롬 기준, 쿠키는 sqlite로 저장하여 관리한다.

```python
# urls.py
path('send_cookie/', views.send_cookie, name='send_cookie')

# views.py
def send_cookie(request):
    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo')
    return res
```

- #### 2. Django로 세션 보내기

```
내용 입력 필요
```





### D. Follow 구현(M:N)

- DB구조

```
# 새로운 table, 누가 누구를 팔로우하는가에 대한 데이터를 저장
column : id(pk), from_user, to_user_id

BUT...
user table을 사용해야하기 때문에 
Django의 자동생성 User를 사용하고 있었다면 
from django.contrib.auth.models import AbstractUser
사용해서 새로운 테이블을 만들어야한다. 
```

- `accounts`app : `models.py`

  - ```
    from django.db import models
    from django.conf import settings 
    from django.contrib.auth.models import AbstractUser
    ```

- `settings.py`

  - ```
    # 새로 정의한 모델을 지정해줌 
    AUTH_USER_MODEL = 'accounts.User'
    ```



### E. `User` 모델 참조하기

https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#referencing-the-user-model

만약 독자가 [`User`](https://docs.djangoproject.com/ko/2.2/ref/contrib/auth/#django.contrib.auth.models.User) 를 직접 참조한다면 (예를 들어 외래 키로 참조하듯이), [`AUTH_USER_MODEL`](https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-AUTH_USER_MODEL) 설정이 다른 사용자 모델로 변경된 프로젝트에서는 코드가 동작하지 않을 것입니다.

```
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

### F. Tag '#' 구현(M:N)

1. `models.py`

```python
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
```

2. `models.Article`

```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True) ## 참조
```

3. 스키마 재정의

4. `views.py`: `def create()`

```python
@login_required
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save() 
            
            # hashtag
            for word in article.content.split():
                if word.startswith('#'):
                    hastag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hastag)
            return redirect(article)    					# tuple return
            												# 없으면 False,Create()
															# 있으면 True,get()
        else:
            return redirect('articles:create')
```









## 속성

### A. Queryset 

https://docs.djangoproject.com/ko/2.2/ref/models/querysets/

**Iteration.** A `QuerySet` is iterable, and it executes its database query the first time you iterate over it. For example, this will print the headline of all entries in the database:

```
for e in Entry.objects.all():
    print(e.headline)
```

- Note: Don't use this if all you want to do is determine if at least one result exists. It's more efficient to use [`exists()`](https://docs.djangoproject.com/ko/2.2/ref/models/querysets/#django.db.models.query.QuerySet.exists).

- 데이터의 포함여부를 확인하려면 `exists()`를 사용하는게 훨씬 효율적이다..! 

```
*참고
.get(): 데이터를 1개만 Return / 찾으려는 데이터가 없으면 error
.filter(): 조건에 맞는 데이터를 queryset으로 Return / 찾으려는 데이터 없으면 빈 Queryset
```

### B. With (builtins)

https://docs.djangoproject.com/en/2.2/ref/templates/builtins/

**Caches** a complex variable under a simpler name. This is useful when accessing an “expensive” method (e.g., one that hits the database) multiple times.

```python
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

- 간단한 Caching 방법

- 한번 불러온 후에 for를 돌기 때문에 메모리 낭비가 매우 적어진다 





## Django 쿼리셋 사용/수정

## Django ORM

https://brownbears.tistory.com/63



### 쿼리셋 더하기

- Q objects

  - Complex lookups with `Q` objects
  - https://docs.djangoproject.com/en/2.2/topics/db/queries/

- Itertools.chain

  - from itertools import chain

  - ```python
        followings = request.user.followings.all()
        #chain을 사용해 두 쿼리셋을 엮는다. 
        followings_and_me = chain(followings, [request.user])
        articles = Article.objects.filter(user__in=followings_and_me)
    ```



## Json 데이터 로드 및 dump

https://ko.gravatar.com/

- Django REST framework 이용 *tutorial*

- https://www.django-rest-framework.org/tutorial/quickstart/ 

- `pip install djangorestframework`

  - Django RESTFUL API를 만들기 위한 framework

- ```
  INSTALLED_APPS = [
      'musics.apps.MusicsConfig',
  ]
  'musics' 처럼 앱 이름 입력 안하고 이렇게 입력해도 된다..
  ```

- 데이터 로드

  - ```
    >[main app dir]
    	>migrations
    	>fixtures
    		>[app_name]
    			>dummy.json
    			
    이 위치에 데이터 파일 위치시킨 후 
    python manage.py loaddata [app_name]/dummy.json 
    
    데이터 로드 성공!
    ```

- 데이터 추출

  - ```
    python manage.py dumpdata articles > dummy.json --indent 2
    (--indent 2 안하면 한 줄로 나옴..)
    ```

- `serializers.py` 생성

  - ```
    from rest_framework import serializers
    from .models import Music
    
    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ('id','title','artist_id',)
    ```

- `views.py`에서 `serializers.py`의 `class MusicSerializer`를 가져와서 사용

  - ```python
    # MusicSerializer에 데이터를 넣으면 자동으로 데이터를 직렬화 해줌
    
    from django.shortcuts import render
    from .models import Music
    from .serializers import MusicSerializer
    # Response 클래스는 return을 도와줌
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    
    # RESTful하게 만들기 위해 어떤 역할을 하는지 명시해줘야함,
    # 어떤 데이터..?
    @api_view()
    def music_list(request):
        musics = Music.objects.all()
        
        # return render() -> .html 페이지로 response  
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
    
    ```

- `drf_yasg`:Yet another Swagger generator

  - https://github.com/axnsan12/drf-yasg

  - https://github.com/Redocly/redoc

  - https://github.com/swagger-api

  - `settings.py`

    - ```python
      INSTALLED_APPS = [
          'drf_yasg',
      ]
      ```

  - `views.py`

    - ```python
      from django.urls import path
      from . import views
      from drf_yasg import openapi
      from drf_yasg.views import get_schema_view
      
      schema_view = get_schema_view(
          openapi.Info(
              title='Music API',
              default_version='v1',
          )
      )
      
      app_name = 'musics'
      
      urlpatterns = [
          path('musics/', views.music_list, name='music_list'),
          path('musics/<int:music_pk>', views.music_detail, name='music_detail'),
          path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
          path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
      ]
      ```

- 클래스 상속 

  - ```python
    class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = ('id','name',)
            
            
    class ArtistDetailSerializer(serializers.ModelSerializer):
        music_set = MusicSerializer(many=True)
        
        class Meta(ArtistSerializer.Meta):
            fields = ArtistSerializer.Meta.fields + ('music_set',)
    ```

    ​	

## POSTMAN

- https://www.getpostman.com/downloads/



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

# 1014 Django

### 상식 뽀시래기

- Django girls : https://tutorial.djangogirls.org/ko
- `settings.py`의 i18n과 i10n
  - `i18n`: == internationalization, 국제화 툴, 자동 번역 렌더링 등을 위해 설정 
  - `i10n`: == localization

- Server side(django)에 모든 데이터를 올리고 하나로 만드는 사이트 : monolithic design
- SPA: (single page web application),단일 페이지 웹 어플리케이션. 
  - 웹에서는 웹브라우저가 모든 HTML, CSS, JS파일을 해석하고 이들을 화면에 렌더링해주는 방식을 취한다.http://hong.adfeel.info/frontend/spa-2/
  - 단일 페이지 어플리케이션은 소스코드가 브라우저에 처음 로딩되었을때 로드 되었다가 필요한 데이터만(JSON,XML) 서버 통신으로 요청해서 데이터만 변경해서 사용할 수 있는 웹 어플리케이션을 의미함
- NoSQL: https://ko.wikipedia.org/wiki/NoSQL
  - 모바일 시대에 유행
  - **NoSQL** 데이터베이스는 전통적인 [관계형 데이터베이스](https://ko.wikipedia.org/wiki/관계형_데이터베이스) 보다 덜 제한적인 [일관성 모델](https://ko.wikipedia.org/w/index.php?title=일관성_모델&action=edit&redlink=1)을 이용하는 데이터의 저장 및 검색을 위한 매커니즘을 제공한다.
- MERN: MongoDB, ExpressJS, ReactJS, Node.js   // 프로그래밍 스택 / 웹 개발

  

### TDD : Test driven development

- Test code를 먼저 작성한 후 개발한다 
- 기술부채가 없는, DRY한, 재사용성 높은 코드를 작성하는 방법 
- 

### list_display

https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/

https://tutorial.djangogirls.org/ko/django_admin/

## Restful API

https://meetup.toast.com/posts/92

https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

#### Django REST Framework

https://www.django-rest-framework.org/

#### GraphQL

[https://medium.com/@FourwingsY/graphql%EC%9D%84-%EC%98%A4%ED%95%B4%ED%95%98%EB%8B%A4-3216f404134](https://medium.com/@FourwingsY/graphql을-오해하다-3216f404134)

### URL reverse

https://wayhome25.github.io/django/2017/05/05/django-url-reverse/

### Django Forms

https://wayhome25.github.io/django/2017/05/06/django-form/

https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form

#### Django bootstrap forms

`pip install django-bootstrap4`

https://wayhome25.github.io/django/2017/05/06/django-form/

- `Auth0`개인정보 대리보호 사이트

# 1021 Django

## 회원가입, 로그인 모듈화 - Authentication

- User가 지닐 수 있는 column
  - id
  - email
  - password
  - username
  - name
- 회원가입(== User CRUD) , 로그인(cookie,session) + 권한설정

```
https://wayhome25.github.io/django/2017/05/18/django-auth/ 		#갓몽갓키
https://docs.djangoproject.com/en/2.2/topics/auth/ 				#Django Documentation	
```

- **django.contrib.auth**에 Django Authentication support가 들어있다.
- ModelForm을 이용함 
- Admin 계정,페이지를 사용하는 것과 비슷

### 참고사항

- [https://ssungkang.tistory.com/entry/Django%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%9C%A0%EC%A7%80%ED%95%98%EA%B8%B0-%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98](https://ssungkang.tistory.com/entry/Django로그인-유지하기-쿠키와-세션)
- https://jeong-pro.tistory.com/80 #쿠키와 세션의 차이, 용도, 사용법

## Process

1. `python manage.py startapp accounts`  # `accounts` typo 조심
2. `settings.py` `INSTALLED_APPS`등록 
3. main app의 `urls.py` : `path('accounts/', include('accounts.urls')),` 등록
4. `accounts` app의 `urls.py` 생성 및 `app_name`, `views.py` import,  url 패턴 등록  



### 회원가입 : `UserCreationForm`

#### User에 대한 CRUD

https://github.com/django/django/tree/master/django

- `django.contrib.auth.models.py` : `class User` < `class AbstractUser` < `class AbstractBaseUser`
  - Documentation을 확인하면 세부사항별로 모듈화되어있다. 

- `forms.py` 의  UserCreationForms (model form)을 사용한다.
- `UserCreationForms`: user creation을 위한 여러 preset ModelForm 기능이 있다.
  - validation check ->is_valid False일 때 flash message() 생성 및 redirection

### 로그인 : `AuthenticationForm`

#### Session에 대한 CRUD (사용자의 로그인여부를 DB로 관리)

- 사실상 회원가입과 구조는 동일하다. 

- 체크리스트

  - 회원가입이 되어있는가?
  - db저장된 id, pw와 일치하는가?

- `django.contrib.auth`의 `login`함수 사용

  - `from django.contrib.auth import login as auth_login`

  - login 함수와 변수명 겹치지 않도록 조심

  - `AuthenticationForm(request,request.POST)`: 첫번째 인자로 `requset`가 필요하다.

  - ```
    def login(request):
        if request.method =='POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context ={
            'form':form,
        }
        return render(request, 'accounts/login.html',context)
    ```

- django login decorators
  - https://docs.djangoproject.com/ko/2.2/_modules/django/contrib/auth/decorators/

  - ```
    from django.contrib.auth.decorators import login_required
    @login_required
    def create(request):
    ```

  - 설정시, 로그인이 안되어있을 때 함수를 호출하려고하면 로그인 페이지로 redirect

  - `http://127.0.0.1:8000/accounts/login/?next=/articles/create/`: next로 redirection

  - cf) 만약 views.py의 login함수의 함수명을 login말고 다른 것으로 바꿨다면 자동으로 보내지지 않음.

    - ```
      # views.py에서 
      @login_required(login_url='/accounts/log_in') # 으로 설정해주거나
      
      # settings.py에서
      LOGIN_URL = '/accounts/log_in/' # loginurl을 설정해줘야함
      ```

#### HTTP error code : 401 Unauthorized

- https://developer.mozilla.org/ko/docs/Web/HTTP/Status

- ```
  401 Unauthorized
  비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다.
  ```

## Django model 1:N 관계 설정

https://tothefullest08.github.io/django/2019/06/10/Django19_relations1_comment_CRUD1/

- 1:N 관계 설정을 통해 각 게시글에 댓글을 쓰는 코드를 작성해보자. 유저와 댓글간의 1:N 및 게시글과 댓글 간의 1:N, 이중 1:N 관계를 띄도록 코드를 작성 할 수 있음.

## 쿠키와 세션의 차이, 용도, 사용법

- **쿠키와 세션을 사용하는 이유**:bulb: 
  - HTTP(Hypertext Transfer Protocol)의 특징이자 약점을 보완하기 위해서 
  - HTTP의 특징 
    - 1) 비연결지향 Connectionless
      - 클라이언트 request < ㅡ > response 서버 : 이후 접속을 끊는 특성  
    - 2) 상태정보유지안함 Stateless 
      - 연결을 끊는 순간 통신이 끝나며 상태 정보를 유지하지 않는 특성.
      - 비연결지향 속성 덕분에 리소스 낭비가 줄어들지만 통신할 때마다 클라이언트가 자기 자신을 인증해야하는 단점이 생김. 

- `Cookie`: 클라이언트인 웹 브라우저 로컬에 저장하는 키와 값이 들어있는 작은 데이터 파일

  - 서버가 클라이언트 (유저) 각각에게 부여한 후 다른 유저와 구분하기 위해 사용

  - 과거 로그인 / 유저인증에 사용되었지만 이젠 보안이 너무 낮아서 로그인에 사용하지 않음 

  - 장바구니에 담긴 물품과 관련된 팝업광고 등 여러 방법으로 사용 

  - 최근 로그인 인증은 서버 측에서 접속된 유저의 [IP,디바이스의 MAC, Cookie]를 모두 검증함 

  - Response Header에 Set-Cookie 속성을 사용해 만들 수 있음

  - 쿠키는 사용자가 따로 요청하지 않아도 브라우저가 자동으로 서버에 전송

    - 쿠키 프로세스

      1. 브라우저에서 웹페이지 접속

      2. 클라이언트가 요청한 웹페이지를 받으면서 쿠키를 클라이언트 로컬(하드)에 저장

      3. 클라이언트가 재 요청시 웹페이지 요청과 함께 쿠키값도 전송

      4. 지속적으로 로그인 정보를 가지고 있는 것처럼 사용

    - 쿠키의 제한 

      1. 클라이언트에 300개까지 저장 가능
      2. 하나의 도메인 당 20개의 값만 가질 수 있음
      3. 하나의 쿠키값은 최대 4KB

- `Session`: 

  - **일정 시간 동안 같은 사용자, 같은 브라우저**로부터 들어오는 일련의 요구를 하나의 상태로 보고 **그 상태를 일정하게 유지시키는 기술** 
  - 사용자의 정보를 서버에서 관리한다고 볼 수 있다.
  - 웹 브라우저를 통해 웹 서버에 접속한 후 브라우저를 종료할 때까지 유지되는 상태
  - 쿠키를 기반, 차이점은 사용자 정보를 브라우저에 저장하지 않고 서버에서 관리
    -   세션을 구별하기 위해 ID가 필요하고 그 ID만 쿠키를 이용해서 저장해놓는다.
  - https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-cookie-based-sessions
    - 세션 프로세스
      1. 클라이언트가 서버에 접속시 세션ID 발급
      2. 서버에서는 클라이언트로 발급해준 세션 ID를 쿠키를 사용해 저장 (JSESSIONID)
      3. 클라이언트는 다시 접속할 때, 이 쿠키(JSESSIONID)를 이용해서 세션ID값을 서버에 전달

- `Cookie`와 `Session`의 차이점 

|                          | 쿠키                                  | 세션                         |
| ------------------------ | ------------------------------------- | ---------------------------- |
| 저장위치                 | 클라이언트(브라우저)에 파일로 저장    | 서버에 저장                  |
| 보안                     | 보안에 취약                           | 보안성이 좋다                |
| **라이프 사이클** :bulb: | 만료기간까지 브라우저를 종료해도 유지 | 브라우저가 종료되면 자동삭제 |
| 속도                     | 속도가 빠름                           | 처리 필요, 비교적 느린 속도  |

- cf) `Cache`: 
  - Cache는 데이터나 값을 미리 복사해놓는 임시장소를 가리킨다. (CPU에 저장되는 데이터 등)
  - 웹에서의 Cache는, 이미지나 css, js파일 등이 사용자의 브라우저에 저장이 되는 것이다.
  - 즉, 한 번 사용하기 위해 불러온 정보를 다음사용에도 다시 불러오지 않도록 임시저장해두는 것.
  - 자원을 아낄 수 있다.
- cf) `Registry`:
  - cache보다도 더 CPU에 가까운 DB
- `Caching`: https://opentutorials.org/course/697/3839

**참고사이트** 

```
https://jeong-pro.tistory.com/80
https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-cookie-based-sessions
https://ssungkang.tistory.com/entry/Django로그인-유지하기-쿠키와-세션
```

### 1. Django로 쿠키 보내기

- 브라우저가 request / response를 도와준다. 
- 크롬 기준 `F12` 후 네트워크 탭을 확인하면 `Request Headers`를 통해 브라우저로 전송되는 데이터를 확인할 수 있다. 

- 크롬 기준, 쿠키는 sqlite로 저장하여 관리한다.

```python
# urls.py
path('send_cookie/', views.send_cookie, name='send_cookie')

# views.py
def send_cookie(request):
    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo')
    return res
```

### 2. Django로 세션 보내기





### Django admin.py 세팅

```
from django.contrib import admin
from .models import Artist, Music, Comment

admin.site.register(Artist)
```





## `User` 모델 참조하기

https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#referencing-the-user-model

만약 독자가 [`User`](https://docs.djangoproject.com/ko/2.2/ref/contrib/auth/#django.contrib.auth.models.User) 를 직접 참조한다면 (예를 들어 외래 키로 참조하듯이), [`AUTH_USER_MODEL`](https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-AUTH_USER_MODEL) 설정이 다른 사용자 모델로 변경된 프로젝트에서는 코드가 동작하지 않을 것입니다.

```
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```



## Django의 preset Form 수정하기



## DB :scream: M:N 관계

```
Article table, User table이 있을 때 
'like'를 구현하려면 
각각의 table에서 새로운 column을 만드는 방식은 불가하다. 

따라서 새로운 table Like table을 만들어서 

4개의 column, 
user_id / pk / article_id 
1  		/ 1  /  2 : 1번 유저가 2번 글을 좋아한다.
1		/ 2  /  3 : 1번 유저가 3번 글을 좋아한다.
2 		/ 3  /  2 : 2번 유저가 2번 글을 좋아한다.
3		/ 4  /  1 : 3번 유저가 1번 글을 좋아한다. 
```

- `models.py` : like_users 

```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
```

- 중복은 자동 처리 





## **Queryset** 

https://docs.djangoproject.com/ko/2.2/ref/models/querysets/

**Iteration.** A `QuerySet` is iterable, and it executes its database query the first time you iterate over it. For example, this will print the headline of all entries in the database:

```
for e in Entry.objects.all():
    print(e.headline)
```

- Note: Don't use this if all you want to do is determine if at least one result exists. It's more efficient to use [`exists()`](https://docs.djangoproject.com/ko/2.2/ref/models/querysets/#django.db.models.query.QuerySet.exists).

- 데이터의 포함여부를 확인하려면 `exists()`를 사용하는게 훨씬 효율적이다..! 

```
*참고
.get(): 데이터를 1개만 Return / 찾으려는 데이터가 없으면 error
.filter(): 조건에 맞는 데이터를 queryset으로 Return / 찾으려는 데이터 없으면 빈 Queryset


```

## With (builtins)

https://docs.djangoproject.com/en/2.2/ref/templates/builtins/

**Caches** a complex variable under a simpler name. This is useful when accessing an “expensive” method (e.g., one that hits the database) multiple times.

```python
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

- 간단한 Caching 방법

- 한번 불러온 후에 for를 돌기 때문에 메모리 낭비가 매우 적어진다 

## Follow 구현(M:N)

- DB구조

```
# 새로운 table, 누가 누구를 팔로우하는가에 대한 데이터를 저장
column : id(pk), from_user, to_user_id

BUT...
user table을 사용해야하기 때문에 
Django의 자동생성 User를 사용하고 있었다면 
from django.contrib.auth.models import AbstractUser
사용해서 새로운 테이블을 만들어야한다. 
```

- `accounts`app : `models.py`

  - ```
    from django.db import models
    from django.conf import settings 
    from django.contrib.auth.models import AbstractUser
    ```

- `settings.py`

  - ```
    # 새로 정의한 모델을 지정해줌 
    AUTH_USER_MODEL = 'accounts.User'
    ```





## Django 쿼리셋 사용/수정

## Django ORM

https://brownbears.tistory.com/63



### 쿼리셋 더하기

- Q objects

  - Complex lookups with `Q` objects
  - https://docs.djangoproject.com/en/2.2/topics/db/queries/

- Itertools.chain

  - from itertools import chain

  - ```python
        followings = request.user.followings.all()
        #chain을 사용해 두 쿼리셋을 엮는다. 
        followings_and_me = chain(followings, [request.user])
        articles = Article.objects.filter(user__in=followings_and_me)
    ```

## Tag '#' 구현(M:N)

1. `models.py`

```python
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
```

2. `models.Article`

```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True) ## 참조
```

3. 스키마 재정의

4. `views.py`: `def create()`

```python
@login_required
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save() 
            
            # hashtag
            for word in article.content.split():
                if word.startswith('#'):
                    hastag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hastag)
            return redirect(article)    					# tuple return
            												# 없으면 False,Create()
															# 있으면 True,get()
        else:
            return redirect('articles:create')
```



## Gravatar : 글 작성 시 아바타 달기

https://ko.gravatar.com/

- Django REST framework 이용 *tutorial*
  
- https://www.django-rest-framework.org/tutorial/quickstart/ 
  
- `pip install djangorestframework`

  - Django RESTFUL API를 만들기 위한 framework

- ```
  INSTALLED_APPS = [
      'musics.apps.MusicsConfig',
  ]
  'musics' 처럼 앱 이름 입력 안하고 이렇게 입력해도 된다..
  ```

- 데이터 로드

  - ```
    >[main app dir]
    	>migrations
    	>fixtures
    		>[app_name]
    			>dummy.json
    			
    이 위치에 데이터 파일 위치시킨 후 
    python manage.py loaddata [app_name]/dummy.json 
    
    데이터 로드 성공!
    ```

- 데이터 추출

  - ```
    python manage.py dumpdata articles > dummy.json --indent 2
    (--indent 2 안하면 한 줄로 나옴..)
    ```

- `serializers.py` 생성

  - ```
    from rest_framework import serializers
    from .models import Music
    
    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ('id','title','artist_id',)
    ```

- `views.py`에서 `serializers.py`의 `class MusicSerializer`를 가져와서 사용

  - ```python
    # MusicSerializer에 데이터를 넣으면 자동으로 데이터를 직렬화 해줌
    
    from django.shortcuts import render
    from .models import Music
    from .serializers import MusicSerializer
    # Response 클래스는 return을 도와줌
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    
    # RESTful하게 만들기 위해 어떤 역할을 하는지 명시해줘야함,
    # 어떤 데이터..?
    @api_view()
    def music_list(request):
        musics = Music.objects.all()
        
        # return render() -> .html 페이지로 response  
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
    
    ```

- `drf_yasg`:Yet another Swagger generator

  - https://github.com/axnsan12/drf-yasg

  - https://github.com/Redocly/redoc

  - https://github.com/swagger-api

  - `settings.py`

    - ```python
      INSTALLED_APPS = [
          'drf_yasg',
      ]
      ```

  - `views.py`

    - ```python
      from django.urls import path
      from . import views
      from drf_yasg import openapi
      from drf_yasg.views import get_schema_view
      
      schema_view = get_schema_view(
          openapi.Info(
              title='Music API',
              default_version='v1',
          )
      )
      
      app_name = 'musics'
      
      urlpatterns = [
          path('musics/', views.music_list, name='music_list'),
          path('musics/<int:music_pk>', views.music_detail, name='music_detail'),
          path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
          path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
      ]
      ```

- 클래스 상속 

  - ```python
    
    class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = ('id','name',)
            
            
    class ArtistDetailSerializer(serializers.ModelSerializer):
        music_set = MusicSerializer(many=True)
        
        class Meta(ArtistSerializer.Meta):
            fields = ArtistSerializer.Meta.fields + ('music_set',)
    
    ```