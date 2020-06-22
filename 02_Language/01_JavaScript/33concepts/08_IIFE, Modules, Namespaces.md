# 08_IIFE, Modules, Namespaces

## IIFE  (Immediately Invoked Function Expression)
- 익명의 클로저를 통해 "privacy"를 제공하는 설계 패턴

### 기본 사용법
```js
!function() {
    alert("Hello from IIFE!");
}();

void function() {
    alert("Hello from IIFE!");
}();
```
- IIFE 패턴의 핵심은 함수를 사용하여 이를 표현식으로 바꾸고 즉시 실행하는 것이다.
- 첫 번째 문자 인 !은 함수 문, 정의 대신 해당 함수를 표현식으로 만드는 것이다. 그런 다음 즉시 function을 실행한다.
- 전에 보았듯, function 문은 항상 function 키워드로 시작한다. 자바스크립트는 function키워드를 유효한 문장의 첫 단어로 볼 때마다 함수 정의가 수행될 것으로 예상한다. 그래서 이런 일이 발생하지 않도록 1번 라인의 function키워드 앞에 ! 접두사를 붙인다. 기본적으로 자바스크립트는 !다음에 오는 모든 것을 표현식으로 처리하도록 한다.

```js
// Variation 1
(function() {
    alert("I am an IIFE!");
}());
// 함수 표현식 호출을 위한 괄호()는 바깥 괄호 안에 포함된다. 다시 바깥 괄호는 그 함수 밖의 함수 표현식을 만드는 데 필요하다.


// Variation 2
(function() {
    alert("I am an IIFE, too!");
})();
// 표현식을 호출하기위한 괄호() 는 함수 표현식의 줄 바꿈 밖에 있다.
```
- 두 Variation 모두 널리 사용된다. 나는 개인적으로 Variation 1을 선호하는 편이다. 핵심 부분에 들어가면 두 가지 Variation가 어떻게 작동하는지 약간 다르다. 
- 표현식 호출 괄호가 밖에 있든 안에 있든 문제없음


```js
// Valid IIFE
(function initGameIIFE() {
    // 게임을 초기화하는 모든 MAGIC 코드!
}());

// 두가지 IIFE 예제
function nonWorkingIIFE() {
     // 괄호가 필요한 이유를 알았다!
     // 이러한 괄호가 없으면 표현식이 아니라 함수 정의이다.
     // 구문 오류가 발생!
}();

function () {
    // 구문 에러가 발생!
}();
// 기억하라! IIFE를 형성하려면 함수 표현식이 필요합니다. 함수 문장, 정의는 IIFE를 작성하는 데 사용되지 않는다
```

### IIFEs and private variables
- IIFE 내부에서 선언 된 변수는 외부에서 볼 수 없다. ( == 기능범위를 만들 수 있다!)
```js
(function IIFE_initGame() {
    // Private variables that no one has access to outside this IIFE
    var lives;
    var weapons;
    
    init();

    // Private function that no one has access to outside this IIFE
    function init() {
        lives = 5;
        weapons = 10;
    }
}());
```
- `IIFE_initGame`은 IIFE, `lives`와 `weapons`는 private variable 
- `init`와 `lives`,`weapons`은 외부에서 접근 불가능하지만 `init`은 `lives`와 `weapons`에 접근 가능하다. 

### IIFEs with a return value
```js
var result = (function() {
    return "From IIFE";
}());

alert(result); // alerts "From IIFE"
```
- return 값이 필요없으면 `!`, `+`, `void` 등으로 보았던 IIFE 변형 사용해도 된다.
- 하지만 IIFE의 장점 중 하나가 변수에 할당 할 수있는 값을 리턴할 수 있다는 것이다.
- `result`를 alert하면 IIFE의 리턴값을 보여준다.

### IIFEs with parameters
- IIFE는 값을 리턴 할 수 있을 뿐만 아니라 IIFE도 호출되는 동안 인수를 사용할 수 있다. 간단한 예를 보자.

```js
(function IIFE(msg, times) {
    for (var i = 1; i <= times; i++) {
        console.log(msg);
    }
}("Hello!", 5));
```
- 위의 예에서 1번째 줄에서 IIFE는 각각 msg, times라는 두 개의 매개 변수를 갖는다.
- 5번째 줄에서 IIFE를 실행할 때, 지금까지 보아온 빈 괄호() 대신에 IIFE에 인수를 전달한다.
- 2-3번째 줄은 IIFE 내부의 파라미터를 사용한다.

```js
(function($, global, document) {
    // use $ for jQuery, global for window
}(jQuery, window, document));
```
- 위의 예제에서 우리는 3번째 줄의 IIFE에 인수로 jQuery, window 및 document를 전달합니다. IIFE 내부의 코드는 $, global, document로 각각 참조 할 수 있다.

- JavaScript는 항상 현재 함수의 범위에서 범위 조회를 수행하고 식별자를 찾을 때까지 상위 범위에서 계속 검색한다. 3번째 줄로 document를 전달할 때 document의 로컬 scopes를 벗어나는 scopes 조회를 수행하는 유일한 경우이다. 문서화 할 IIFE의 모든 참조 사항은 IIFE의 지역 범위를 넘어 조회 할 필요가 없다. jQuery에도 똑같이 적용된다. 이것에 의한 성능 향상은 IIFE 코드가 얼마나 사소하고 복잡한 지에 따라 거대한 것은 아니지만 여전히 유용한 유용한 트릭이다.

