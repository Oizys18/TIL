# day05

## 1) 캐싱

- 캐시는 컴퓨터 과학에서 데이터나 값을 미리 복사해 놓는 임시 장소를 가리킨다. 캐시는 캐시의 접근 시간에 비해 원래 데이터를 접근하는 시간이 오래 걸리는 경우나 값을 다시 계산하는 시간을 절약하고 싶은 경우에 사용한다

### DB 캐시

- Mapper 프레임워크 등에서 제공하는 캐시는 성능 및 제어에 문제가 많다.
- DB뿐만 아니라 병목이 예상되는 일반적인 데이터 캐싱을 위해 범용 데이터 캐싱 솔루션이 필요하다.

### Redis

- 오픈 소스 소프트웨어
- NoSQL & Cache 솔루션, 메모리 기반 구성
- DB로 사용될 수 있으며 Cache로도 사용될 수 있는 기술이다. 

## 2) 시스템 아키텍쳐 구성도

- WAS와 DB 간의 통신에서 병목이 발생할 것 이라고 예상한다. 
  - 특히 현재 구조 특성상 영화 상세정보 페이지에서 불필요한 요청이 많이 발생한다.
- 선정이유
  1. 각 유저 별로 영화 데이터를 최소 1개에서 최대 100개 까지 요청한다.
  2. 유저가 확인하는 영화 상세정보 데이터는 모두 동일하기 때문에 최적화가 효과적일 것이라고 판단했다.

## 3) 공통 프로젝트 소스 

```python
from django.core.cache import cache
@api_view(['GET'])
def movies(request):
    # 모든 샘플 데이터가 있는 movies_all을 get, 없으면 set 한다.
    movies_all = cache.get_or_set('movies_all', Movie.objects.all())
    serializer = MovieSerializer(movies_all, many=True)
    return Response(serializer.data)
```

## 4) Django Backend에 Redis 적용하기

#### 개요 

- 공통프로젝트의 백엔드는 Java Spring으로 구성되었기 때문에 1학기 최종프로젝트인 Django 백엔드로 진행했다. 

#### 목표

- 요청/응답에 가장 많은 시간이 걸리는 구간을 선택한다.
- `loadtest`라이브러리를 사용하여 시간을 체크한다.
- Redis 적용 후 시간을 체크하여 비교한다.

#### 과정

#### 1) redis 적용할 구간 선택

- DB의 모든 영화상세정보를 읽어오는 페이지 (http://127.0.0.1/api/v1/movies)

#### 2) redis 적용 전 request 시간 체크 

- 100개의 요청을 보냈을 시,
  - mean latency: 973.5ms
  - Total time: 97.35s
  - Total error: 0
  - Longest request: 1987ms
- 각 요청마다 모든 데이터를 읽어오기 때문에 너무 많은 시간이 소요된다.

#### 3) redis 적용 

1. 프로젝트 venv 접속 후 `pip install django-redis`로 redis 설치

2. `settings.py`에 CACHE 추가

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',   
       },
   }
   ```

3. request 를 보낸 후 redis-cli에서 SELECT 1 로 1번 데이터베이스로 접속
4. GET * 

#### 4) redis 적용 후 시간 체크

- 동일하게 100개의 요청을 보냈을 시,
  - mean latency: 2.7 ms
  - Total time: 2.7 s
  - Total error: 0
  - Longest request: 525ms
- 동일한 100개의 데이터를 조회하기 때문에, 실제 DB에서 데이터를 읽어오는 제일 처음  request가 Longest request인 525ms일 것 같고 나머지는 caching을 통해서 데이터를 바로 가져오기 때문에 속도가 많이 줄었다. 

#### 결론

- 동일한 데이터의 read가 빈번하게 발생하는 경우 caching을 적극적으로 활용하여 최적화를 진행해야겠다. 