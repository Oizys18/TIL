# 15_this, call, apply, bind

- `call`,`apply`,`bind`: 함수 호출을 제어하는데 사용된다.
- `call()`/`apply()`를 사용하여 함수를 즉시 호출할 수 있다. `bind()`는 나중에 실행될 때 원래의 함수를 호출하는 올바른 컨텍스트("**this**")를 갖는 바인딩 함수를 반환한다. 그래서 `bind()`는 함수가 특정 이벤트에서 나중에 호출되어야 할 경우에 유용하게 사용할 수 있다.

![https://miro.medium.com/max/700/1*TkzF3ckhM9Xf_U9XFaCyhA.png](https://camo.githubusercontent.com/d8b9e1e44fcd93975319a70666cff4b1eb821d3f/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3730302f312a546b7a4633636b684d3958665f5539584661437968412e706e67)

## 0. this 

- 함수가 생성될 때 `this` 키워드가 함께 생성되고, 함수가 작동하는 object와 연결된다.
- `this` 키워드의 값은 함수 그 자체와는 아무 관련이 없다. 함수가 호출되는 방식이 `this`값을 결정한다.

```js
// define a function
var myFunction = function () {
  console.log(this);
};

// call it
myFunction();

// 디폴트로 this는 window Object다. 
```

- 디폴트로 `this`는 언제나 window Object, 즉 root(Global scope)를 가리킨다. 
  - 단, strict mode에서 작동될 때 `this`는 `undefined`다.

### Object literal 객체 리터럴

```js
var myObject = {
  myMethod: function () {
    console.log(this);
  }
};
```

- 이 때 `this`는 뭐가 될지 모른다..!
- `this`값은 함수 그 자체와 아무 상관이 없다는 것을 잊지 말자.. 함수가 호출되는 방식이 `this`값을 결정한다..!

### implicit binding

```js
//implicit binding
var myMethod = function () {
  console.log(this);
};

var myObject = {
  myMethod: myMethod
};

myObject.myMethod() // this === myObject
myMethod() // this === window
```

- `myObject`는 `myMethod` 함수를 가리키는 `myMethod` 속성을 가지고 있다. `myMethod` 함수가 글로벌 스코프에서 호출될 때, `this`는 window Object를 가리킨다. `myObject`의 메소드로 호출될 때, `this`는 `myObject`를 가리킨다. 

### explicit binding

- 명시적으로  `call()` 혹은 `apply()`를 사용하여 `context`를 함수에 바인딩하는 것을 말한다.

```js
var myMethod = function () {
  console.log(this);
};

var myObject = {
  myMethod: myMethod
};

myMethod() // this === window
myMethod.call(myObject, args1, args2, ...) // this === myObject
myMethod.apply(myObject, [array of args]) // this === myObject
```

- `explicit binding`이 `implicit binding`보다 우선시된다. 

### hard binding

- `bind()`는 기존에 정의한 `this` context를 불러오도록하는 새로운 함수를 리턴한다.
- `hard binding`이 `explicit binding`보다 우선시된다.

```js
myMethod = myMethod.bind(myObject);

myMethod(); // this === myObject

var myMethod = function () { 
  console.log(this.a);
};

var obj1 = {
  a: 2
};
var obj2 = {
  a: 3
};

myMethod = myMethod.bind(obj1); // 2
myMethod.call( obj2 ); // 2
```

### new binding

- 함수가 `new`로 호출될 경우 `implicit`,`explicit`,`hard` 신경 안쓰고 새로운 context를 생성한다(`new instance`).
- 

```js
function foo(a) {
  this.a = a;
}

var bar = new foo( 2 );
console.log( bar.a ); // 2

function foo(something) {
  this.a = something;
}

var obj1 = {};

var bar = foo.bind( obj1 );
bar( 2 );
console.log( obj1.a ); // 2

var baz = new bar( 3 );
console.log( obj1.a ); // 2
console.log( baz.a ); // 3
```

### Lexical Binding

- 간결함보다 arrow function는 `this`키워드에 관해서 훨씬 더 직관적인 접근법을 가지고있다. arrow function은 일반 함수와 달리 `this`가 없습니다. 대신 `this`는 `lexically`로 결정됩니다.
  이는 정상적인 변수 조회 규칙을 따라 어떻게 예상할지 결정되는 멋진 방식입니다. 

```js
const user = {
  name: 'Tyler',
  age: 27,
  languages: ['JavaScript', 'Ruby', 'Python'],
  greet() {
    const hello = `Hello, my name is ${this.name} and I know`

    const langs = this.languages.reduce((str, lang, i) => {
      if (i === this.languages.length - 1) {
        return `${str} and ${lang}.`
      }

      return `${str} ${lang},`
    }, "")

    alert(hello + langs)
  }
}
```

- arrow function으로 인해 `this`가 `lexically`로 결정된다는 이유도 다시 한번 제기됩니다. arrow function에는 `this`가 없습니다. 대신 변수 조회와 마찬가지로 자바스크립트 인터프리터는 `this`가 참조하는 것을 판별하기 위해 둘러싸는 (부모)범위를 조사합니다.

## 1. Call() or Function.prototype.call()

```js
//Demo with javascript .call()
var obj = {name:"Niladri"};

var greeting = function(a,b,c){
  return  "welcome "+this.name+" to "+a+" "+b+" in "+c;
};

console.log(greeting.call(obj,"Newtown","KOLKATA","WB"));
// returns output as welcome Niladri to Newtown KOLKATA in WB
```

- `call()`메서드의 첫번째 파라미터는 함수가 호출되는 대상인 "**this**" 값을 설정한다. 위의 경우에는 "**obj**"이다.
- 나머지 매개변수는 실제 함수에 대한 대한 인수들이다.

## 2. apply() or Function.prototype.apply()

```js
//Demo with javascript .apply()
var obj = {name:"Niladri"};

var greeting = function(a,b,c){
  return  "welcome "+this.name+" to "+a+" "+b+" in "+c;
};

// array of arguments to the actual function
var args = ["Newtown","KOLKATA","WB"];
console.log("Output using .apply() below ")
console.log(greeting.apply(obj, args));

/* The output will be Output using .apply() below welcome Niladri to Newtown KOLKATA in WB */
```

- `call()` 메서드와 마찬가지로 `apply()` 메서드의 첫 번째 매개변수는 함수가 호출되는 대상인 **"this"** 값을 설정한다. 위의 경우엔 **"obj"** 객체이다. `apply()`와 `call()`의 유일한 차이는 두 번째 파라미터이다. `apply()`는 *배열*로 실제 함수에 대한 인수를 받아 들인다.

## 3. bind() or Function.prototype.bind()

```js
//Use .bind() javascript
var obj = {name:"Niladri"};

var greeting = function(a,b,c){
  return  "welcome "+this.name+" to "+a+" "+b+" in "+c;
};

//creates a bound function that has same body and parameters
var bound = greeting.bind(obj);

console.dir(bound); ///returns a function

console.log("Output using .bind() below ");

console.log(bound("Newtown","KOLKATA","WB"));
//call the bound function

/* the output will be Output using .bind() below welcome Niladri to Newtown KOLKATA in WB */
```

- 여기서 `bind()`는 나중에 호출 될 컨텍스트가 있는 바운드 함수를 반환하고 있다.
- bind() 메서드의 첫 번째 매개변수는 바인딩 함수가 호출될 때 대상 함수의 "**this**" 값을 설정한다. 바인딩 함수가 "**new**" 연산자를 사용하여 구성된 경우 첫 번째 파라미터의 값은 무시된다는 점에 유의하라. 나머지 매개 변수는 대상 함수를 호출 할 때 바인드 된 함수에 제공된 인수 앞에 추가되는 인수로 전달된다.

## this 참고사항

1. 함수 호출이 어디서 일어났는지 확인한다.
2. 점을 기준으로 왼쪽에 객체가 있는지 확인하고, 그것이 있다면 그게 바로 `this`키워드가 참조하는 것이다. 만약에 없다면 3번으로 가라.
3. “call”, “apply”, 혹은 “bind”와 함수가 호출되었는가? 만약에 그렇다면 `this`키워드가 참조하는 것을 명시적으로 선언할 것이다. 그렇지 않다면 4번으로 가라
4. 함수가 new 키워드와 호출이 되었는가? 그렇다면, `this`키워드는 새롭게 창조된 객체고 자바스크립트 인터프리터에 의해 생성된 것이다. 이것들과 호출된 게 아니라면 5번으로 가라.
5. 화살표 함수 안에 `this`가 있는가? 그렇다면 아마도 근처의 (부모)스코프에서 Lexically - 어휘적으로? - 찾을 수 있을 것이다. 그렇지 않다면 6번으로 가라.
6. Strict mode를 사용중인가? 그렇다면 `this`키워드는 undefined이다. 그렇지 않다면 7번으로 가라.
7. 자바스크립트는 이상한 애다. `this`는 window 객체를 참조한다.





## 참조

- [this]:https://www.codementor.io/@dariogarciamoya/understanding--this--in-javascript-du1084lyn?icn=post-8i1jca6jp&ici=post-du1084lyn