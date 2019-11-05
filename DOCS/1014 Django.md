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
- 

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

    ​	





## POSTMAN

- https://www.getpostman.com/downloads/

