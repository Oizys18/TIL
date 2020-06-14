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

### Virtual DOM 
- 기존의 `Real DOM` 구조는 정적으로 서버와 통신하여 요청을 주고 받으면 받은 데이터를 DOM 객체에 속성 값, text를 변화,생성,제거 하도록 만들어졌다. 이 때 코드는 계속해서 DOM 객체의 CRUD 코드를 반복해서 생성한다. DOM 객체의 연산을 연속적으로 하게 됨에 따라 컴퓨터 자원을 많이 소모하게 되었고, 특히 SPA 모델의 웹 어플리케이션을 만들 경우 많은 개발 부채를 불러오게 된다. 
- 따라서 위와 같은 컴퓨터 자원 낭비를 줄이기 위해 `REACT`는 real DOM의 추상화 개념을 활용한 새로운 DOM을 사용하는데, 이것이 `Virtual DOM` 이다.
- Real DOM과 비교했을 때 Virtual DOM은 동적이며, 생명주기가 존재하며, 특히 SPA 웹 앱을 개발할 때 훨씬 더 좋은 성능을 발휘한다. (단, 만약 Dynamic UI 웹 앱이 아닌 이전 트렌드의 웹 앱같은 경우 일반 DOM의 성능이 더 좋다.)


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
- 싱글 스레드 언어인 자바스크립트는 스택에 쌓인 함수들에서 어떠한 값을 반환하기 전까지는 즉각적인 반응을 보여줄 수 없다. 즉 즉각적인 반응이 필요할 때 스택이 막혀있다면 아무런 반응을 볼 수가 없다.
- 따라서 싱글 스레드인 자바스크립트에서 유동적인 UI를 만들기 위해 비동기함수를 사용한다.
- 비동기 콜백 == 코드의 일정 부분을 실행시키고 나중에 실행될 콜백함수를 스택에 넣는 것 (AJAX)
- 모든 비동기 콜백들은 코드에서 읽힌 순간 실행되지 않고, 잠시 후에 실행된다.
  - == 동기 함수들과는 다르게 바로 스택 내부로 push되지 않는다.

- 이벤트 루프가 하는 일?
  - 이벤트 루프는 큐에서 콜백을 실행하고 스택이 비어있을때 스택에 넣는다. 이벤트 루프의 기본 작업은 스택과 작업 큐를 모두 보고 스택이 비어있을때 큐의 첫번째 작업을 스택에 넣는 것이다. 각 메시지 또는 콜백은 다른 메시지가 처리되기 전에 완전히 처리된다.

- 콜백 함수의 호출은 호출 스택의 초기 프레임으로 사용되며 JavaScript가 단일 스레드이므로 스택의 모든 호출이 반환 될 때까지 추가 메시지 폴링 및 처리가 중단됩니다. 후속 (동기식) 함수 호출은 스택에 새로운 호출 프레임을 추가합니다.

  - `폴링`
  - 통신에서, "폴링"은 한 프로그램이나 장치에서 다른 프로그램이나 장치들이 어떤 상태에 있는지를 지속적으로 체크하는 전송제어 방식으로서, 대체로 그들이 아직도 접속되어 있는 지와 데이터 전송을 원하는지 등을 확인한다.

## Bundler 
- 최신 웹 어플리케이션 개발 환경에서 속도 저하의 가장 큰 원인은 HTTP request이다. 따라서 가능하면 요청을 최대한 적게, 모두 합쳐서 보내고 받는 것이 좋다.
- 하지만 개발자 입장에서 HTML, JS, CSS 등 여러 파일을 분리하여 관리하는 것이 가독성 측면에서 필요하다. 
- 이런 고민을 해결해 줄 수 있는 것이 번들러입니다. 번들러는 지정한 단위로 파일들을 하나로 만들어서 요청에 대한 응답으로 전달할 수 있은 환경을 만들어주는 역할을 합니다. (어떤 면에서는 컴파일러와 닮아 있기도 하지만 이렇게 합쳐진 파일이 실행되는 것은 여전히 스크립트 방식일 것입니다. )

- 예시
  - webpack
  - Parcel
  - Rollup

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