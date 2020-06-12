# Web 상식

## HTML (HyperText Markup Language)
- [HTML] 위키백과 
- 최신버전은 HTML5 
- 하이퍼텍스트 마크업 언어
- 구조적 문서의 형태를 띈 웹페이지를 만들 수 있는 방법을 제공하는 마크업 언어
- `< >`로 둘러싸인, `태그`로 되어있는 HTML 요소 형태로 작성한다.
- 웹 브라우저와 같은 HTML 처리 장치의 행동에 영향을 주는 `JS`와 본문과 그 밖의 항목의 외관과 배치를 정의하는 `CSS`와 같은 스크립트를 포함하거나 불러올 수 있다. 

## XML(Extensible Markup Language)
- [XML] 위키백과
- [W3C]에서 개발된, 다른 특수한 목적을 갖는 마크업 언어를 만드는데 사용하도록 권장하는 다목적 마크업 언어 
- [SGML]의 단순화된 부분집합으로, 다른 많은 종류의 데이터를 기술하는 데 사용할 수 있다. 주로 다른 종류의 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 [HTML]의 한계를 극복할 목적으로 만들어졌다.


## DOM (Documnet Object Model) 문서 객체 모델 
- [XML]이나 [HTML] 문서에 접근하기 위한 인터페이스
- 웹 문서는 텍스트 파일로 만들어져있어서, 브라우저가 이해할 수 있는 구조로 메모리에 올리려면 가공이 필요하다. 브라우저의 렌더링 엔진은 웹 문서를 로드한 후, 파싱하여 웹 문서를 브라우저가 이해할 수 있는 구조로 구성하여 메모리에 적재한다. 이렇게 모든 요소와 요소의 어트리뷰트, 텍스트를 각각의 객체로 만들고 이들 객체를 부자 관계를 표현할 수 있는 트리 구조로 구성한 것이 DOM이다. 
- DOM은 자바스크립트를 통해 동적으로 변경할 수 있으며 변경된 DOM은 렌더링에 반영된다.  


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





## 참조링크들 
[SGML]:https://ko.wikipedia.org/wiki/SGML
[HTML]:https://ko.wikipedia.org/wiki/HTML
[XML]:https://ko.wikipedia.org/wiki/XML
[W3C]:https://ko.wikipedia.org/wiki/W3C