# 이벤트 루프 

![img](https://camo.githubusercontent.com/cb15c3924ce957b8c91ffa9d0c6276ce884b6203/68747470733a2f2f643676646d61393136366c64682e636c6f756466726f6e742e6e65742f6d656469612f696d616765732f39616163626364302d343463352d343565312d623365622d6265383461326562393964382e706e67)

- 메시지 큐에 더 많은 메시지가 있는지 확인하는 루프
- Javascript에서 비동기화를 허용하는 기본 모델
- 끊임없이 호출 스택이 비었는지에 대한 검사를 실행하는 프로세스(콜 스택이 비어 있으면 호출 대기 중인 함수가 있는지 확인한다.)
- 모든 요청마다 새 스레드가 생성되는 스레드 모델과 달리 단일 스레드에서 실행되므로 오버헤드가 발생하지 않는다.
- 특징
  - 동시성(Concurrency)
    - 자바스크립트 **런타임은 한 번에 한 가지만 할 수 있고**, 다른 코드를 실행하는 동안에는 Ajax 호출을 할 수 없으며, 다른 코드를 실행하는 동안에는 setTimeout 할 수 없지만 **브라우저를 통해 이 모든 것을 할 수 있다.** 브라우저를 사용하면 다른 코드를 실행하는 동안 Ajax 호출을 할 수 있으며 다른 코드를 실행하는 동안 setTimeout을 할 수도 있다.
    - setTimeout을 하고 Ajax 요청을 하는 것은 Javascript 런타임에 있는 것이 아니라 브라우저가 웹 API로 처리한다. 브라우저는 이러한 것들의 처리과정에 대해 알고 있으며 그것의 콜백 함수를 통해 결과를 얻을 수 있다.
  - 비동기성 (asynchronous)

```javascript
setTimeout(function doSomething() {
  // Do stuff.
}, 0);
// 함수 호출 후 0ms 이후 실행되는 것이 아니라, 최소 0ms 후에 실행되는 것이다. 
```

## 요약
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


### Non-blocking I/O

- 자바스크립트에서 거의 모든 I / O는 차단되지 않습니다.(non-blocking) 여기에는 HTTP 요청, 데이터베이스 작업 및 디스크 읽기 및 쓰기가 포함됩니다. 실행의 single-threaded는 런타임에 작업을 수행하도록 요청하고 콜백 기능을 제공한 다음 다른 작업을 수행하도록 이동합니다. 작업이 완료되면 제공된 콜백 기능과 함께 메시지가 대기열에 포함됩니다. 앞으로 어떤 시점에서 메시지는 대기열에서 제외되고 콜백이 시작됩니다.

### The Event Loop

- 비동기 작업이 완료되고 콜백이 시작될 때까지 기다리는 동안 자바스크립트 런타임에서 다른 작업을 수행 할 수 있습니다.
- 자바스크립트 런타임에는 처리 할 메시지 목록과 관련 콜백 함수를 저장하는 메시지 대기열이 있습니다. 
- 루프에서 대기열은 다음 메시지 ( 각 polling을 "tick"이라고 함)에 대해 polling되고 메시지가 발생하면 해당 메시지에 대한 콜백이 실행됩니다.
- 이 콜백 함수의 호출은 호출 스택의 초기 프레임으로 사용되며 JavaScript가 single-threaded이므로 스택의 모든 호출이 반환 될 때까지 추가 메시지 polling 및 처리가 중단됩니다.(루프가 순환하는 동안 웹 페이지를 클릭하면 클릭 처리기가 즉시 실행되지 않습니다. 대신 메시지 대기열에 추가됩니다.) 
- 후속(동기)함수 호출은 새로운 호출 프레임을 스택에 추가합니다. 

### Queuing Additional Messages

- 이벤트(DOM 요소, XMLHttpRequest, 서버 보낸 이벤트 등) 
- setTimeout 및 setInterval

```javascript
  function f() {
    console.log("foo"); // 1
    setTimeout(g, 0); // callback 대기열 (메세지큐에 추가)
    console.log("baz"); // 2
    h(); // callstack
  }

  function g() {
    console.log("bar"); // 4, 이벤트 루프에서 callstack으로 
  }

  function h() {
    console.log("blix"); // 3  
  }

  f();

// foo -> baz -> blix -> bar 
```

### Web Workers

- Web Workers를 사용하면 별도의 실행 스레드로 분산하여 메인 스레드를 자유롭게하여 다른 작업을 수행 할 수 있습니다. 
- Worker는 별도의 메시지 대기열, 이벤트 루프 및 이를 인스턴스화 한 원래 스레드와 별개의 메모리 공간을 포함합니다. 
- Worker와 주 스레드 간의 의사 소통은 메시지 전달을 통해 수행됩니다. 

### 클로저 참고사항

- 자바스크립트의 클로저는 콜백의 실행이 완전히 새로운 콜 스택을 생성하더라도 생성 된 환경에 대한 액세스를 유지하면서 실행할 때 콜백을 등록 할 수있게 해줍니다. 
- 특히 콜백이 생성 된 메시지와 다른 메시지의 일부로 콜백이 호출된다는 사실을 알고 있어야합니다. 

```javascript
  function changeHeaderDeferred() {
    var header = document.getElementById("header"); // 1
    
    setTimeout(function changeHeader() {  // 2 -> 콜백 
      header.style.color = "red"; // 4 -> header가 garbage collection에 수집되지 않고 참고 가능 
      return false; // 5 -> changeHeader(): false 반환  (header garbage collection에 포함됨)
    }, 100);

    return false; // 3 -> changeHeaderDeferred(): false 반환 
  }

  changeHeaderDeferred();
```

### Message Queue

- 콜백 함수들이 실행되기 전 기다리는 대기열 (queue 논리구조)
- call stack이 비어있으면 event loop에 의해 call stack으로 하나씩 옮겨진다.
  - 이러한 반복을 이벤트 루프의 틱 (tick)이라고합니다.

### Job Queue : 작업 대기열

```javascript
const bar = () => console.log('bar')

const baz = () => console.log('baz')

const foo = () => {
  console.log('foo') // 1
  setTimeout(bar, 0) // 4 
  new Promise((resolve, reject) =>
    resolve('should be right after baz, before bar')
  ).then(resolve => console.log(resolve)) // 3
  baz() // 2
}

foo()

// foo -> baz -> should be right after baz, before bar -> bar
```

- ES6, ES2015에서 소개된 Promises가 사용하는 작업 대기열 개념 

- 이벤트 루프 대기열의 맨 위에있는 레이어(이벤트 루프 대기열의 모든 tick의 끝에 첨부되는 대기열)

- 현재 함수가 끝나기 전에 해결되는 약속은 현재 함수 바로 다음에 실행된다. 

- 메시지 큐가 대기열 뒤쪽에 들어간다면 promise는 현재 실행되는 함수 직후에 실행된다. (메시지 큐보다 먼저)

  

## 유지 보수가 가능하고 쉬운 비동기 코드 작성에 관한 5가지 팁

### 1.  깨끗한 코드

```javascript
// `rp` is a request-promise function.
rp('https://api.example.com/endpoint1').then(function(data) {
 // …
});

// `rp` is a request-promise function.
var response = await rp('https://api.example.com/endpoint1');
```

- async  await를 사용하면 훨씬 적은 코드를 작성할 수 있습니다. async를 사용할 때마다 몇 가지 불필요한 단계를 건너 뜁니다. .then을 쓰고, 익명 함수를 만들어 응답을 처리하고, 해당 콜백의 응답 이름을 지정합니다.

### 2. 오류처리

```js
function loadData() {
    try { // Catches synchronous errors.
        getJSON().then(function(response) {
            var parsed = JSON.parse(response);
            console.log(parsed);
        }).catch(function(e) { // Catches asynchronous errors
            console.log(e); 
        });
    } catch(e) {
        console.log(e);
    }
}

async function loadData() {
    try {
        var data = JSON.parse(await getJSON());
        console.log(data);
    } catch(e) {
        console.log(e);
    }
}
```



- Async / await을 사용하면 잘 알려진 try / catch 문과 동일한 코드 구문을 사용하여 동기화 및 비동기 오류를 모두 처리 할 수 있습니다.

### 3. 조건부

```js
function loadData() {
  return getJSON()
    .then(function(response) {
      if (response.needsAnotherRequest) {
        return makeAnotherRequest(response)
          .then(function(anotherResponse) {
            console.log(anotherResponse)
            return anotherResponse
          })
      } else {
        console.log(response)
        return response
      }
    })
}

async function loadData() {
  var response = await getJSON();
  if (response.needsAnotherRequest) {
    var anotherResponse = await makeAnotherRequest(response);
    console.log(anotherResponse)
    return anotherResponse
  } else {
    console.log(response);
    return response;    
  }
}
```



- async / await으로 조건부 코드를 작성하는 것이 훨씬 더 간단합니다.

### 4. Stack Frames

- async / await와는 달리, Promise 체인에서 반환 된 오류 스택은 오류가 발생한 위치를 알 수 없습니다.
  다음을보십시오 :

```js
function loadData() {
  return callAPromise()
    .then(callback1)
    .then(callback2)
    .then(callback3)
    .then(() => {
      throw new Error("boom");
    })
}
loadData()
  .catch(function(e) {
    console.log(err);
// Error: boom at callAPromise.then.then.then.then (index.js:8:13)
});


async function loadData() {
  await callAPromise1()
  await callAPromise2()
  await callAPromise3()
  await callAPromise4()
  await callAPromise5()
  throw new Error("boom");
}
loadData()
  .catch(function(e) {
    console.log(err);
    // output
    // Error: boom at loadData (index.js:7:9)
});
```

### 5. **디버깅** 

- Promise을 사용했다면 디버깅이 악몽이라는 것을 알고 있습니다. 예를 들어 .then 블록 내에 중단 점을 설정하고 "중지"와 같은 디버그 바로 가기를 사용하면 디버거가 동기 코드를 "단계별로"수행하기 때문에 다음으로 이동하지 않습니다.
- async / await을 사용하면 정상적인 동기 함수 인 것처럼 정확히 기다릴 수 있습니다.

