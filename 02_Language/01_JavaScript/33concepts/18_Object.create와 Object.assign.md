# 18_Object.create와 Object.assign

## Object.create

- ECMAScript 5의 기능, IE8 이하 버전 사용 불가
- `프로토타입 체인`만 연결한다고 보면 될 듯

```js
// 1
const original = {
  a: 1,
  b: 2,
  c: {
    d: 3
  }
};

// 2
const copied = Object.create(original); // 복사가 아니다! 
console.log(original.isPrototypeOf(copied)); //true

// 3
original.a = 1000;
original.c.d = 3000;
console.log(copied.a);	// 1000
console.log(copied.c.d);	// 3000

// 4 
console.log(copied);	// {}

// 5
original.hasOwnProperty('a');	// true
copied.hasOwnProperty('a');	// false
```

- 작동순서

  1. 객체 리터럴 `original` 생성

  2. 프로토타입이 `original`로 설정된 완전히 새로운 객체인 copied를 생성  

     - `isPrototypeOf`를 사용해보면 true가 나오는 것을 확인할 수 있다.
     - 복사도 안될 뿐 더러,`original` 객체는 단지 `copied` 객체의 프로토타입이 될 뿐이다.

  3. `original`이 수정되면 `copied`도 함께 수정된다. 

  4. `copied` 객체를 찍어보면, 빈 객체가 출력되는것을 볼 수 있다.

     - 단, `__proto__`에는 `original`이 들어있다. 

  5. `프토토타입 체인은 확인하지않고, 해당 객체의 특정 프로퍼티 유무를 판단하는` **Object.hasOwnProperty()** 를 사용해보면, 

     - `original`은 `a`프로퍼티를 가지고 있지만, 

     - `copied`는 `a` 프로퍼티를 가지고 있지 않다.

### new 와 Object.create()의 차이 

```js
function Dog(){
    this.pupper = 'Pupper';
};

Dog.prototype.pupperino = 'Pups.';
var maddie = new Dog();
var buddy = Object.create(Dog.prototype);

//Using Object.create()
console.log(buddy.pupper); //Output is undefined
console.log(buddy.pupperino); //Output is Pups.

//Using New Keyword
console.log(maddie.pupper); //Output is Pupper      
console.log(maddie.pupperino); //Output is Pups.
```

- `new`는 생성자 코드를 실행한다.
- `Object.create()`는 프로토타입만 연결한다. (프로토타입 체인)
- `new()`가 3배 빠름! 빨갛다! 
  - 클래스 구문 사용하자!





## Object.assign (shallow copy)

- ECMAScript 5의 기능, IE8 이하 버전 사용 불가
- `Object.assign()` 메소드는 모든 열거 가능한 속성의 값을 복사하는 데 사용된다.
- 첫번째 인자로 들어오는 객체에 두번째 인자로 들어오는 객체의 프로퍼티들을 복사한다.

```js
const obj = {a: 1, b: 2};
const target = {c: 3};

const copiedObj = Object.assign(target, obj);

console.log(copiedObj);	//{c: 3, a: 1, b: 2}
```

- 복사하려는 객체의 내부에 존재하는 객체는 완전한 복사가 이루어지지 않는다. (shallow copy)

```js
const person = {
  age: 100,
  name: {
    first: 'junwoo',
    last: 'park'
  }
};

const copied = Object.assign({}, person);

person.age = 1000;
person.name.first = 'paul';
// person객체의 프로퍼티를 바꾸면, copied 객체의 프로퍼티가 바뀐다.
console.log(copied.age);	// 100
console.log(copied.name.first);	// 'paul'
```

- 복사하면서 값을 확장할 수도 있다.
- 첫 번째 인수는 Default 객체이고 다음 인수는 주가 될 객체이다. 여러 객체를 전달할 수 있으며 마지막으로 전달된 객체의 중복 속성이 다음을 따릅니다.

```js
const myObj = {
  clown: '🤡',
  police: '👮',
  santa: '🎅',
  farmer: '👩‍🌾'
}

const myObj4 = Object.assign({}, myObj, {
  santa: '🎄',
  teacher: '👩‍🏫'
});

console.log(myObj4);
// Object {
//   clown: "🤡",
//   farmer: "👩‍🌾",
//   police: "👮",
//   santa: "🎄",
//   teacher: "👩‍🏫"
// }
```

- Note: `Object.is`는 두 객체가 동일한지 확인하는 방법이다.

```js
const myObj = {
  clown: '🤡',
  police: '👮',
  santa: '🎅',
  farmer: '👩‍🌾'
}

const myObj2 = myObj;
const myObj3 = Object.assign({}, myObj);

console.log(Object.is(myObj, myObj2)); // true
console.log(Object.is(myObj, myObj3)); // false
console.log(myObj3);
// Object {
//   clown: "🤡",
//   farmer: "👩‍🌾",
//   police: "👮",
//   santa: "🎅"
// }
```

