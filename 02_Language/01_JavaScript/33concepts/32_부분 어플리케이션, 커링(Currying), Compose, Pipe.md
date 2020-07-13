# 32_부분 어플리케이션, 커링(Currying), Compose, Pipe

- 코드에 전혀 문제가 없는 경우에도 이를 수행하면 상용구 코드의 많은 부분과 불필요한 변수를 대부분 제거하여 더 작고 간결한 코드를 생성할 수 있으며 결함이 있을 때 버그와 버그를 쉽게 식별할 수 있습니다.

## 함수의 합성(function composition)

- **한 가지 기능을 수행하는 작은 함수들을** 조립하여 하여 **복잡한 기능** 을 생성
- 데이터 작업 방식에 있어 더 많은 유연성, 예측 가능성, 가독성, 테스트 가능성 제공
- 한 함수의 **출력**을 다른 함수의 **입력** 으로 전달
- 여러 간단한 함수를 결합하여 더 복잡한 함수를 만드는 메커니즘
- JS의 함수는 **일급시민**이기 때문에 boolean 조건을 기반으로 하여 완전히 새로운 기능을 구성할수 있다. 

```js
// 기본적인 함수 합성
const users = [
  { name: "Jeff", age: 14 },
  { name: "Jack", age: 18 }, 
  { name: "Milady", age: 22 },
]
const filter = (cb, arr) => arr.filter(cb);
const map = (cb, arr) => arr.map(cb);

map(u => u.name, filter(u => u.age >= 18, users)); //["Jack", "Milady"]

// 자동화 버전
const compose = (...functions) => args => functions.reduceRight((arg, fn) => fn(arg), args);
const filter = cb => arr => arr.filter(cb);
const map = cb => arr => arr.map(cb);

compose(
  map(u => u.name),
  filter(u => u.age >= 18)
)(users) //["Jack", "Milady"]




// JS 함수의 일급시민 특성을 이용한 boolean 조건 기반 구성 용례
func1 = (condition < 50)? minus10: add10
func2 = (age < 20)? add100: minus100
priceAdjuster = compose(func1, func2)
```

- `compose`는 고차 함수입니다. 다른 함수를 반환하는 함수입니다.
- `compose`는 여러 함수를 인수로 취해서 spread opeartor:`...`를 사용하여 함수의 배열로 변환합니다.
- 그런 다음 해당 함수에 간단히 `reduceRight`를 적용합니다. 콜백의 첫 번째 매개 변수는 현재 인수입니다. 두 번째 인수는 현재 함수입니다. 그런 다음 현재 인수로 각 함수를 호출하고 결과는 다음 호출에 사용됩니다.



## Compose()

