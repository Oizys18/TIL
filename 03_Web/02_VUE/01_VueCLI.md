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