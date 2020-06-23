# 16_new, 생성자, instanceof, 인스턴스

## new

- 생성자 함수 (Constructor function)을 호출하는 방법이다. 
- 이름은 대문자로 시작한다.
- `new` 신규작성 시, 
  - 새로운 빈 오브젝트를 생성한다.
  - 새로 생성된 오브젝트에 `this`를 바인딩한다.
  - 새로 생성된 오브젝트에 생성자 함수의 `prototype object`를 가리키는 `proto`라는 속성을 추가한다. 
  - 생성된 오브젝트가 함수로부터 반환될 수 있도록 함수의 마지막에 `return this`를 추가한다. (function에서 object를 반환)

```js
function Student(name, age) {
  this.name = name;
  this.age = age;
}

var second = new Student('Jeff', 50);

second.__proto__ === Student.prototype;
// true
```

![img](https://miro.medium.com/max/594/1*RIY6LBqQAbXPzMXMwH5d-Q.png)

- `Student` constructor 함수는 `.prototype` 속성을 갖고있다. 이 `prototype`은 다시 constructor를 가리키는 `.constructor`라는 오브젝트를 지니고 있다. (`loop`다!)

- 이러한 속성과 오브젝트의 loop는 **상속**의 개념을 갖고 있기 때문에 중요하다. `prototype` 오브젝트는 `constructor`함수를 통해 해당 함수로 생성된 모든 오브젝트 간 공유된다. **즉, 모든 오브젝트가 사용해야할(필요한) 함수와 속성을 `prototype`에 추가할 수 있다는 뜻이다.**
  - `toString()`같은 메소드를 직접 추가하지 않아도 사용할 수 있는 이유! (`Object prototype`에 자동생성)

### 생성자의 return

- 일반적으로 생성자에는 return 문이 없습니다. 생성자의 목적은 `this`에 필요한 내용을 모두 적는 것이고, 그 자체로 목적입니다. 
- 하지만 `return`문이 있으면 아래와 같이 작동합니다. 
  - object와 함께 return이 호출되면, `object`가 `this`대신 반환됩니다.
  - primitive와 함께 `return`이 호출되면 무시됩니다.
- `return` + `object` -> `object`반환 
- 다른 경우 모두 `this`반환 

```js
// 1
function BigUser() {
  this.name = "John";
  return { name: "Godzilla" };  // <-- returns an object
}
alert( new BigUser().name );  // Godzilla, got that object ^^'

// 2
function SmallUser() {
  this.name = "John";
  return; // finishes the execution, returns this
  // ...
}
alert( new SmallUser().name );  // John
```

### 생성자의 메소드

- 오브젝트를 생성하기 위해 생성자를 사용하면 매우 큰 유연성이 보장된다. 생성자 함수는 오브젝트를 정의하는 인자를 가질 수 있으며, 인자에 무엇이 들어갈 지도 정할 수 있다.
- 물론 `this`에 속성뿐만 아니라 메소드도 넣을 수 있다. 
- 아래 예시에서 `new User(name)`은 주어진 `name`과 `sayHi` 함수를 지닌 채 생성된다.

```js
function User(name) {
  this.name = name;

  this.sayHi = function() {
    alert( "My name is: " + this.name );
  };
}

let john = new User("John");

john.sayHi(); // My name is: John

/*
john = {
   name: "John",
   sayHi: function() { ... }
}
*/
```

### 요약

- 생성자 함수의 첫 문자는 대문자로 생성한다. 
- 생성자 함수는 오직 `new`로만 호출한다. 이 호출은 비어있는 `this`를 생성하며 마지막에 생성된 오브젝트를 반환한다.
- JS는 built-in 오브젝트에 생성자 함수를 제공한다. ex) `Date`, `Set`



## DRY한 JS 객체 작성 방법

```js
// 기존 방법

// 1. 개체문자표기법
let user1 = {
  name: "Taylor",
  points: 5,
  increment: function() {
    user1.points++;
  }
};

// 2. Object.create()
let user2 = Object.create(null);

user2.name = "Cam";
user2.points = 8;
user2.increment = function() {
  user2.points++;
}
```

- 기존의 두 가지 방법은 반복적이며 항목을 수동으로 생성해야한다. 대안으로 아래와 같은 방법들이 있다.

### 1. function으로 오브젝트 생성

```js
function createUser(name, points) {
  let newUser = {};
  newUser.name = name;
  newUser.points = points;
    // function으로 생성
  newUser.increment = function() { 
    newUser.points++;
  };
  return newUser;
}

let user1 = createUser("Bob", 5);
user1.increment(); 
// 단, 이 increment는 복사본일 뿐이다. 
// 각 개체에 대해 기능의 변경 가능성을 수동으로 수행해야 하므로 이 방법은 코드를 쓰는 데 적합하지 않다.
```

