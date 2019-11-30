# Deploying, 배포

## Django to Heroku

- Local PC -> Git remote Repo(Gitlab/Github) **--- Deploy --->** Online Remote Server(Heroku server) 배포

- `PaaS` Platform as a service

### 초기세팅
#### 0. Heroku 가입, Heroku CLI 설치
- https://devcenter.heroku.com/articles/heroku-cli 
#### 1. 필요 패키지 설치

##### `django-heroku` 설치
- https://github.com/heroku/django-heroku  
- `pip install django-heroku`
- 기능
  - Settings configuration (Static files / WhiteNoise). 
  - Logging configuration.
  - Test runner (important for Heroku CI).
  - `DATABASE_URL`, `ALLOWED_HOSTS`, .env에 `SECRET_KEY` 변수명으로 추가된 SECRET_KEY를 자동으로 추가한다.
  
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

##### `gunicorn` 설치
- `$ pip install gunicorn`


#### 2. static file 모으기

- Django app `settings.py`
- `STATIC_ROOT` 설정
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
- collect static files 
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


#### 4. heroku cli 이용, app과 연결
- `$ heroku login`
  - pop up webpage에서 로그인
- `$ heroku create <app_name>`
  - app_name으로 heroku 서버 생성
- `git remote -v`를 통해 heroku 서버를 확인한다.

- `$ heroku git:remote -a <app>`
  - 필요하다면, 다른 heroku 서버로 연결한다.

- heroku website의 연결할 서버의 변수설정
  - Settings > Config Vars 
    - SECRET_KEY = "~~~"
    - DEBUG = True




1. allowed hosts에 heroku 서버 넣기

2.  배포

   - `git push heroku master`

11. heroku서버에서 makemigrations , migrate


## Vue CLI Frontend Firebase 배포

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