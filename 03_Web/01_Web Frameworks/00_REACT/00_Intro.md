# Intro to React

## 개요

https://ko.reactjs.org/

### 정의

- 사용자 인터페이스를 만들기 위한 Javascript 라이브러리(엄밀히 말하면 공식적으로는 프레임워크가 아니다!)

<hr>

### 특징

#### 1. 선언형

- App의 각 상태에 대한 뷰를 설계 -> 데이터의 변경에 따라 컴포넌트만 효율적으로 갱신/렌더링
- 선언형 뷰는 코드를 **예측 가능하게**, **디버깅하기 쉽게** 만들어 준다.

#### 2. 컴포넌트 기반

- 스스로 상태를 관리
- 템플릿이 아닌 Javascript로 작성
- DOM과 별개로 상태관리 가능

#### 3. 재사용성

- Node 서버에서 렌더링 가능
- React Native를 이용해 모바일 앱 생성 가능

#### **JSX 사용 권장**

- https://reactjs-kr.firebaseapp.com/docs/introducing-jsx.html

- JS의 문법 확장, React **요소**를 만드는 태그 문법

<hr>

### 준비사항

- 상황에 맞춰 한가지를 택한다.

- https://ko.reactjs.org/docs/add-react-to-a-website.html

#### 기존 웹사이트에 React 사용

1. 기존 웹사이트에서 JSX를 통해 React 사용

   - JSX CDN

   ```html
   <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
   ```

   - 이후 `<script>` 태그에서 `type="text/babel"` 추가 시 JSX 사용 가능
   - 단, 이 방법은 사이트를 느리게 만들고 **프로덕션에서는 맞지 않다.** 공부/데모 사이트만을 위해 사용

2. 프로젝트에 JSX 추가하기

   a. `Node.js` 설치

   b. 프로젝트 파일 디렉토리에서,

   - `$ npm init -y`
   - `$ npm install babel-cli@6 babel-preset-react-app@3`

3. JSX 전처리기 실행

   - `src` 폴더 생성
   - `$ npx babel --watch src --out-dir . --presets react-app/prod`
   - 자동화된 JSX 감시기가 실행된다.

#### CDN 링크 사용

- 압축 CDN

```html
<script
  src="https://unpkg.com/react@16/umd/react.production.min.js"
  crossorigin
></script>
<script
  src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"
  crossorigin
></script>
```

#### React App 생성

- Single page application을 생성한다.

```javascript
npx create-react-app my-app
cd my-app
npm start
```

## VS Code 추천 익스텐션
- 김신재님 참고

1. **ES7 React/Redux/GraphQL/React-Native snippets**

   React 개발한다면 그냥 국룰.

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/696b2e78-69d1-46ae-89b4-e10f5d45eedf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/696b2e78-69d1-46ae-89b4-e10f5d45eedf/Untitled.png)

2. **Reactjs code snippets**

   얘도 그냥 국룰. **ES7 React/Redux/GraphQL/React-Native snippets** 서브.

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/737bccb9-6c56-41b4-8ab2-ecca8711cdc5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/737bccb9-6c56-41b4-8ab2-ecca8711cdc5/Untitled.png)

3. **JS JSX Snippets**

   얘도 서브. JSX 문법 자동완성 안되면 이것도 설치.

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2989623a-8a40-48f3-9a0c-d1ff9e5f8a5d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2989623a-8a40-48f3-9a0c-d1ff9e5f8a5d/Untitled.png)

4. **ESLint**

   JS 개발한다면 그냥 국룰.

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/541ecb1c-df5a-482a-bedf-5c7b72220579/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/541ecb1c-df5a-482a-bedf-5c7b72220579/Untitled.png)

5. **JavaScript (ES6) code snippets**

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7258b86e-f458-4fe8-97b0-e345a6c0070b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7258b86e-f458-4fe8-97b0-e345a6c0070b/Untitled.png)

6. **Debugger for Chrome**

   구글 크롬과 통합된 디버깅 환경을 제공하는 익스텐션

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2185f02c-a91b-4743-882d-7aab5336657b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2185f02c-a91b-4743-882d-7aab5336657b/Untitled.png)

7. **vscode-styled-components**

   이거는 디자인할 때, 일반적인 css나 scss 대신 styled-components를 사용한다면 쓰기 좋은거.

   ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/98c11f8a-da37-4431-b3cd-12e6f12e575e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/98c11f8a-da37-4431-b3cd-12e6f12e575e/Untitled.png)

---

## +α) 구글 확장 프로그램

- **React Developer Tools**

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3f0f849-ea59-4525-b692-1cd4490d51fc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3f0f849-ea59-4525-b692-1cd4490d51fc/Untitled.png)

  _react_ 컴포넌트 구조와 `props`, `state`를 크롬 DevTools에서 확인할 수 있게 해준다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab527d36-ed8a-40e9-ab9c-01f52884fb31/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab527d36-ed8a-40e9-ab9c-01f52884fb31/Untitled.png)
