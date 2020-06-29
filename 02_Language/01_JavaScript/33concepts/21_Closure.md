# 21_Closure

### 정의 #1 : 클로저는 스코프가 닫힌 후에도 상위 스코프에 접근 할 수 있는 함수입니다.

### 정의 #2: 클로저는 함수와 해당 함수가 선언된 'lexical environment'의 조합입니다.

```js
  //this is closure's global scope
function outie(){
  // this is closure's first and only outer scope
  function closure(){
   // this is closure's local scope
  }
}
```

[closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))는 외부의 변수를 기억하고 접근할 수 있는 함수입니다(스코프 체인에 값에 대한 참조를 저장한다.). 몇몇 언어에서는, 이러한 구현이 불가능합니다. 또한 이러한 일이 일어나게 하기 위해서는 함수를 특별한 방법으로 작성해야 합니다. 하지만 위에 기재된대로, 자바스크립트에서는, 모든 함수가 자연적으로 closure입니다. (다만 하나의 예외는 있는데, 나중에 다뤄질 것이지만 ["new Function" 문법(클래스 인스턴스)](https://javascript.info/new-function)이 있습니다.

자바스크립트의 함수들은 자신이 생성된 위치를 숨겨진 `[[Environment]]` 프로퍼티를 이용하여 기억합니다. **그리고 그렇게 만들어진 모든 함수들은 외부 변수에 접근이 가능합니다.** 인터뷰를 할 때, 한 프론트엔드 개발자가 "closure란 무엇인가요?"라는 질문을 받았습니다. 유효한 정답은 closure의 정의를 설명하고 모든 자바스크립트에서의 함수가 클로져이며, 기술적인 디테일에 대해서 몇가지 추가적인 설명을 더 해주는 것입니다: `[[Environment]]` 프로퍼티와 어떻게 어휘 환경이 작동하는지에 대해서요.



## 함수 실행 패턴

- 함수 호출 시 

1. 자바스크립트는 새로운 실행 컨텍스트, 지역 실행 컨텍스트를 만듦니다.
2. 지역 실행 컨텍스트는 자기 자신의 변수 집합을 가지고 있습니다. 이들 변수들은 지역에서 실행 컨텍스트가 될 것입니다.
3. 새로운 실행 컨텍스트는 실행 스택에 추가됩니다. 실행 스택은 실행 중인 프로그램의 위치를 추적하는 메커니즘이라고 생각합니다.

- `반환(return) 구문이 있거나 닫히는 중괄호 } 가 있는 경우`: 함수가 끝났을 때 아래의 내용이 발생

1. 지역 실행 컨텍스트는 실행 스택에서 분리됩니다.
2. 함수는 반환 값을 호출 컨텍스트로 다시 전달합니다. 호출 컨텍스트는 이 함수를 호출한 실행 컨텍스트로서 글로벌 실행 컨텍스트 또는 다른 지역 실행 컨텍스트입니다. 그 시점에서 반환값을 처리하는 것은 호출 실행 컨텍스트에 달려 있습니다. 반환값은 객체, 배열, 함수, 부울 등 무엇이든 될 수 있습니다. 만약 함수에 반환 구문이 없다면, undefined을 반환합니다.
3. 지역 실행 컨텍스트는 소멸되는 것은 중요 합니다.소멸되다. 지역 실행 컨텍스트 내에서 선언된 모든 변수는 삭제됩니다. 변수는 더이상 사용할 수 없습니다. 그래서 지역 변수라고 부릅니다.

## Lexical Environment 어휘환경

1. Environment Record(환경 기록) - 모든 로컬 변수를 속성으로 저장하는 객체
2. 외부 lexical environment(어휘 환경)에 대한 참조, 외부 코드와 관련된 것

### 변수 선언의 어휘환경

![img](https://camo.githubusercontent.com/1566474755894adef62e219742a13a5b5524eb23/68747470733a2f2f6a6176617363726970742e696e666f2f61727469636c652f636c6f737572652f6c65786963616c2d656e7669726f6e6d656e742d676c6f62616c2d322e7376673f73616e6974697a653d74727565)

1. 스크립트가 시작될 때, Lexical Environment(어휘 환경)은 비어 있습니다.
2. let phrase 이 나타납니다. 값이 지정되지 않았으므로 undefined가 저장됩니다.
3. phrase에 값이 할당 됩니다.
4. phrase 값이 변경됩니다.

### 함수 선언의 어휘환경

![img](https://camo.githubusercontent.com/3ed4603e37951b020c56fbdefb6c9abbf9bec0bb/68747470733a2f2f6a6176617363726970742e696e666f2f61727469636c652f636c6f737572652f6c65786963616c2d656e7669726f6e6d656e742d676c6f62616c2d332e7376673f73616e6974697a653d74727565)

let 변수와 달리, 실행이 변수에 도달 했을 때가 아니라 Lexical Environment이 생성되었을 때 완전히 초기화 됩니다.
최상위 기능의 경우 스크립트가 시작되는 순서를 의미합니다.
그렇기 때문에 정의하기 전에 함수 선언을 호출 할 수 있습니다.
아래 코드는 Lexical Environment가 처음부터 비어 있지 않음을 보여줍니다.

### 내외부 Lexical Environment

![img](https://camo.githubusercontent.com/1cbeeb097f7f91fe33ffcc78af66415a8c410dc7/68747470733a2f2f6a6176617363726970742e696e666f2f61727469636c652f636c6f737572652f6c65786963616c2d656e7669726f6e6d656e742d73696d706c652d6c6f6f6b75702e7376673f73616e6974697a653d74727565)

- 함수가 외부 변수가 접근하면 새로운 Lexical Environment가 자동으로 작성되어 호출의 로컬 변수 및 매개 변수를 저장한다.
  - 함수 호출 중에는 내부 환경(함수 호출의 경우) 과 외부 환경(글로벌)의 두가지 Lexical Environment이 있습니다.
  - 코드가 변수에 접근할 때, 아래와 같은 순서대로 탐색된다. 변수를 못찾으면 strict 모드에서 오류가 발생한다.
    - 내부 Lexical 환경 
    - 외부 Lexical 환경
    - ...
    - 글로벌 Lexical 환경 

### 중첩함수

- 함수 속 함수
- 내부의 중첩함수는 외부의 변수에 접근할 수 있다. 
  - 외부에서는 함수 내부의 변수에 접근할 수 없다. 
- 중첩 함수를 새 객체의 속성 또는 그 자체로 반환할 수 있다는 것입니다.

```js
function makeCounter() {
  let count = 0;

  return function() {
    return count++; // has access to the outer "count"
  };
}

let counter = makeCounter(); 
// 함수 호출할 때마다 새로운 lexical환경이 자체 count로 작성된다.
// 결과 카운터 기능은 독립적이다. 

alert( counter() ); // 0
alert( counter() ); // 1
alert( counter() ); // 2
```

![img](https://camo.githubusercontent.com/9a34cc0cdb604b17a080908cbffc53b1dcac580d/68747470733a2f2f6a6176617363726970742e696e666f2f61727469636c652f636c6f737572652f6c65786963616c2d7365617263682d6f726465722e7376673f73616e6974697a653d74727565)

- 카운터 작동 순서
  1. 중첩된 함수의 지역 어휘 환경에 접근합니다.
  2. 외부 함수의 변수들에 접근합니다.
  3. 전역 변수에 닿을 때까지 계속하여 반복합니다.

### If

![img](https://media.vlpt.us/post-images/jakeseo_me/758bae90-8cf7-11e9-bbde-c38131c8b066/lexenv-if.png)

- `user` 변수는 오직 `if` 블럭 안에만 존재합니다.

- 실행 컨텍스트가 `if` 블럭 안으로 들어갈 때, 블럭을 위한 새로운 "if-only" 어휘 환경이 만들어집니다.

  이 어휘 환경은 외부 어휘 환경으로의 참조를 갖고 있습니다. 그래서 `phrase`를 찾을 수 있습니다. 하지만 if문 내부에 선언된 모든 변수와 함수 표현식들은 그 어휘 환경 내부에 존재합니다. 그리고 바깥에서 접근될 수 없습니다.

### For, while

```js
for (let i=0; i<10; i++) {
  // 각각의 루프가 자신의 어휘 환경을 가짐
  // {i: value}
}

alert(i); // Error, no such variable
```

- For 루프 문은 모든 반복이 독립된 어휘 환경을 지닙니다. 만일, 변수가 `for` 내부에서 선언됐다면 그 변수 또한 어휘 환경의 지역 변수입니다.
- `let i`는 시각적으로는 `{...}` 외부에 있지만, 실제로는 각 루프의 반복(iteration)이 `i`를 내부에 지닌 자신의 어휘 환경을 갖는다는 것입니다. 루프 이후에는 `i`에 접근이 불가능하다.

- 실수 예시

```js
var names = ['Locke', 'Franklin', 'Smith', 'Mises'];
var logName = function(name) {
    console.log(name);
};
var name;
for (var i=0; i < names.length; i++) {
    name = names[i];
    // 이 function은 그대로 for문의 scope를 공유하기 때문에 i가 지나가면 기억못함
    setTimeout(function(){  
        logName(name);
    }, 1000);
} 
// Mises 4회 출력
```

```js
var names = ['Locke', 'Franklin', 'Smith', 'Mises'];
var logName = function(name) {
    console.log(name);
};
var name;
for (var i=0; i < names.length; i++) {
    name = names[i];
    
    setTimeout(!function(){  
        logName(name);
    }(), 1000);
} 
// IIFE로 만들었다. 
// Locke, Franklin, Smith, Mises 출력 
```



### IIFE

-  js에 블럭-레벨 어휘 환경이 존재하지 않았을 때 대신했던 것.

```js
// IIFE 만드는 방법
(function() {
  alert("Parentheses around the function");
})();

(function() {
  alert("Parenthjeses around the whole thing");
})();

!function() {
  alert("Bitwise NOT operator starts the expression");
}();

+function() {
  alert("Unary plus starts the expression");
}();
```

### 가비지 컬렉션

```js
function f() {
  let value = 123;
  function g() { alert(value); }
  
  return g;
}

let g = f(); 
// g는 f 내부의 value에 접근 가능하여 외부 어휘 환경을 메모리에 유지시킵니다.
```

-  `f`의 끝에 여전히 접근 가능한 중첩된 함수가 존재한다면, 그 때 이 `[[Environment]]` 참조는 외부 어휘 환경을 다음과 같이 살려놓습니다.