### 2. JS의 prototypal nature를 활용

```js
function createUser(name, points) {
  let newUser = Object.create(userFunction);
  newUser.name = name;
  newUser.points = points;
  return newUser;
}

let userFunction = {
  increment: function() {this.points++};
  login: function() {console.log("Please login.")};
}

let user1 = createUser("Bob", 5);
user1.increment();
```

- 모든 JavaScript 기능에는 기본적으로 비어 있는 프로토타입 속성이 있습니다. 이 프로토타입 속성에 기능을 추가할 수 있으며, 이 양식에서는 이를 메소드라고 합니다. 상속된 기능이 실행되면 이 값이 상속되는 개체를 가리킵니다.
- `user1` 객체가 생성되었을 때 `userFunction`과의 프로토타입 체인 결합이 형성되었습니다.
- `user1.increment()`가 call stack에 있는 경우, 글로벌 메모리에서 `user1`을 찾습니다. 다음으로, `increment`function을 찾지만 찾지 못합니다. prototype chain의 다음 object를 보고 거기서 increment function을 찾을 것입니다.

### 3. new와 this 활용

```js
function User(name, points) {
 this.name = name; 
 this.points = points;
}
User.prototype.increment = function(){
 this.points++;
}
User.prototype.login = function() {
 console.log(“Please login.”)
}

let user1 = new User(“Dylan”, 6);
user1.increment();
```

#### prototype과 proto의 차이

- 프로토타입(Prototype)은 생성된 개체에서 **proto** 속성이 되는 것을 결정하는 생성자 기능의 속성입니다. 
- `__proto__`는 생성된 참조이며, 이 참조는 프로토타입 체인 결합이라고 알려져 있습니다.

### 4. ES6의 syntactic sugar

```js
class User {
  constructor(name, points) {
    this.name = name;
    this.points = points;
  }
  increment () {
    this.points++;
  }
  login () {
    console.log("Please login.")
  }
}

let user1 = new User("John", 12);
user1.increment();
```

- 3번과 동일하지만, ES6에서 도입된 `class`구문을 사용하면 더 깔끔하게 작성할 수 있다.



## typeof  vs  instanceof

- `typeof`는 값이 원시 타입의 요소인지 확인한다.

  ```js
   if (typeof value === 'string')
  ```

- `instanceof`는 값이 클래스 또는 생성자 함수의 인스턴스인지 확인한다.

  ```js
  if (value instanceof Map)
  ```

- 하지만 이것은 이상적이지 못하다. 왜냐하면 원시 값과 객체의 차이점이 종종 모호해지기 때문이다. 추가로 몇가지 이상한 점이 상황을 더욱 복잡하게 만든다.

  - `typeof null`은 `'object'`이다. `'null'`이 아니다. 이것은 버그로 간주된다. (하지만 코드일관성을 위해 안 고침)

  - `typoeof`는 객체와 함수를 구분할 수 있다.

    ```js
    > typeof {}
    'object'
    > typeof function () {}
    'function'
    ```

- `typeof`를 통해 개체성을 확인할 수 있는 간단한 방법이 없다는 것을 의미한다.

### 원시타입에 instanceof 적용

