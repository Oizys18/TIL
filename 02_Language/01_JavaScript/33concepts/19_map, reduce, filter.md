# 19_map, reduce, filter

- 코드 간결성
- 함수형 프로그래밍! 
- `for`, `forEach` 루프 관리 안해도 된다!
- `Array.prototype`에 정의되어 있으므로 어떤 배열에서도 사용할 수 있다!!

## [map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?source=post_page---------------------------)

- `map()` 메소드는 배열의 모든 요소에 제공된 함수를 적용하여, 결과로 새 배열을 생성한다.

- `map`에 전달한 콜백은 명시적으로`return` 문을 가져야한다. 그렇지 않으면`map`은`undefined`로 가득 찬 배열을 출력합니다.

- 콜백 인자 

  - | param   | meaning                                     |
    | ------- | ------------------------------------------- |
    | elem    | 요소 값                                     |
    | index   | 각 순회의 인덱스는 왼쪽에서 오른쪽으로 이동 |
    | array   | 메소드를 호출 한 원래의 배열                |
    | thisArg | (선택 사항) 콜백에서 this로 참조 될 객체    |

```js
array.map(function(elem, index, array) {
      ...
}, thisArg);

// 예시
const numbers = [2, 4, 8, 10];  
const halves = numbers.map(x => x / 2);// halves is [1, 2, 4, 5]
```

## [filter()](https://developer.mozilla.org/pt-PT/docs/Web/JavaScript/Reference/Global_Objects/Array/filter?source=post_page---------------------------)

- `filter()` 메소드는 배열의 모든 요소에 제공된 함수의 조건을 만족하는지 판단하여, 결과로 새 배열을 생성한다.

- **콜백이 무조건 `true`혹은 `false`를 `return`해야 한다.** 만약 return 문을 안 쓰면 콜백은 undefined를 반환하고, filter는 오류를 뱉는 대신 `false`값만 나올 것이다.  

- 콜백 인자 

  - | param   | meaning                                     |
    | ------- | ------------------------------------------- |
    | elem    | 요소 값                                     |
    | index   | 각 순회의 인덱스는 왼쪽에서 오른쪽으로 이동 |
    | array   | 메소드를 호출 한 원래의 배열                |
    | thisArg | (선택 사항) 콜백에서 this로 참조 될 객체    |

```js
array.filter(function(elem, index, array) {
      ...
}, thisArg);

// 예시
const words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];  
const longWords = words.filter(word => word.length > 6);
// longWords is ["exuberant", "destruction", "present"]
```

## [reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce?source=post_page---------------------------)

- `reduce()` 메소드는 배열의 각 요소(좌 -> 우)에 대해 누적값(accumulator)과 함께 함수를 적용하여 단일 값으로 감소시킨다.

  - 이 때 단일 `value`는 `숫자`가 아니다. 즉, 단일 배열을 반환할 수도 있다! 

- `map()`,`filter()`와 유사하지만 콜백 인수가 다르다.

- 콜백 인자 

  - | param        | meaning                                                      |
    | ------------ | ------------------------------------------------------------ |
    | prevValue    | 각 콜백을 통해 반환 된 누적 값 (accumulator)                 |
    | elem         | 요소 값                                                      |
    | index        | 각 순회의 인덱스는 왼쪽에서 오른쪽으로 이동                  |
    | array        | 메소드를 호출 한 원래의 배열                                 |
    | initialValue | (선택 사항) 첫 번째 (가장 왼쪽) 콜백에서 첫 번째 인수로 사용되는 객체입니다. |

```js
array.reduce(function(prevVal, elem, index, array) {
      ...
}, initialValue); // initialValue 입력안하면 배열의 0번 인덱스를 사용한다.
    
// 예시
const total = [0, 1, 2, 3].reduce((acc, value) => acc + value, 1);// total is 7
```

- 콜백 함수의 호출의 결과를 다음 콜백 함수의 호출로 전달하여 **속임수** 같이 동작할 수 있게 한다.

### Compose Functions (함수의 합성)

- [reduce 함수합성 예시](https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d)

```js
const compose = (...fns) => x => fns.reduceRight((v, f) => f(v), x);
/*  
const compose = (...fns) => {
	return (x) => {
		return fns.reduceRight((v, f) => f(v), x)
	}
};
*/
```

- *compose*는 [커링 패턴 형태](https://www.facebook.com/notes/kevin-lee/currying-어따-써먹냐구요/214522735556858/)로써 부분적으로 적용되며, 그 결과를 다음 함수로 전달한다. [**rest parameters**](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters) 가 사용된 것을 주목하라. 때문에 원하는 만큼의 함수를 전달 하여 *fns* 배열에 넣을 수 있는 것이다.

  그런 compose에 함수들을 전달한 다음 초기 값 (*x*)를 입력하면 된다.

  수집된 함수의 배열(*fns*)에 *x*를 초기값으로 전달하여 [reduceRight](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/ReduceRight)를 호출하여 반환한다.

  **reduceRight**는 reduce와 기능은 같지만 배열의 끝에서 시작하여 시작점으로 이동한다.

- 사용 예시

```js
const add1 = n => n + 1;  
const double = n => n * 2;const add1ThenDouble = compose(  
  double,  
  add1  
);add1ThenDouble(2); // 6  
// ((2 + 1 = 3) * 2 = 6)
```

### 프로미스 체이닝

```js
let itemIDs = [1, 2, 3, 4, 5];
itemIDs.reduce((promise, itemID) => {  
  return promise.then(_ => api.deleteItem(itemID));  
}, Promise.resolve());

// 위와 동일
Promise.resolve()  
.then(_ => api.deleteItem(1))  
.then(_ => api.deleteItem(2))  
.then(_ => api.deleteItem(3))  
.then(_ => api.deleteItem(4))  
.then(_ => api.deleteItem(5));
```

## Find

```js
// definition 
collection.find((item) => {
    // return first element that satisfy the condition
});
// example
const arr = [1,2,8,4,5];
const value = arr.find(i => i%4 == 0);
// return the first value i.e 8 
```

- **Find는 배열에서 작동하고 함수에서 조건을 만족하는 첫 번째 요소를 반환합니다.**

  Note: 쉽고 단순하지만 대용량 data set에서는 효율적이지 않은 이유는 무엇입니까? [여길](https://github.com/dg92/Performance-Analysis-JS?source=post_page---------------------------) 보세요

  #### 일부 실제 시나리오 + 일부 ES6에서 사용할 수 있습니다. 