# Deploying, 배포

## Django to Heroku

- Local PC에서 곧바로 Heroku 서버로 배포하지 않는다.
- 따라서 서버에 배포할 프로젝트 경로를 Git 원격저장소에 모두 추가한다.
- 서버 배포 전 새로운 `repository`에 `push`한 후 각 단계마다 `commit`한다.
- Local PC -> Git remote Repo(Gitlab/Github 등) 
  - **--- Deploy --->** Online Remote Server(Heroku server) 배포

### 초기세팅

#### 0. Heroku 가입, Heroku CLI 설치
- https://devcenter.heroku.com/articles/heroku-cli 
#### 1. 필요 패키지 설치

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

#### 3. `SECRET_KEY` 환경변수 설정
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


## Vue CLI to Firebase

### 초기세팅

1. google firebase 가입(구글계정)
2. 새 프로젝트 추가
    - 계정 설정 
    - 국가 설정(대한민국)
    - Google Analytics data 전송 설정 
3. Firebase CLI 설치 및 인증	
   - `npm install -g firebase-tools`
   - `firebase login`
   - `firebase list` 
5. `firebase init`

   - 1. firebase로 무엇을 할지 물어봄. Hosting 선택
- 2. 이미 존재하는 프로젝트 사용하거나 새로 만들거나 할 수 있음
   - 3. Public directory로 뭐 사용할거냐고 물어보는데 `dist` 적으면 됨 
   - `dist`는 complie된 배포용 파일이 위치할, 곧 생성될 디렉토리
- 프로젝트와 연결
   - 공개용 루트 디렉터리로 사용할 디렉터리를 지정합니다.
     - 보통 `index.html`, 
   - 사이트 구성 선택 (SPA의 경우 Y)
5. `npm run build` : 컴파일
6. `firebase deploy` 배포
   - 문제없을 경우 아래 url로 배포된다.
   - `projectID.web.app`
   - `projectID.firebaseapp.com`