- 또한 JavaScript minifier는 함수에서 선언 된 매개 변수 이름을 안전하게 축소 할 수 있다. 이러한 매개 변수를 매개 변수로 전달하지 않으면 minifier가이 함수의 범위를 벗어나는 문서 또는 jQuery에 대한 직접 참조를 축소하지 않는다.



### ES6로 IIFE를 대신한다?
```js
//IIFE
(function() {
  var scoped = 42;
}());

console.log(scoped); // ReferenceError

//ES6
{
  let scoped = 42;
}

console.log(scoped); // ReferenceError
```
- 둘은 동일하게 작동함


```js
var myModule = (function() {
  // private 변수, IIFE 안에서만 접근할 수 있다.
  var counter = 0;

  function increment() {
    counter++;
  }

  // 외부로 노출되는 로직
  return {    
    increment: increment
  }
}());

// myModule.js

let counter = 0;

export function increment() {
  counter++;
}    

// logic.js

import {increment} from 'myModule.js';

increment();
```
- 이 둘도 동일하게 작동


```js


const SENTENCE = 'Hello world, how are you?';
const REVERSE = (() => {
  const array  = [...SENTENCE];
  array.reverse();
  return arr.join('');
})();
```
- IIFE를 사용하는 경우는 즉시 호출되는 화살표 함수를 사용할 때이다. 때로는 단일 표현식이 아니라 일련의 구문을 통해서만 결과를 생성할 수 있으며, 이러한 구문을 인라인화 하려면 즉시 함수를 호출해야 한다;



##  Module
```
- js 코딩은 변수 관리가 중요하다. 
- Scope를 통해 변수 유지관리를 하는데 이 때 다른 scope에서 같은 변수를 사용할 경우 전역변수 처리를 해서 함께 사용할 수 있다.
- 하지만 전역 변수로 만들어 사용할 시 발생할 수 있는 여러문제가 존재해서, 이를 해겨하기 위해 모듈을 사용한다.
```
### 모듈을 사용하는 이유
- 모듈은 이러한 변수와 함수를 구성하는 더 좋은 방법을 제공합니다. 모듈을 사용하면 함께 사용하기에 적합한 변수와 함수를 그룹화 할 수 있습니다. 이러한 함수와 변수를 모듈 범위에 넣습니다. 모듈 스코프를 사용하여 모듈의 함수간에 변수를 공유 할 수 있습니다.
- 그러나 함수 범위와 달리 모듈 범위는 변수를 다른 모듈에서도 사용할 수 있는 방법을 제공합니다. 모듈의 어떤 변수, 클래스 또는 함수가 사용 가능해야하는지 명시 적으로 말할 수 있습니다. 다른 모듈에서 사용할 수있는 것이 있으면 이를 export라고합니다. export를하면 다른 모듈은 해당 변수, 클래스 또는 함수에 의존한다고 명시 할 수 있습니다.

- 모듈은 명시적인 관계이기 때문에 다른 모듈을 제거하면 어떤 모듈이 파손될지를 알 수 있습니다.
- 일단 모듈들 사이에 변수를 export하고 import 능력을 갖게 되면, 당신의 코드를 서로 독립적으로 작동할 수 있는 작은 덩어리로 분해하는 것을 훨씬 더 쉽게 만듭니다. 그런 다음 이 덩어리를 결합하고 다시 결합하면, 마치 레고 블록과 같은, 동일한 모듈에서 모든 종류의 어플리케이션을 만들 수 있습니다.
- 모듈이 매우 유용하기 때문에, 자바스크립트에 모듈 기능을 추가하려는 시도가 여러 번 있었습니다. 오늘날에는 두 가지 모듈 시스템이 활발하게 사용되고 있습니다.
CommonJS(CommonJS, CJS)는 Node.js가 역사적으로 사용해 온 것이다. ESM(EcmaScript 모듈)은 자바스크립트 규격에 추가된 최신 시스템입니다. 브라우저는 이미 ES 모듈을 지원하며, Node는 지원을 추가하고 있습니다.

- 장점 :

1. 코드는 작은 파일들로 분할될 수 있습니다.
2. 어느 애플리케이션에서(애플리케이션의 어디든지) 동일한 Module을 공유할 수 있습니다.
3. 이상적으로, Module들은 다른 개발자들에 의해 검증될 필요가 없습니다. 왜냐하면 Module들의 기능이 입증되었기 때문입니다.(일부 의역 : works을 기능으로)
4. Module을 참조하는 코드는 의존성을 이해합니다. Module 파일이 변경되거나 이동되면 즉시 문제가 됩니다.
5. Module 코드는 (보통) 네이밍 중복을 줄이는데 도움을 줍니다. module1에서의 함수 x()는 module2에서 함수와 충돌이 되지 않습니다. 네임스페이스와 같은 옵션들이 사용되어서 module1.x() 와 module2.x()이 됩니다.

### 작동방식
- 모듈을 사용하여 개발할때 의존성 그래프를 작성합니다. 서로 다른 종속성 사이의 연결은 사용하는 모든 import 문에서옵니다.
- 이 import 문은 브라우저 또는 Node가 로드해야하는 코드를 정확히 인식하는 방법입니다. 그래프의 진입점으로 사용할 파일을 제공합니다. 여기에서 나머지 코드를 찾으려면 import문을 따르면 됩니다.

