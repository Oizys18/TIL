# Vue-CLI

- `Django-admin` 처럼 `Vue`를 CLI에서 조작 가능 

- npm을 이용한 설치 (`yarn`사용 가능) 

  - 전역: ` npm install -g @vue/cli `
  - 프로젝트 단위  -  default 
    - `vue --version`

- 프로젝트 디렉토리 생성

  - `vue init <template-name> <project-name>`
    `vue init webpack my-project `

  - ` vue create todo-vue-cli`

    ```
    ?  Your connection to the default npm registry seems to be slow. Use https://registry.npm.taobao.org for faster installation?  >> Yes
    ```

    - 미국에서 제작했기 때문에 중국 타오바오 서버를 통해 빠른 속도로 만들어줌 - `Yes`

  - preset은 `default`

- 프로젝트 톺아보기

  - `babel.config.js`
    - 오래된 브라우저가 새로운 언어/기능을 이해못하면 자동으로 번역(?)해줌 

  - `package.json`
    - 프로젝트에서 사용되는 패키지들 관련 정보
  - `node_modules`
    - 실제 패키지

- 위와 같이 실제 프로젝트에 필요한 데이터는 많은데 (88mb..) 실제 배포 시에는 `build`를 통해 컴파일한다.

  - 그래서 만약 다른 사람의 코드를 받아서 사용하려면 처음 저장 후 `npm install`해야함 


## CLI 사용자 정의 설정
- https://vuejs-kr.github.io/vue/vue-cli/2018/01/27/vue-cli-3/


- 타입스크립트 지원
- 프로그레시브 웹 앱 (PWA) 지원
- Vue Router
- Vuex
- CSS 프리프로세서 (SCSS/SASS, LESS, Stylus)
- ESLint 와 Code Formatter
  - 에러를 일으키는 코드만 lint
  - ESLint + Airbnb
  - ESLint + Standard
  - ESLint + Prettier
- 추가 lint 설정
  - 저장할 때 lint
  - 커밋할 때 lint lint-staged
- 유닛 테스팅 도구
  - Mocha + Chai
  - Jest
- 엔드 투 엔드 테스팅 도구
  - Cypress
  - Nightwatch


## 디렉터리 구조
- dist         # 빌드 결과물, yarn build 전까지 없음
- node_modules # yarn 또는 npm으로 설치한 의존성
- public       # 공용으로 접근 가능한 파일이 위치함
- src          # 애플리케이션 소스코드
- test         # 테스트코드
.gitignore
package.json