- `Object.assign()`으로 만들면 동일하지 않은 새로운 복사본을 만든다.

# JS에서 객체 복사하기

## 1. Shallow copy 얕은 복사

### 참조할당

```js
const original = {
  a: 1,
  b: 2
};

const copied = original;
original.a = 1000;

console.log(copied.a);	//1000
```

- 한 객체 값을 수정하면 다른 객체 값도 동일하게 변화한다. 
- 즉 `original`과 `copied`라는 서로 다른 변수가 같은 객체를 바라본다.

### Object.assign()

- 상술

### ES6의 전개 연산자 

```js
const original = {
  a: 1,
  b: 2,
  c: {
    d: 3
  }
};

const copied = {...original};

original.a = 1000;
original.c.d= 3000;

console.log(copied.a);	// 1
console.log(copied.c.d);	// 3000
```

- `Object.assign()`과 동일하게 작동.
- 객체의 프로퍼티로 객체를 가지고 있으면 참조를 해버리는 문제가 있다.

### for문으로 순서대로 복사하기

```js
const copyFunc = obj => {
  let copiedObj = {};
  
  for(let key in obj) {
    copiedObj[key] = obj[key];
  }
  
  return copiedObj;
}

const original = {
  a: 1,
  b: 2,
  c: {
    d: 3
  }
};

const result = copyFunc(original);

original.a = 100;
original.c.d = 3000;

console.log(result.a);
console.log(result.c.d);
```

- 반복문을 사용하여 객체를 복사하는 방법.

- 하지만 객체가 프로퍼티로 객체를 가지고 있다면, 정말 deep한 복사 대신에 오리지널 객체를 참조한다.

  오지지널 객체가 가지고 있는 객체를 수정하면 `result` 도 같이 바뀐다.

## 2. Deep clone 깊은 복사

### JSON 객체의 메소드 이용 

```js
const cloneObj = obj => JSON.parse(JSON.stringify(obj));

const original = {
  a: 1,
  b: {
    c: 2
  }
};

const copied = cloneObj(original);

original.a = 1000;
original.b.c = 2000;

console.log(copied.a);	// 1
console.log(copied.b.c);	// 2
```

- `original` 객체의 프로퍼티를 수정해도 `copied`객체는 그대로네요.

  어떻게 가능했을까요?

  `JSON.stringify` 는 자바스크립트 객체를 JSON문자열로 변환시킵니다.

  반대로 `JSON.parse`는 JSON문자열을 자바스크립트 객체로 변환시킵니다.

  JSON문자열로 변환했다가 다시 객체로 변환하기에, 객체에 대한 참조가 없어진 것입니다.

```js
const cloneObj = obj => JSON.parse(JSON.stringify(obj));

const original = {
  a: 1,
  b: {
    c: 2
  },
  d: () => { console.log('hi') }
};

const copied = cloneObj(original);

console.log(copied.d);	// undefined
```

- 2가지 문제점
  1. 다른 방법에 비해서 성능적으로 느리다
  2.  `JSON.stringify` 메소드가 function을 undefined로 처리한다다.

### Lodash의 deepclone 함수 사용하기

```js
const clonedeep = require('lodash.clonedeep');

const original = {
  a: 1,
  b: {
    c: 2
  },
  d: () => { console.log('hi') }
};

const deepCopied = clonedeep(original);

original.a = 1000;
original.b.c = 2000;

console.log(deepCopied.a);	// 1
console.log(deepCopied.b.c);	// 2
console.log(deepCopied.d());	// 'hi'
```

- Lodash는 많은 사람들이 사용해오고 안정성이 증명된 라이브러리입니다.

  Lodash는 많은 메소드들을 제공하는데요.

  그 중 하나인 deepclone메소드를 사용하면 깊은복사가 가능합니다.

### 직접 구현하기

```js
function deepClone(obj) {
  if(obj === null || typeof obj !== 'object') {
    return obj;
  }
  
  const result = Array.isArray(obj) ? [] : {};
  
  for(let key of Object.keys(obj)) {
    result[key] = deepClone(obj[key])
  }
  
  return result;
}

const original = {
  a: 1,
  b: {
  	c: 2
  },
  d: () => { console.log('hi') }
};

const copied = deepClone(original);

original.a = 1000;
original.b.c = 2000;
original.d = () => { console.log('bye') }

console.log(copied.a);	// 1
console.log(copied.b.c);	// 2
console.log(copied.d());	// 'hi'
```

- 재귀적으로 객체트리를 따라서 모두 복사를 해주는 함수를 만들어서 사용하는 방법도 있습니다.

## 참고

- https://junwoo45.github.io/2019-09-23-deep_clone/