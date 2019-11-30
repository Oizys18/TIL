# Deploying, 배포

- Django Backend REST API 서버 -> Heroku
- VUE CLI Frontend 서버 -> Firebase

# Django to Heroku

https://devcenter.heroku.com/articles/getting-started-with-python

- Local PC에서 곧바로 Heroku 서버로 배포 가능하다.
- 하지만 기록을 위해 서버에 배포할 프로젝트 경로를 Git 원격저장소에 모두 추가한다.
- 서버 배포 전 새로운 `repository`에 `push`한 후 각 단계마다 `commit`한다.
  - Local PC -> Git remote Repo(Gitlab/Github 등) 
  - Local PC **- Deploy ->** Online Remote Server(Heroku server) 배포

### 초기세팅

#### 0. Heroku 가입, Heroku CLI 설치
- https://devcenter.heroku.com/articles/heroku-cli 
#### 1. 필요 파일 및 패키지 생성 / 설치

##### a. `django-heroku` 설치
- https://github.com/heroku/django-heroku  
- `pip install django-heroku`
- 기능
  - Settings configuration (Static files / WhiteNoise). 
  - Logging configuration.
  - Test runner (important for Heroku CI).
  - `DATABASE_URL`, `ALLOWED_HOSTS` 자동 변경 및 설정
  - `.env`에 `SECRET_KEY` 변수명으로 추가된 SECRET_KEY를 자동으로 추가한다.
  
  
  
- 사용법
```
# Django app settings.py 최하단에 추가한다. 

import django_heroku
django_heroku.settings(locals())

# 예외처리가 필요할 시 settings()에 아래의 값을 추가하여 설정 가능하다. 
databases
test_runner
staticfiles
allowed_hosts
logging
secret_key
```

##### b. `gunicorn` 설치
- `$ pip install gunicorn`

- https://gunicorn.org/

- http://docs.gunicorn.org/en/latest/install.html

  - WSGI(Web Server Gateway Interface)란?

  ```
  파이썬에서 어플리케이션이 웹 서버와 통신하기 위한 인터페이스이다. 
  즉 웹 서버에서 어플리케이션을 작동시키기 위한 인터페이스인 CGI(Common Gateway Interface)의 일종.
  
  # 작동방식
  request -> Web Servcer -> WSGI server(Middleware) -> WSGI 지원 App(django 등)
  
  이때 WSGI server(middleware)는 
  1. 같은 프로세스 내에서 여러 프레임워크,어플리케이션을 실행시켜준다.
  	- $ python manage.py runserver로 배포하면 안되는 이유
  2. 환경변수가 바뀌면 Target URL에 따라 request 경로를 지정해준다. 	
  ```

- 기능

  - `pre-fork worker model`로 `central master process` 가 `set of worker process`를 관리한다.
  -  개별 `worker process`가 모든 요청/응답을 처리한다.
  - framework들은 스스로 수 많은 요청을 실행하고 최적으로 처리하지 못하기 때문에, 이 부분을 WSGI가 대신 처리한다.

- 사용법

  - **Django에서 추가설정없이 자동으로 작동된다.** 

##### c. `Procfile` 생성

- 프로세스 유형을 지정한다.
- Heroku가 웹사이트 생성을 위해 실행해야할 명령어 순서를 알려준다.
- 배포 시 `web`프로세스로 `gunicorn <project>.wsgi --log-file -`을 실행해서 gunicorn을 통해 WSGI를 사용해서버를 구동하겠다는 뜻이다. 

```
web: gunicorn <프로젝트명>.wsgi --log-file -
ex) web: gunicorn recap.wsgi --log-file -
```

##### d. `requirements.txt` 생성

- Heroku가 해당 Django 프로젝트 구성을 위해 필요한 required package를 확인할 수 있도록 파일을 생성한다.
- `$ pip freeze > requirements.txt` 
  - 해당 터미널 명령어를 Django 프로젝트 root directory에서 실행하면 현재 pip list의 목록을 txt로 저장해준다.

##### e. `runtime.txt` 생성

- 어떤 버전의 파이썬을 사용하고 있는 지 명시한다.
- `$ python --version`의 출력물과 동일하게 입력한다.

```
python-3.7.4
```

##### f. `SECRET_KEY` 환경변수 설정

- 환경변수 설정을 위해 `python-decouple` 사용
  - `pip install python-decouple`