![img](https://github.com/Lee-hyuna/33-js-concepts-kr/wiki/resource/yongkwan/33/02.png)

- `compose()`는 **인자를 함수로 받는데 **, **데이터 플로우는 오른쪽에서 왼쪽으로**이어지며 인자들을 결합한다. 그 다음 결합 된 함수를 반환한다.

```js
const compose = (...fns) => {
	 return x => {
		return fns.reduceRight((y, f) => f(y), x)
	 }
 }

const addTwo = x => x + 2;
const multiplyByFour = x => 4 * x;
const composeFunc = compose(multiplyByFour, addTwo)
const result = composeFunc(3)
```

## Pipe()

![img](https://github.com/Lee-hyuna/33-js-concepts-kr/wiki/resource/yongkwan/33/03.png)

- `pipe()`는 `compose()`와 거의 동일하다. 차이점은 pipe()`는 데이터 이동이 `왼쪽 --> 오른쪽`으로 **반대 방향**이다.
- Compose와는 달리 `Array.prototype.reduceRight`대신 `Array.prototype.reduce`이 사용 된다.

```js
const pipe = (...fns) => {
	 return x => {
		return fns.reduce((y, f) => f(y), x)
	 }
 }

// addTwo와 multiplyByFour의 위치가 바뀜! 
const addTwo = x => x + 2;
const multiplyByFour = x => 4 * x;
const pipeFunc = pipe(addTwo, multiplyByFour)
const result = pipeFunc(3)
```



## 커링 Currying

- 여러 개의 매개 변수를 필요로 하는 함수를 적은 수의 매개 변수가 제공 되었을 때 나머지 매개 변수를 기다리는 새로운 함수를 리턴하는 함수로 변환하는 프로세스
- Currying은 모든 인수가 적용될 때까지 항상 하나의 인수로 다른 함수를 반환한다. 따라서 모든 인수를 다 사용하고 최종 값이 반환 될 때까지 반환 된 함수를 계속 호출한다.
- 오른쪽 -> 왼쪽으로 진행된다. 
  - 배열과 함수를 취하는 Ramda함수는 일반적으로 함수를 첫 번째 인수로, 배열을 두 번째 인수로 예상합니다.

```js
// Normal function  
function addition(x, y) {  
   return x + y;  
}

// Curried function  
function addition(x) {  
   return function(y) {  
     return x + y;  
   }  
}
```

- Curry는 이진 함수를 사용하여 단항 함수를 반환하는 단항 함수를 반환
- 커링이된 함수에는 반복자 동작이 내장되어 있다. 
- 한 번에 하나의 인수가 적용되고 다음 단계에서 사용할 호출 함수로 리턴된다. 

### 용례

1. 커리 함수의 일반적인 사용 사례는 **함수 합성**입니다 (예 :`p (x) = q (r (x))`). 즉, 인수를 전달하여 이전 함수에서 새 함수를 작성합니다. 함수 `q` 는 함수 `r` 의 인수로 반환 값을 받습니다. 함수는 하나의 값만 반환 할 수 있으므로 반환 값에 적용되는 함수는 단항이어야 합니다.
2. 커링된 함수는 일반 기능을 생성 할 수있는 많은 가능성이있는 프로젝트의 ** 인프라구조 설정 ** 동안에도 사용될 수 있으므로 작은 조각을 쉽게 구성하고 재사용 할 수 있습니다.
3. [**Ramda.js**](https://ramdajs.com/0.16/index.html) 라이브러리. 함수는 자동으로 커링되며 lodash에는 [curry](https://lodash.com/docs/4.17.10#curry)라는 함수가 있으며이 함수는 커링 기능을 만드는 데 사용할 수 있습니다.
4. [**Memoization**](https://taylodl.wordpress.com/2012/06/13/functional-javascript-memoization-part-i/) 커링 함수를 위한 다른 좋은 케이스 입니다.
5. **Handling error** 에러를 발생시키는 함수의 핸들링과 에러 직후 즉시 종료 처리.
6. API에서의 **Catching multiple error and use it as a validator** 처리와 클라이언트 사이드 코드.
7. 함수를 인자로 받아서 그 값을 리턴할 수 있는 **First class functions** 를 생성할 수 있다.

### ES6 Curry Factory Method

```js
// 띠용한 코드!
const compose = (…fns) =>
  // g()에서 처리한 것을 f()가 처리한다 
  fns.reduce((f, g) => (…args) => f(g(…args)));
```

### Partial Application

- 함수에 여러 인수를 고정하여 더 작은 인수의 다른 함수, 즉 함수 체인이 진행됨에 따라 하나 이상의 인수에 값을 바인딩하는 다른 함수를 생성하는 기술

```js
function add1(x) {  
  return 1 + x;  
}

// 내장 메소드 .bind 사용
function.bind(_thisValue_, [_arg1_], [_arg2_], ...)

// 암시적인 이 매개 변수가 초기 인수로 항상 지정된 새 함수로 바뀜
function addition(x, y) {  
   return x + y;  
}

// this 값은 (메소드가 아닌) 함수 추가에 중요하지 않으므로이 값이 null입니다.
const plus5 = addition.bind(null, 5)  
plus5(10) // output -> 15
```

- [Underscore](https://harrythegreat.tistory.com/entry/%EC%96%B8%EB%8D%94%EC%8A%A4%EC%BD%94%EC%96%B4-%EC%A0%95%EB%A6%AC) 나 lodash를 사용할 때 이 bind 메소드보다 훨씬 좋은 *partial* 함수를 사용할 수 있습니다.

- 차이점
  - 커링은 항상 중첩 된 단항 (1 차) 기능을 생성합니다. 변환 된 함수는 여전히 원본과 동일합니다. (원본 함수는 여전히 해당 인자들의 갯수를 원합니다. )
  - partial 어플리케이션은 임의의 수의 인수 함수를 생성합니다. 변환 된 함수는 원래 함수와 다릅니다. 인수가 더 적습니다.
  - 커링은 partial 어플리케이션이 아닙니다. partial 어플리케이션 프로그램을 사용하여 구현할 수 있습니다. 많은 수의 인수를 취하는 함수를 커링 할 수 없습니다. (인수의 수를 수정하지 않는 한).





### MapReduce 

-  데이터 셋에 맵을 적용하고 결과를 줄여 단일 결과를 생성합니다.(일반적인 함수합성의 원리)

```js
// 단어 카운터 MapReduce
const reduce = cb => arr => arr.reduce(cb); //Just currify the reduce function

const mapWords = map(() => 1);
const reduceWords = reduce((acc, curr) => acc += curr)(0)

compose(reduceWords, mapWords)(['foo', 'bar', 'baz']); //3
```

### Pipe와 Composition 

- 차이: 컴포지션 순서 
  - Pipe는 왼쪽 -> 오른쪽
  - Compose는 오른쪽 -> 왼쪽 

```js
// pipe 예시
const pipe = (...functions) => args => functions.reduce((arg, fn) => fn(arg), args);

pipe(
  filter(u => u.age >= 18),
  map(u => u.name),
)(users) //["Jack", "Milady"]

pipe(mapWords, reduceWords)(['foo', 'bar', 'baz']);
```

## 참고

- [JS Underscore](https://harrythegreat.tistory.com/entry/%EC%96%B8%EB%8D%94%EC%8A%A4%EC%BD%94%EC%96%B4-%EC%A0%95%EB%A6%AC)