# Deploying, 배포

- DevOps
  - Continuous Intergretion : CI 지속적 통합
  - Continuous  Delivery: CD 지속적 서비스 제공
  
## Django Backend Heroku 배포

- Local PC -> Git remote Repo(Gitlab/Github) **--- Deploy --->** Online Remote Server(Heroku server) 배포

- `PaaS` Platform as a service

### 초기세팅

1. `pip install django-heroku`

2. static file 모으기

   - `settings.py`

   - ```python
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```

   - ```bash
     $ python manage.py collectstatic
     ```

3. 배포용 ignore 추가

   - `settings.py`

   - ```python
     # 배포용 ignore 파일
     venv
     db.sqlite3    #heroku는 PostgreQC쓴다..
     *.sqlite3
     .env
     *.bak
     ```

4. ENV 설정

   - `python-decouple` 필요

   - `pip install python-decouple`

     - `settings.py`의 `SECRET_KEY` env로 옮겨줌

     - ```
       SECRET_KEY='~~원래 django.settings.py에 있던 secret key'
       DEBUG=True
       ```

     - ```
       SECRET_KEY = config('SECRET_KEY')
       DEBUG = config('DEBUG')
       ```

5. Heroku 가입, Heroku CLI 설치

   - https://devcenter.heroku.com/articles/heroku-cli 

   - ```
     $ heroku login
     ```

   - ```
     $ heroku create <app_name>
     ```

   - 이제 `git remote -v`하면 헤로쿠 서버가 보일 것. 

   - heroku 웹사이트 들어가서 추가

     - Settings
     - Config Vars
       - SECRET_KEY = "~~~"
       - DEBUG = True

6. **`django-heroku`** **패키지 설치**

   ```
   // settings.py
   import django_heroku
   django_heroku.settings(locals())
   ```

7. 필요 파일 추가

   - `runtime.txt`

     ```
     python-3.7.4
     
     ```

   - `Procfile`

     ```
     web: gunicorn [프로젝트_이름].wsgi --log-file -
     
     ```

   - `gunicorn` 설치

     - `$ pip install gunicorn`

   - `requirements.txt`

     - `$ pip freeze > requirements.txt`

8. allowed hosts에 heroku 서버 넣기

9. 배포

   - `git push heroku master`

10. heroku서버에서 makemigrations , migrate


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

4. `firebase init`
   - firebase deploy 디렉토리는 `dist`를 입력한다 
   - `dist`는 complie된 배포용 파일이 위치할, 곧 생성될 디렉토리
   - 프로젝트와 연결
   - 공개용 루트 디렉터리로 사용할 디렉터리를 지정합니다.
     - 보통 `index.html`, 
   - 사이트 구성 선택 (SPA의 경우 Y)

5. `firebase deploy` 배포
   - 문제없을 경우 아래 url로 배포된다.
   - `projectID.web.app`
   - `projectID.firebaseapp.com`
     