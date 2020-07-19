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

## OSI  7 layer 계층

- OSI 7 Layer이란 통신 접속에서 완료까지의 과정을 7단계로 정의한 국제 통신 표준 규약

![img](https://t1.daumcdn.net/cfile/tistory/995EFF355B74179035)

- 1계층 - 물리계층(Physical Layer)
  -  전송하는데 필요한 기능을 제공. 장비로는 통신 케이블, 허브가 존재한다.
- 2계층 - 데이터 링크계층(DataLink Layer)
  - 송/수신을 확인. MAC Address를 가지고 통신. 장비로는 브릿지와 스위치가 존재한다.
- 3계층 - 네트워크 계층(Network Layer)
  - 패킷을 네트워크 간의 IP를 통하여 데이터를 전달, 장비로는 라우팅이 존재한다.
- 4계층 - 전송 계층(Transport Layer)
  - 두 호스트 시스템으로부터 발생하는 데이터의 흐름을 제공한다.
- 5계층 -세션 계층(Session Layer) 
  -  통신 시스템 사용자간의 연결을 유지 및 설정한다.
- 6계층 - 표현 계층(Presentation Layer)
  - 세션 계층 간의 주고받는 인터페이스를 일관성 있게 제공한다.
- 7계층 - 응용 계층(Application Layer)
  -  사용자가 네트워크에 접근할 수 있도록 서비스를 제공한다.



## TCP/IP 프로토콜 스택 4계층

- LINK 계층
  - 물리적인 영역의 표준화에 대한 결과. 가장 기본이 되는 영역으로 LAN, WAN, MAN과 같은 네트워크 표준과 관련된 프로토콜을 정의하는 영역.
- IP 계층
  - 경로검색을 해주는 계층. IP 자체는 비연결지향적이며 신뢰할 수 없는 프로토콜이다. 데이터를 전송할 때마다 거쳐야 할 경로를 선택해주지만, 그 경로는 일정치 않다. 특히 데이터 전송 도중에 경로상에 문제가 발생하면 다른 경로를 선택해 주는데, 이 과정에서 데이터가 손실되거나 오류가 발생하는 등의 문제가 발생한다고 해서 이를 해결해주지 않는다. 즉, 오류발생에 대한 대비가 되어있지 않은 프로토콜이다.
- TCP/UDP(전송) 계층
  - 데이터의 실제 송수신을 담당한다. UDP는 TCP에 비해 상대적으로 간단하며, TCP는 신뢰성 있는 데이터의 전송을 담당한다. 그런데 TCP가 데이터를 보낼 때 기반이 되는 프로토콜이 IP이다. 앞서 말했듯이 IP 계층은 문제가 발생한다면 해결해주지 않는 신뢰되지 않은 프로토콜이다. 그 문제를 해결해 주는 것이 TCP. 데이터가 순서에 맞게 올바르게 전송이 갔는지 확인을 해주며 대화를 주고받는다. 확인절차를 걸쳐서 신뢰성 없는 IP에 신뢰성을 부여한 프로토콜이라 생각하면 됨.
- APPLICATION 계층
  - 이러한 서버와 클라이언트를 만드는 과정에서 프로그램의 성격에 따라 데이터 송수신에 대한 약속(규칙)들이 정해지기 마련인데, 이를 가리켜 Aplication 프로토콜이라한다.

## TCP

- TCP 서버의 함수호출 순서 : socket() 소켓생성 -> bind() 소켓 주소할당 -> listen() 연결요청 대기상태 -> accept() 연결허용 -> read()/write() 데이터 송수신 -> close() 연결종료
- TCP 클라이언트의 함수호출 순서 : socket() 소켓생성 -> connect() 연결요청 -> read()/write() 데이터 송수신 -> close() 연결종료
- 서버와 클라이언트의 차이점은 ‘연결요청’이라는 과정이다. 이는 클라이언트 소켓을 생성한 후에 서버로 연결을 요청하는 과정. 서버는 listen()를 호출한 이후부터 연결요청 대기 큐를 만들어 놓는다. 따라서 그 이후부터 클라이언트는 연결요청을 할 수 있다. 이 때, 서버가 바로 accept()를 호출할 수 있는데 이때는, 연결되기 전까지 호출된 위치에서 블로킹 상태에 놓이게 된다.
- 3-way handshaking : TCP 소켓은 연결설정 과정에서 총 세번의 대화를 주고 받는다.
  - SYN :: Synchronize Sequence Number 연결 요청 플래그
  - ACK :: Acknoledgement 응답
  - 클라이언트는 서버에 접속을 요청하는 SYN(M) 패킷을 보낸다. 
  - 서버는 클라이언트의 요청인 SYN(M)을 받고 클라이언트에게 요청을 수락한다는 ACK(M+1)와 SYN(N)이 설정된 패킷을 발송한다.
  - 클라이언트는 서버의 수락 응답인 ACK(M+1)와 SYN(N) 패킷을 받고 ACK(N+1)를 서버로 보내면 연결이 성립된다.
  - 클라이언트가 연결을 종료하겠다는 FIN플래그를 전송한다.
  - 서버는 클라이언트의 요청(FIN)을 받고 알겠다는 확인 메세지로 ACK를 보낸다. 그리고나서는 데이터를 모두 보낼 때까지 잠깐 TIME_OUT이 된다.
  - 데이터를 모두 보내고 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 FIN플래그를 전송한다.
  - 클라이언트는 FIN 메세지를 확인했다는 메세지(ACK)를 보낸다.
  - 클라이언트의 ACK 메세지를 받은 서버는 소켓 연결을 Close한다.
  - 클라이언트는 아직 서버로부터 받지 못한 데이터가 있을 것을 대비해 일정 시간 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정을 거친다. (TIME_WAIT)

## UDP

- UDP는 TCP의 대안이며, IP와 함께 쓰일 때에는 UDP/IP라고 표현하기도 한다.
- TCP와 마찬가지로 실제 데이터 단위를 받기위해 IP를 사용한다. 그러나 TCP와 달리, 메세지를 패킷으로 나누고, 반대편에서 재조립하는 등의 서비스를 제공하지 않는다. 즉, 여러 컴퓨터를 거치지 않고 데이터를 주고 받을 컴퓨터끼리 직접 연결하고자 할때 UDP를 사용한다.
- UDP를 사용해서 목적지(IP)로 메세지를 보낼 수 있고, 컴퓨터를 거쳐서 목적지까지 도달할 수도 있다. 허나 도착하지 않을 수도 있다. 정보를 받는 컴퓨터에서는 포트를 열어두고 패킷이 올 때까지 기다리며 데이터가 온다면 모두 다 받아들인다. 패킷이 도착했을 때 출발지에 대한 정보(IP, PORT)를 알 수 있다.
- UDP는 이러한 특성 때문에 안정적이지 않은 프로토콜이다. 하지만 TCP에 비해서 속도가 빠른편이기에 데이터의 유실이 일어나도 큰 상관이 없는 스트리밍이나 화면전송에 사용된다.

 ## Multi-Thread 서버

- 듣기 소켓을 통해서 새로운 클라이언트가 들어오면 fork(:2) 함수를 이용해서 자식 프로세스를 만드는 대신에, pthread_create(:3) 함수를 이용해서 새로운 스레드를 만드는 것이다. 이 스레드는 문맥을 포함한 코드 조각으로 듣기 소켓의 소켓 지정 번호를 매개 변수로 받아들일 수 있다. 이 듣기 소켓을 이용해서 클라이언트를 처리하는 식이다.
- 핵심은 서버 프로그램이 듣기 소켓과 연결 소켓이 분리되어 있는데, 듣기 소켓에 클라이언트 연결이 들어와서 연결 소켓이 만들어 지면, 스레드를 만들어 클라이언트 요청을 처리하는데 있다. (대리자)
- 스레드는 코드 조각이므로 프로세스를 복사하는 멀티 프로세스 방식보다 좀 더 작고 빠르게 작동하는 프로그램을 만들 수 있다. 반면 독립된 프로세스 단위로 구동되지 않기 때문에, 디버깅이 힘들다는 단점이 있다. 또한 하나의 스레드에 생긴 문제가 전체 프로세스에 문제를 줄 수 있다는 문제점도 있다.



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



## Bundler 
- 최신 웹 어플리케이션 개발 환경에서 속도 저하의 가장 큰 원인은 HTTP request이다. 따라서 가능하면 요청을 최대한 적게, 모두 합쳐서 보내고 받는 것이 좋다.
- 하지만 개발자 입장에서 HTML, JS, CSS 등 여러 파일을 분리하여 관리하는 것이 가독성 측면에서 필요하다. 
- 이런 고민을 해결해 줄 수 있는 것이 번들러입니다. 번들러는 지정한 단위로 파일들을 하나로 만들어서 요청에 대한 응답으로 전달할 수 있은 환경을 만들어주는 역할을 합니다. (어떤 면에서는 컴파일러와 닮아 있기도 하지만 이렇게 합쳐진 파일이 실행되는 것은 여전히 스크립트 방식일 것입니다. )

- 예시
  - webpack
  - Parcel
  - Rollup

## Framework vs Library
- 코드 주체성이 어느 쪽에 있는 지에 달려있다. 
- 프로젝트에 특정 *기능*이 필요해서 import 후 추가했다면 Library 
- 프로젝트 코드 규칙이 이미 정해져있고, 그것에 따라 코드를 작성해야한다면 Framework 
- 단, 최근 모호해지는 경향이 있다. (ex - React) 

## SSR(Server Side Rendering) vs CSR(Client Side Rendering)
- https://blog.martinwork.co.kr/devops/2019/05/24/server-side-rendering01.html
- https://medium.com/aha-official/%EC%95%84%ED%95%98-%ED%94%84%EB%A1%A0%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EA%B8%B0-1-spa%EC%99%80-ssr%EC%9D%98-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EA%B7%B8%EB%A6%AC%EA%B3%A0-nuxt-js-cafdc3ac2053
- https://brownbears.tistory.com/411


## Heading Space


## SPA vs MPA


## Architecture




## 참조링크들 
[SGML]:https://ko.wikipedia.org/wiki/SGML
[HTML]:https://ko.wikipedia.org/wiki/HTML
[XML]:https://ko.wikipedia.org/wiki/XML
[W3C]:https://ko.wikipedia.org/wiki/W3C