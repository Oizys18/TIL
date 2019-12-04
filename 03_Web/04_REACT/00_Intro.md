# Intro to React

## 개요

https://ko.reactjs.org/

### 정의

- 사용자 인터페이스를 만들기 위한 Javascript 라이브러리

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

- 세가지 방법 중 상황에 맞춰 한가지를 택한다.

- https://ko.reactjs.org/docs/add-react-to-a-website.html

1. 기존 웹사이트에 React 사용

   - 압축 CDN

   ```html
   <script src="https://unpkg.com/react@16/umd/react.production.min.js" crossorigin></script>
   <script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js" crossorigin></script>
   ```

2. 기존 웹사이트에서 JSX를 통해 React 사용

   - JSX CDN

   ```html
   <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
   ```

   - 이후 `<script>` 태그에서 `type="text/babel"` 추가 시 JSX 사용 가능
   - 단, 이 방법은 사이트를 느리게 만들고 **프로덕션에서는 맞지 않다.** 공부/데모 사이트만을 위해 사용

3. 프로젝트에 JSX 추가하기

   a. `Node.js` 설치

   b. 프로젝트 파일 디렉토리에서,

   - `$ npm init -y`
   - `$ npm install babel-cli@6 babel-preset-react-app@3`

4. JSX 전처리기 실행

   - `src` 폴더 생성
   - `$ npx babel --watch src --out-dir . --presets react-app/prod ` 
   - 자동화된 JSX 감시기가 실행된다.