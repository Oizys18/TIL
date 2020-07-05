# 26_[Async/Await](https://joshua1988.github.io/web-development/javascript/js-async-await/)

```js
async function 함수명() {
  await 비동기_처리_메서드_명();
}
```

- async와 await는 자바스크립트의 비동기 처리 패턴 중 가장 최근에 나온 문법 (ES2017 `ES8` )
- 내부적으론 비동기 작업을 수행하면서, 표면적으론 완전히 동기식 코드를 작성할 수 있도록 도와준다.
- 기존의 비동기 처리 방식인 콜백 함수와 프로미스의 단점을 보완하고 개발자가 읽기 좋은 코드를 작성할 수 있다.
- 일반적으로 자바스크립트의 비동기 처리 코드는 아래와 같이 콜백을 사용해야 코드의 실행 순서를 보장받을 수 있다.
- 함수 앞에 `async`가 붙으면 항상 `promise`를 리턴한다. 다른 값들은 자동적으로 resolve된 promise로 감싸진다.

```js
// 미적용
function logName() {
  var user = fetchUser('domain.com/users/1');
  if (user.id === 1) {
    console.log(user.name);
  }
}

// 콜백처리 
function logName() {
  // 아래의 user 변수는 위의 코드와 비교하기 위해 일부러 남겨놓았습니다.
  var user = fetchUser('domain.com/users/1', function(user) {
    if (user.id === 1) {
      console.log(user.name);
    }
  });
}

// async & await 적용 후
async function logName() {
  var user = await fetchUser('domain.com/users/1');
  if (user.id === 1) {
    console.log(user.name);
  }
}
```

## 사용법

