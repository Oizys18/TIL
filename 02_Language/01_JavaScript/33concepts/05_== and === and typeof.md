# 05_== and === and typeof
## `==` 와 `===`

### 요약

`==` Double Equal 동등연산자: **느슨한 평등**

- Value가 동일하면 `true`
    - 유형 강제변환(암묵적 형변환)을 수행한다.
- coercion comparison 논리구조

`===` Triple Equal 일치연산자:  **엄격한 평등**

- Value와 Type이 모두 동일해야만 `true`

### Falsy

- JS는 `0` 을 `false`(bool)로 변환한다.
- Falsy values
    - `false`- 부 울린 거짓
    - `0` - 숫자 0
    - `“”` - 빈 문자열
    - `null`
    - `undefined`
    - `NaN` - 숫자가 아님
- Falsy value comparison 규칙 (`==`)
    - `false`, `0` , `""`
        - 셋은 서로 동등하다.
    - `null`, `undefined`
        - 서로 동등하다.
    - `NaN`
        - 무엇이든 동등하지 않다.

```jsx
Triple Equals는 double equals보다 우수합니다. 가능할 때마다 평등을 테스트하기 위해 Triple Equals를 사용해야합니다. type과 value를 테스트함으로써 항상 진정한 평등성 테스트를 수행하고 있음을 확신 할 수 있습니다.
```

## `typeof` 와 `instanceof`

- type check

### `typeof`

- Primitive type 구별에만 사용한다. (`Symbol`도 가능!)
- Array, Null, 날짜, RegExp, 사용자 정의 객체, DOM 요소 등등에 `Object`를 반환한다.
    - typeof(null)은 `null`을 반환해야 하지만, `object`를 반환한다.
- `typeof(sth)` or `typeof sth` 둘 다 사용가능
- 예시

### `instanceof`

- 객체가 특정 타입(생성자,constructor)의 인스턴스인지 여부를 알려준다.
    - 예를 들어 Array가 new Array로 새 배열을 생성하는 것 처럼 constructor이기 때문
- `Null`과 `undefined`를 제외하면 Primitive type에는 작동하지 않는다.
    - 단, 생성자 속성을 확인하면 `number`, `boolean` , `string`에도 작동한다.

    ```jsx
    (3).constructor === Number // true
    true.constructor === Boolean // true
    'abc'.constructor === String // true

    // 원시 값의 속성을 참조할 때마다 자바스크립트가 
    // 다음과 같이 객체 래퍼로 자동으로 값을 감싸기 때문이다.
    var wrapper = new Number(3)
    ```

- 생성자 점검의 문제
    1. `prototype 체인`을 확인하지 않는다.

    ```jsx
    function Cat(){}
    Cat.prototype = new Animal()
    Cat.prototype.constructor = Cat
    var felix = new Cat()
    felix instanceof Cat // true
    felix instanceof Animal // true
    felix.constructor === Cat // true
    felix.constructor === Animal // false
    ```

    2. 질의 객체가 null이거나 undefined인 경우 심각한 문제를 발생한다.

    ```jsx
    felix = null
    felix instanceof Animal // true
    felix.constructor === Animal // throws TypeError
    ```