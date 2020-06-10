# Web 상식

## Browser storage

`Application - storage`

- `session storage `
  - 브라우저가 켜진 상태까지만 지속되는 저장소
  - ex) 로그인 정보, 
- `local storage`
  - 브라우저가 닫혀도 지속되는 저장소

## LocalStorage API (Web api)

- https://developer.mozilla.org/ko/docs/Web/API/Window/localStorage

- localStorage는 string으로 저장하기 때문에 데이터 처리를 해야 합니다.
  - 저장할 때 : JSON.stringify 
  - 읽을 때 : JSON.parse

```js
// Create
localStorage.setItem('key','value')

// Read
localStorage.getItem('key')

// Update
localStorage.setItem('existingKey','newValue')

// Delete
localStorage.removeItem('key')

// Count
localStorage.length
```

## Declarative Programming 

- 선언형 프로그래밍(== Descriptive Programming)

- 내가 만드려는 것을 묘사하면 자동으로 만들어주는 것

  - `Reactive Programming ` : 데이터 변화에 반응 (자동 적용/반영)
  - `Responsive Programming` : device 화면크기에 반응



## 멈추지 않고 기다리기(Non-blocking)와 비동기(Asynchronous) 그리고 동시성(Concurrency)
https://tech.peoplefund.co.kr/2017/08/02/non-blocking-asynchronous-concurrency.html

## Event Loop

## Bundler 

## Framework

## Architecture

## SSR(Server Side Rendering) vs CSR(Client Side Rendering)
- https://blog.martinwork.co.kr/devops/2019/05/24/server-side-rendering01.html
- https://medium.com/aha-official/%EC%95%84%ED%95%98-%ED%94%84%EB%A1%A0%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EA%B8%B0-1-spa%EC%99%80-ssr%EC%9D%98-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EA%B7%B8%EB%A6%AC%EA%B3%A0-nuxt-js-cafdc3ac2053
- https://brownbears.tistory.com/411
## SPA vs MPA





## 에러핸들링 
```
There might be a problem with the project dependency tree.
It is likely not a bug in Create React App, but something you need to fix locally.

The react-scripts package provided by Create React App requires a dependency:

  "webpack": "3.10.0"

Don't try to install it manually: your package manager does it automatically.
However, a different version of webpack was detected higher up in the tree:
```
- react-start-app으로 생성한 프로젝트를 `yarn start` 하려고 했을 때 발생.
- webpack 버전의 문제지만, yarn이 함께 제시한 방법을 모두 사용해봐도 해결 불가했음
- `.env`를 root에 생성후 `SKIP_PREFLIGHT_CHECK=true`를 추가하면 해결된다. 


## 프론트 체크리스트 
- https://github.com/kesuskim/Front-End-Checklist
- 배포 전 확인해야할 좋은 내용들이 들어있다.
- 또한 google chrome lighthouse 기능도 좋음..!