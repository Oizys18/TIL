# REST API

## RESTful API - CRUD

https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

- REST: “Representational State Transfer” 의 약자
  자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다
- **HTTP URI(Uniform Resource Identifier)**를 통해 자원(Resource)을 명시하고, **HTTP Method(POST, GET, PUT, DELETE)**를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
- 장점
  1. 백엔드와 프론트엔드의 완전한 분리가 가능
  2. 정보 송수신이 자유로워져 생산성이 급격하게 상승
  3. 코드의 재사용성이 높아짐 



### Music : Comment == 1 : N

```python
# Music REST API
C			POST	/musics/
R(list)		GET		/musics/
R(detail)	GET		/musics/:pk
     /
U			PUT		/musics/:pk/
D			DELETE	/musics/:pk/

# Comment REST API -> 모두 하나의 music에 대한 Comment, music_pk에 dependant
C			POST	/musics/:pk/comments/
R(list)		GET		/musics/:pk/comments/
R(detail)	GET		/musics/:pk/comments/:pk
U			PUT		/musics/:pk/comments/:pk
D			DELETE	/musics/:pk/comments/:pk
```


## 프론트 엔드가 신경 안쓸 수 있게 만들자..