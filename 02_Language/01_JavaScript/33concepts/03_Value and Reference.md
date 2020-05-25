# JS 33 concepts - Value and Reference

- 자바스크립트는 메모리에 있는 데이터 구조의 전체 접근 권한을 주지 않는다. 대신 언어 차원의 reference type을 제공한다.
- 모든 변수가 생성된 후에 고정된 양의 메모리가 할당됩니다.
- 변수가 복사 될 때 ,메모리 내의 값이 복사됩니다.

### Primitives Type 원시타입 : Value 전달(Pass-by-value(복사))
- == 스칼라 or 단순한 타입
    - `Boolean`
    - `null`
    - `undefined`
    - `String`
    - `Number`

- 변수 할당 시 값을 복사함, 서로 영향을 주지 않음
- 고정된 양의 메모리에 저장
```
# JS의 Strings
Strings 은 자바스크립트에서 특별한 존재이다. 다른 많은 언어와 달리 string은 character의 배열처럼 정의 되지 않는다. 무엇보다 character 타입이 자바스크립트에는 존재하지 않는다. Strings는 변화하지 않는 데이터 타입으로 문자 배열처럼 보이게 하는 인터페이스를 지니고 있다. 실제로 문자열을 수정하면 새로운 불변의 값이 생겨난다.
```
### Object 오브젝트 : Reference 전달(Pass-by-reference(참조))
- == (Compound Value)복합타입, 컨테이너 유형
    - `Array`
    - `Function`
    - `Object`
- 참조 유형의 내용은 변수에 이용될 수 있는 고정된 메모리 양에 맞지 않을 수 있습니다. 참조 유형의 메모리안의 값은 참조 유형 자체의 값 입니다.
- 메모리의 일부 위치에 생성되고, 메모리의 값에 대한 참조가 제공된다.
- `참조에 의한 할당`: 변수 할당 시 값 대신 참조로 복사된다.
  - Object로 작업할 때 =로 할당되는 것은 원래의 객체에 대해 비슷한 객체를 생성하는 것이고 새로운 객채를 생성하지 않는다. "by reference"라는 말이 바로 그 뜻이다.

- `참조 재할당`: 기준 변수(이미 할당된 변수)에 재할당하면 기존 참조가 대체된다.
  - 이후 가비지 컬렉터가 삭제한다.




### `===` 예시 체크
 ```javascript
console.log([10] === [10]);   // false!

var oldArray = [];
var object = {};
object.newArray = oldArray;
oldArray.push(10);
console.log(object.newArray === oldArray);  // true!

```