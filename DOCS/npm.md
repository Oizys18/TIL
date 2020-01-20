# NPM(Node Package Manager)

## 개요 
- Node : node.js
- Pakckage : 모듈(프로그램보다는 조금 작은 단위)
- Manager : 관리자
- 즉, Node.js로 만들어진  package(module)을 관리해주는 툴

## 명령어 모음
- `npm install 모듈`: 모듈 설치
- `npm init`: package.json 생성
- `npm install`: package.json 파일 및 해당 종속성에 나열된 모든 모듈을 설치
- `npm update`: 설치한 패키지를 업데이트
- `npm whoami`: 자신의 아이디를 알려준다.
- `npm run`: sciprts를 실행하는 명령어
- `npm start` 
  - package.json의 scripts에 있는 start명령어를 실행하는 부분
  - 만약 start 명령어를 따로 설정하지 않았다면 node server .js가 실행됨