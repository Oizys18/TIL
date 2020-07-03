# 25_[Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)

```js
var promise = new Promise(function(resolve, reject) {  
// do a thing, possibly async, then…  
  
if (/* everything turned out fine */) {  
resolve("Stuff worked!");  
}  
else {  
reject(Error("It broke"));  
}  
});
```

- `Promise` 는 자바스크립트 비동기 처리에 사용되는 객체
- 콜백을 함수에 전달하는 대신 콜백을 첨부하는 객체가 리턴되는 것이다.
-  보다 동기적인 방식으로 비동기 코드를 작성할 수 있다. (`promise`는 비동기다!)
- `.then`을 통해 여러 `promise`를 체이닝할 수 있다.
  - Promise는 이전 Promise이 해결되거나 완료된 후에 어떤 일이 일어나야 하는지를 보여주기 위해 `.then` 구문을 사용한다. 

### 속성

- `Promise.length`
  - 값이 언제나 1인 길이 속성입니다. (생성자 인수의 수)

- [`Promise.prototype`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/prototype)
  - `Promise` 생성자의 프로토타입을 나타냅니다.

### 메소드

- [`Promise.all(iterable)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

  `iterable` 내의 모든 프로미스가 이행한 뒤 이행하고, 어떤 프로미스가 거부하면 즉시 거부하는 프로미스를 반환합니다. 반환된 프로미스가 이행하는 경우 `iterable` 내의 프로미스가 결정한 값을 모은 배열이 이행 값입니다. 반환된 프로미스가 거부하는 경우 `iterable` 내의 거부한 프로미스의 이유를 그대로 사용합니다. 이 메서드는 여러 프로미스의 결과를 모을 때 유용합니다.

- [`Promise.race(iterable)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

  `iterable` 내의 어떤 프로미스가 이행하거나 거부하는 즉시 스스로 이행하거나 거부하는 프로미스를 반환합니다. 이행 값이나 거부 이유는 원 프로미스의 값이나 이유를 그대로 사용합니다.

- [`Promise.reject()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)

  주어진 이유로 거부하는 `Promise` 객체를 반환합니다.

- [`Promise.resolve()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

  주어진 값으로 이행하는 `Promise` 객체를 반환합니다. 값이 `then` 가능한 (즉, `then` 메서드가 있는) 경우, 반환된 프로미스는 `then` 메서드를 따라가고 마지막 상태를 취합니다. 그렇지 않은 경우 반환된 프로미스는 주어진 값으로 이행합니다. 어떤 값이 프로미스인지 아닌지 알 수 없는 경우, [`Promise.resolve(value)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve) 후 반환값을 프로미스로 처리할 수 있습니다.

### promise 프로토타입

- 속성

  - `Promise.prototype.constructor`

    인스턴스의 프로토타입을 만드는 함수를 반환합니다. 기본값은 [`Promise`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise) 함수입니다.

- 메소드

  - [`Promise.prototype.catch()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

    프로미스(promise)에 거부 처리기 콜백을 추가하고 호출된 경우 콜백의 반환값 또는 프로미스가 대신 이행된 경우 그 원래 이행(fulfillment)값으로 결정하는(resolving) 새 프로미스를 반환합니다.

  - [`Promise.prototype.then()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

    프로미스에 이행 또는 거부 처리기를 추가하고 호출된 처리기의 반환값 또는 프로미스가 처리되지 않은 경우 그 원래 처리된(settled) 값으로 결정하는 새 프로미스를 반환합니다 (즉 관련 처리기 `onFulfilled` 또는 `onRejected`가 `undefined`인 경우).

  - [`Promise.prototype.finally()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)

    Appends a handler to the promise, and returns a new promise which is resolved when the original promise is resolved. The handler is called when the promise is settled, whether fulfilled or rejected.

### state

- `Promise`의 3가지 상태값
  1. 대기 `pending`: 보류중 / 응답을 기다리는 중 (실행도 거부도 완료도 아님. 그냥 기다리는 중)
  2. 이행 `resolved/fulfilled` : 응답 성공 / Promise 완료 
  3. 거부`rejected`: 응답 실패 (오류)

### value

- `resolved` 혹은 `rejected` 값
- 값이 설정되면 변경할 수 없다. 

![img](https://joshua1988.github.io/images/posts/web/javascript/promise.svg)

- 프로미스 처리 흐름

###  promise chaining

```js
function getPromise(url) {
  // return a Promise here
  // send an async request to the url as a part of promise
  // after getting the result, resolve the promise with it
}

const promise = getPromise('some url here');

promise.then((result) => {
  //we have our result here
  return getPromise(result); //return a promise here again
}).then((result) => {
  //handle the final result
});
```

```js
promise.then((result) => {
  console.log('Got data!', result);
}).catch((error) => {
  console.log('Error occurred!', error);
});

promise.then((result) => {
  console.log('Got data!', result);
}).then(undefined, (error) => {A
  console.log('Error occurred!', erroAr);
});

// 두 코드는 동일하다.
```

- then()은두개의 콜백을 인자로 받는다. promise가 거부되면 두번째 promise가 호출된다. 혹은 catch()함수를 사용할 수도 있다.
- then()을 호출 할 때마다 Promise 체인에 다른 단계가 생성되고 체인의 어느 지점에서든 오류가 발생하면 다음 catch() 블록이 트리거됩니다. 
- then() 및 catch()는 모두 원시 값 또는 새로운 약속을 반환 할 수 있으며 결과는 체인의 다음 then()으로 전달됩니다.



### 안티패턴! 지양하기

- 콜백이랑 프로미스 섞어쓰기
- 에러핸들링을 `.catch()`가 아니라 `.then()` 으로 하기
- 콜백지옥 금지
- `return`꼭 하기



## 참고

- [캡틴판교 JS프로미스](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)
- [MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript 비동기 처리를 위한 promise 이해하기](https://velog.io/@cyranocoding/2019-08-02-1808-%EC%9E%91%EC%84%B1%EB%90%A8-5hjytwqpqj)
- [ES6 프로미스(Promise), 진짜 쉽게 이해하기 (Promise의 목적만 생각한다.)](https://jeong-pro.tistory.com/128)
- [감성프로그래밍](https://programmingsummaries.tistory.com/325)