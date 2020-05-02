# day04 인프라 프로젝트

## 도커
- 참고문헌 
  - https://github.com/cheese10yun/TIL/blob/master/docker/docker-beginner.md
  - http://pyrasis.com/Docker/Docker-HOWTO

### 개요 
- 리눅스에서 제공하는 컨테이너를 이용하여 애플리케이션을 묶어서 실행, 배포 할 수 있게 해주는 오픈 소스 SW
- 개발, 테스트, 서비스 서버 등의 다양한 환경을 쉽게 관리 할 수있게 해줌

### 이미지& 컨테이너
- 서버 구성에 필요한 파일 모음
  - 실행 파일, 라이브러리, 설정 파일
- 이미지를 실행한 형태 == 컨테이너

### 명령어
- `docker -v`: 버전 확인
- `docker run hello-world`: 테스트용 
- `docker ps -a`: 컨테이너 조회
- `docker rm [컨테이너 id/name]`: 컨테이너 삭제
- `docker images`: 이미지 조회
- `docker rmi [이미지 id/tag]` 이미지 삭제
- `docker exec [명령어]`: 컨테이너에 특정 명령어 실행
- `docker restart [컨테이너 id/name]`: 컨테이너 재시작
- `docker build [위치]`: 도커 이미지 빌드 


# 도커 공부 계획
- 2020.05.02
- 책 구매, 매일 1단원