- `settings.py`의 `SECRET_KEY` env로 이동

```
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
```

- `.env` 환경변수 파일 생성 (root directory)

```
SECRET_KEY='~~원래 django.settings.py에 있던 secret key'
DEBUG=True
```

#### 


#### 2. static file 모으기

- Django app `settings.py`
- `STATIC_ROOT` 설정
  - https://docs.djangoproject.com/ko/2.2/ref/settings/#static-root
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
- collect static files 
  - https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-contrib-staticfiles
```bash
$ python manage.py collectstatic
```

#### 4. Heroku cli 이용, app과 연결

- `$ heroku login`
  - pop up webpage에서 로그인
- `$ heroku create <app_name>`
  - app_name으로 Heroku 서버 생성
- `git remote -v`를 통해 Heroku 서버를 확인한다.
- `settings.py`의 `ALLOWED_HOSTS`에 생선된 Heroku 서버 URL을 추가한다.
- `$ heroku git:remote -a <app>`
  - 필요하다면, 다른 Heroku 서버로 연결한다.

- Heroku website의 연결할 서버의 변수설정
  - Settings > Config vars
    - SECRET_KEY = "~~~"
    - DEBUG = True

#### 5. Heroku 서버로 전송

- 앞서 모든 과정을 확인했다면 마지막으로 원격저장소에 `git push`한다.
- 이후 Heroku 서버의 master로 push한다.
  - `git push heroku master`
- Heroku web에서 `open app`으로 구동상태를 확인한다.

- 필요시 DB를 업데이트한다.

#### etc. 자주하는 실수 / 에러

```
1. 내가 올리려는 서버와 app에서 remote로 지정된 서버의 일치하는지?
2. web의 서버 setting에 configure variable 추가했는지?
3. venv를 사용한다면 필요 패키지를 모두 설치했는지? 혹은 venv가 켜져있는지?
4. 만약 패키지를 새로 설치했다면, pip freeze를 통해 requirements.txt를 업데이트했는지?
5. ALLOWED_HOST에 서버주소를 통과시켜주도록 설정했는지?
6. heroku 서버와의 연결말고도 Remote repo와도 연결설정이 되었는지?
7. git push heroku server를 실행한 후 기도는 빼먹지 않았는지?
```

# Vue CLI to Firebase

- https://firebase.google.com/docs/web/setup?hl=ko
- https://firebase.google.com/docs/hosting/quickstart?hl=ko

### 초기세팅

#### 0. google firebase 가입

- https://console.firebase.google.com/
- 계정 설정 
- 새 프로젝트 생성
- 국가 설정(대한민국)
- Google Analytics data 전송 설정 

#### 1. Firebase CLI 설치 및 인증	

- `$ npm install -g firebase-tools`
  - `-g` global 설정 잊으면 작동 안 할 수도 있다.

- `$ firebase login`
- `$ firebase list` 
  - 현재 web에서 생성한 서버 목록

#### 2. Project Directory 초기화

- `$ firebase init`
  - app의 root directory 에서 실행한다.

1. firebase로 할 수 있는 작업목록 중 `Hosting` 선택
   - `space`가 선택이고 `Enter`가 확정이다.

2. Create new project 또는 Use existing project
   - 연결할 새로운 서버를 생성하거나 이미 존재하는 서버를 설정한다.

3. Public directory 설정

   - 공개용 루트 디렉토리로 사용할 곳을 지정.

   - Compile된 배포용 파일(index.html)이 생성될 디렉토리로 설정한다.
   - 보통 `dist` 를 사용해서 자동으로 새로운 폴더를 생성하게 한다.

4. URL 구성을 선택한다.
   - `vue-router`를 사용하는 SPA의 경우 Y를 선택한다.
   - firebase가 index.html에 URL을 모두 모아서 입력한다.

#### 3. Compile

- `$ npm run build`
  - 배포를 위해 모든 파일을 compile한다.

#### 4. 배포

- `$ firebase deploy` 
  - 문제없을 경우 아래 url로 배포된다.
  - `projectID.web.app`
  - `projectID.firebaseapp.com`

#### 5. 추가

a. 로컬 수정/업데이트 반영

- 아래와 같은 순서로 다시 컴파일 -> 배포 한다.
  - `$ npm run build`
  - `$ firebase deploy`

b. test run

- `$ firebase serve`