1.  함수 앞에 `async` 예약어를 붙인다.
2. 함수의 내부 로직 중 HTTP 통신을 하는 비동기 처리 코드 앞에 `await`를 붙인다.
   - 비동기 처리 메서드가 꼭 프로미스 객체를 반환해야 `await`가 의도한 대로 동작합니다.
   - 일반적으로 `await`의 대상이 되는 비동기 처리 코드는 [Axios](https://github.com/axios/axios) 등 프로미스를 반환하는 API 호출 함수입니다.

## 작동방식

1. `async`함수가 호출되면 [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)가 반환됩니다.
2.  `async`함수가 값을 반환하면 `Promise`는 반환 된 값으로 해결됩니다. 
3. `async`함수가 예외 또는 일부 값을 throw하면 `Promise`는 throw된 값과 함께 거부됩니다.

- `async`함수는 [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)표현식을 포함 할 수 있으며, `async`함수의 실행을 일시 중지하고 전달된 `Promises`를 기다린 다음 `async`함수의 실행을 재개하고 해결 된 결과를 리턴합니다.



## 예외처리

-  [try catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)를 사용한다.
- 프로미스에서 에러 처리를 위해 `.catch()`를 사용했던 것처럼 async에서는 `catch {}` 를 사용하면 된다.
- 오류 처리가 완전히 동기적으로 수행된다. 



## Async

```js
async function f() {
  return 1;
}
```

- 함수 앞의 `async` 단어는 한가지 뜻을 지닌다: 이 함수는 항상 promise를 리턴합니다. 다른 값들은 자동적으로 resolve된 promise로 감싸집니다.
- `await` 은 오직 `async` 함수 안에서만 동작한다.

## Await

```js
// works only inside async functions
let value = await promise;
```

- `await` 키워드는 자바스크립트가 promise가 셋팅되고 그 결과 값이 리턴될 때까지 기다립니다.

- `await` 은 문자 그대로 promise가 해결될 때까지 자바스크립트를 기다리게 만듭니다. 그리고 결과가 나오면 계속 진행이 됩니다. 이 작업은 CPU 비용(낭비)이 들지 않습니다. 왜냐하면 엔진은 그 동안에 다른 작업을 할 수 있습니다. : 다른 스크립트나 다른 이벤트를 다룰 수 있습니다.

- 코드의 최상단에 `await`을 사용할 수 없다.

  ```js
  // syntax error in top-level code
  let response = await fetch('/article/promise-chaining/user.json');
  let user = await response.json();
  
  // 대신 비동기 함수(async)로 감싸서 사용할 수 있다.
  (async () => {
    let response = await fetch('/article/promise-chaining/user.json');
    let user = await response.json();
    ...
  })();
  ```

- `promise.then` 처럼, `await`는 then 메서드가 있는 객체를 사용할 수 있다.

- 서드파티 객체가 만약에 promise가 아니지만 promise 처럼 움직일수 있는: 만약 `.then` 을 지원하는 객체라면 충분히 `await` 을 사용할 수 있습니다.

  - 만약에 `await`이 `.then` 을 갖는 promise 객체가 아닐경우 그것은 네이티브 함수 `resolve`, `reject` 를 매개변수로 제공받을 수 있습니다. 그리고 `await`은 그중 하나가 호출 될때까지 기다립니다.

  ```js
  class Thenable {
    constructor(num) {
      this.num = num;
    }
    then(resolve, reject) {
      alert(resolve);
      // resolve with this.num*2 after 1000ms
      setTimeout(() => resolve(this.num * 2), 1000); // (*)
    }
  };
  
  async function f() {
    // waits for 1 second, then result becomes 2
    let result = await new Thenable(1);  //Thenable이 .then을 지원한다.
    alert(result);
  }
  ```



## Async Class method 비동기 클래스 메소드

- 비동기 클래스 메서드를 선언하기 위해서는 단지 `async`만 함수 앞에 붙여주면 됩니다.

```js
class Waiter {
  async wait() {
    return await Promise.resolve(1);
  }
}

new Waiter()
  .wait()
  .then(alert); // 1
```

- 반환받는 값이 promise이고 `await` 을 사용할 수 있다는 보장을 하는 것이다. 함수와 동일하다.



## async/await 과 promise

### `async/await` and `promise.then/catch`

- 우리가 `async/await`을 사용할 때, `.then`이 거의 필요가 없다, 왜냐하면 `await` 는 우리를 위해 기다려주기 때문이다. 그리고 우리는 대게 `.catch` 대신에 `try..catch`를 사용하기 때문이다. 이 방법은 항상 그렇진 않을 수 있지만 대게 편리합니다. 하지만 코드 최상위에서 `async` 함수 밖에서 사용할때 우리는 문법적으로 `await`을 사용할수가 없습니다. 그래서 우리는 최종 결과 또는 에러를 다루기 위해 `.then/catch` 문을 연습해야 한다.

  ```js
  async function f() {
    let response = await fetch('http://no-such-url');
  }
  
  // f() becomes a rejected promise
  f().catch(alert); // TypeError: failed to fetch 
  // async 밖이기 때문에 문법적으로 await이 불가해서 fetch 못함 
  ```

### `async/await` works well with `Promise.all`

- 여러 promise를 기다려야 할때, `Promise.all` 과 `await` 로 감쌀 수 있다.

```js
// wait for the array of results
let results = await Promise.all([
  fetch(url1),
  fetch(url2),
  ...
]);
    
    
// 예시 2 
async  function msg() {
	// array destructuring
	const [a, b, c] = await Promise.all([who(), what(), where()]); 
	console.log(`${ a } ${ b } ${ c }`);
}

msg(); // 🤡 lurks in the shadows <-- after 500ms
```



## Arrow function async

- 화살표 함수를 사용해서 만들 수도 있다. 

```js
// 함수표현식 async-await
const msg = async function() {
	const msg = await scaryClown();
	console.log('Message:', msg);
}

// 화살표 함수 async-await
const msg = async () => {
	const msg = await scaryClown();
	console.log('Message:', msg);
}
```







## 참고

- [캡틴판교](https://joshua1988.github.io/web-development/javascript/js-async-await/)
- [비동기를 동기식으로](https://blueshw.github.io/2018/02/27/async-await/)