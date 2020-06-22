# 07_expression vs statement

- 표현식expression: 단 하나의 Value(값)을 반환하는 코드
- 구문statement: 행동을 수행 (값이 기대되지 않음)

## **식**

- 단일값 생성
- 반드시 상태를 변경하지는 않는다.

## **구문**

- 값이 기대되는 곳에서 사용할 수 없다.
    - 함수의 인수, 할당의 오른쪽, 피연산자, 반환 값 등
- 형태
    - if
    - if-else
    - while
    - do-while
    - for
    - switch
    - for-in
    - with (deprecated)
    - debugger
    - variable declaration

## **Function Expression VS Function Declaration**

- test

### **Function Declaration 함수구문 (선언)**

- Hoisting 됨
- 변수 할당을 요구하지 않고 명명된 함수 변수를 정의한다.
- 독립 실행형 구문으로 발생하며 비-함수 블록 내에 중첩될 수 없다.
- 읽기 쉬운 코드 작성

```
function funcDeclaration() {
    return 'A function declaration';
}
```

### **Function Expression 함수표현식**

- Hoisting 안됨 (할당된 변수 자체는 hoist되지만, 내용인 함수는 hoist 되지 않기 때문에 `undefined`가 나온다.)
- 정의된 함수의 이름은 익명으로 지정할수 있다.
- 함수 이름(존재 하는 경우)은 해당 scope 밖에서 볼 수 없다. (함수 선언식과 대조가 된다.)
- 함수를 변수에 저장한 후 변수를 함수처럼 사용한다. 변수 이름을 사용하여 호출한다.
- 함수 표현식의 이름을 지정하여 함수가 수행해야하는 것을 표현하고 디버깅을 돕는 것이 좋다.
- 장점
    - `클로저`로 사용할 때
    - 다른 함수의 인자로 사용될 때
    - 함수 표현식의 즉시 실행으로서 (IIFE)
    - 함수 선언은 Java 스타일 메서드 선언을 모방하려는 의도였지만 Java 메서드는 매우 다른 존재라고 느낍니다. Javascript 함수에서는 값이 있는한 살아있는 객체 입니다. Java 메소드는 메타 데이터 저장 공간입니다. 다음의 스니펫은 모두 함수를 정의하지만 함수 표현식만이 우리가 객체를 생성하고 있음을 암시합니다.

        ```
        //Function Declaration
        function add(a,b) {return a + b};
        //Function Expression
        var add = function(a,b) {return a + b};
        ```

    - 함수 표현식은 보다 다양합니다. 함수 선언식은 "명령문"으로만 존재할 수 있습니다. 현재 변수가 부모 변수인 객체 변수를 만드는 것뿐 입니다. 반대로 함수 표현식(정의에 의한)은 더 큰 구조의 일부 입니다. 익명 함수를 만들거나 함수를 프로토 타입에 할당하거나 다른 객체의 속성으로 할당하려면 함수표현식이 필요합니다. curry 또는 compose와 같은 고차 애플리케이션을 사용하여 새로운 함수를 만들 때마다 함수 표현식을 사용합니다. 함수 표현식 함수형 프로그래밍은 분리할 수 없습니다.

        ```
        //Function Expression
        var sayHello = alert.curry("hello!");
        ```

- 단점
    - 익명 함수는 디버깅하기 어렵다. (명명된 함수표현식을 사용할 수 있지만, IE9 하위에서 작동 안됨)

```
var funcExpression = function () {
    return 'A function expression';
}
​
// or 
​
var funcExpression2 = function hello() {
    return 'A named function expression'
}
// 함수 밖에서 hello()에 접근할 수 없다.
```

### **명명된 함수 표현식 - 두 접근법의 조합**

```
var num1 = 10;
var num2 = 20;
var addVariable = function addFunction(param1, param2) {
    return param1 + param2 ;
}
```

함수가 더 이상 익명이 아니며 addFunction 이라는 이름이 있다.(또한 변수 - addVariable에 할당됨.)

할당된 변수 이름 addVariable만 사용하여 참조하고 실행할 수 있습니다.

```
var result = addVariable(num1, num2); 
// ==> 30
```