PrimitiveNumber 클래스가 주어지면, 아래의 코드는 `x instanceof PrimitiveNumber` 표현식이 true를 반환하는 값 x를 구성한다. PrimitiveNumber에 대한 정적 메서드를 구현하면 키가 공용 심볼 인 [Symbol.hasInstance](https://exploringjs.com/es6/ch_oop-besides-classes.html#_property-key-symbolhasinstance-method)가 된다.

```js
class PrimitiveNumber {
    static [Symbol.hasInstance](x) {
        return typeof x === 'number';
    }
}
console.log(123 instanceof PrimitiveNumber); // true
```

##  instance 타입 지정

- 특정 오브젝트가 다른 무언가의 instance 임을 확인하려면 `instanceof`를 사용하면 된다.

```js
myBook instanceof Book    // true
myBook instanceof String  // false 
```

- `instanceof`의 우측이 함수가 아니면 에러가 발생한다.

```js
myBook instanceof {};
// TypeError: invalid 'instanceof' operand ({})
```

- instance 의 타입을 확인하는 다른 방법은 `constructor` 속성을 사용하는 것이다. 

```js
myBook.constructor === Book;   // true
```

- `myBook`의 생성자 속성은 `Book`을 가리키고 있기 때문에 `===` 연산이 `true`다. JS의 모든 오브젝트는 각자의 prototype에게서 `constructor` 속성을 상속받는다. 
- 단, constructor 속성을 통해 `instance`확인하는 것은 불필요하게 코드가 길어지기 때문에 안 좋은 방법이다. 

## Object.defineProperty() 메소드

- 생성자 내부에서  `Object.defineProperty()` 를 사용하여 필요한 모든 속성을 설정할 수 있다.

```js
function Book(name) { 
  Object.defineProperty(this, "name", { 
      get: function() { 
        return "Book: " + name;       
      },        
      set: function(newName) {            
        name = newName;        
      },               
      configurable: false     
   }); 
}

var myBook = new Book("Single Page Web Applications");
console.log(myBook.name);    // Book: Single Page Web Applications

// we cannot delete the name property because "configurable" is set to false
delete myBook.name;    
console.log(myBook.name);    // Book: Single Page Web Applications

// but we can change the value of the name property
myBook.name = "Testable JavaScript";
console.log(myBook.name);    // Book: Testable JavaScript
```

- 이 코드는 속성 접근자를 정의하기 위해 `Object.defineProperty()`를 사용했습니다. 속성접근자는 다른 어떠한 속성이나 메서드를 포함하지 않지만, 속성을 읽을때 호출되는 getter와 프로퍼티가 작성될 때 호출되는 setter를 정의합니다.
- getter는 값을 리턴해야하며, setter는 속성에 할당된 값을 인자로 받는다. 위의 생성자는 `name` 속성이 변경/저장될 수 있는 `instance`를 반환하지만, 삭제는 할 수 없다. 그리고 우리가 이름의값을 얻으려할때 getter는 'Book: '이라는 문자열을 앞에 붙이고 리턴을한다.

## 객체리터럴 표기법은 생성자를 선호한다.

- JS는 아홉 개의 만들어진 생성자가 있습니다: `Object()`, `Array()`, `String()`, `Number()`, `Boolean()`, `Date()`, `Function()`, `Error()`, `RegExp()` 
- 값을 만들 때, 객체리터럴이든 생성자든 아무거나 사용해도 된다.
- 단, 객체리터럴이 더 읽기 쉽고 작동도 빠를 뿐만 아니라 파싱할 때 최적화가 가능하기 때문에 간단한 오브젝트는 그냥 객체 리터럴을 사용하자.
- 리터럴에서도 메소드를 호출할 수 있다. 
  - 메소드가 오브젝트에서 호출될 때, JS는 리터럴을 임시 오브젝트로 변환하고 작동가능하도록 만든다. 임시 오브젝트가 불필요해지면 그 때 삭제된다.

## new 키워드 꼭 쓰자

- 모든 생성자 만들 때 `new` 꼭 쓰자.
- 실수로 `new`안 쓰면 새롭게 생성하려고 했던 오브젝트 대신 global object를 (ex window) 수정하게 된다.

```js
function Book(name, year) {
  console.log(this);
  this.name = name;
  this.year = year;
}

// new 안쓰면 window가 수정된다...!
var myBook = Book("js book", 2014);  
console.log(myBook instanceof Book);  //false
console.log(window.name, window.year); // js book 2014

var myBook = new Book("js book", 2014);  
console.log(myBook instanceof Book); // true
console.log(myBook.name, myBook.year); // js book 2014
```

## Scope-safe 생성자

- 생성자는 단순히 함수다. 즉 `new`없이 호출 가능하다.
- 단, 제대로 사용하지 않으면 (바로 위 단락처럼) 의도치 않은 오류가 발생한다. 
- scope-safe 생성자를 사용하면 `new`가 있든 없든 같은 결과를 내도록 도와준다.
- `Object`,`Regex`, `Array`같은 내장함수는 모두 scope-safe다.
  - `new`사용 안하면 해당 생성자를 다시 `new`로 호출해서 올바른 인스턴스를 반환한다.

```js
function Fn(argument) { 

  // if "this" is not an instance of the constructor
  // it means it was called without new  
  if (!(this instanceof Fn)) { 
    // call the constructor again with new
    return new Fn(argument);
  } 
}
```

```js
// scope-safe 버전
function Book(name, year) { 
  if (!(this instanceof Book)) { 
    return new Book(name, year);
  }
  this.name = name;
  this.year = year;
}

var person1 = new Book("js book", 2014);
var person2 = Book("js book", 2014);

console.log(person1 instanceof Book);    // true
console.log(person2 instanceof Book);    // true
```

