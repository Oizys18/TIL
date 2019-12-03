# JavaScript

- 새로운 언어를 배울 때?
  - 문법적 차이
  - 언어의 관례 

1. 저장 + 조작(제어문)   +  (함수) + 혹은 (클래스) 
   - 저장
     - 무엇을(자료형, Data type) | 어디에(identifier 변수명, Container type) | 어떻게(`=`) | 저장하는지?
2. 구현 driven 연습 / framework 연습 

## 개요

- 유형 및 연산자, 표준 내장 객체 및 메소드가 있는 다중 패러다임, 동적 언어
- Java 및 C 언어 기반 구문
- 객체 프로토 타입을 사용한 객체 지향 프로그래밍 지원 + 함수형 프로그래밍 지원 
- 함수 === 객체, 실행 가능한 코드를 유지하고 전달 가능

## 상식

- HTML이 뼈대, CSS가 살을 붙였다면 JS는 동작(움직임)을 위해 존재
- Java와 Javascript는 아예 다른 언어 (관련 없다) : JS는 Browser 조작용 언어 
- ECMA script 
  - 사실상 Javascript
  - Ecma 인터내셔널의 **ECMA-262** 기술 규격에 정의된 표준화된 [스크립트 프로그래밍 언어](https://ko.wikipedia.org/wiki/스크립트_프로그래밍_언어)이다. [자바스크립트](https://ko.wikipedia.org/wiki/자바스크립트)를 표준화하기 위해 만들어졌고 지금도 자바스크립트가 제일 잘 알려져 있지만, [액션스크립트](https://ko.wikipedia.org/wiki/액션스크립트)와 [J스크립트](https://ko.wikipedia.org/wiki/J스크립트) 등 다른 구현체도 포함하고 있다.
- ECMA international
  - 정보와 통신 시스템을 위한 국제적 표준화 기구이다. 여러 Vendor들이 각자의 방식대로 언어를 만들어서 표준화가 되지 않자 ECMA에서 하나의 표준을 만든다.  ES2015(ES6)부터, 크롬/파이어폭스 등 major 벤더들이 ECMA Script의 규격을 지키며 개발하면서 점차 대중화되었다. 
- Vanilla JS 
  - Jquery 등의 라이브러리를 사용하지 않은 original JS
- Node JS 
  - JS는 원래 브라우저 조작언어였으나, JS Runtime : Node JS를 통해 브라우저 밖에서도 일반 프로그래밍언어처럼 JS를 사용가능하게 되었다. 하나의 언어라고 봐도 무방  
- `eventListener` 사용 시 ArrowFunction 사용 금지
- JS는 HTML의 오브젝트를 트리형태로 사용
  - document > body > p > ... 
- `addEventListener`의 인자로 콜백함수를 넣을 때는 `arrowFunction`을 사용하지 않는다! 
- JS의 `this`: 

## 설치

- NodeJS

  - https://nodejs.org/ko/

- bash

  - ```
    # 버전 확인
    node -v
    npm --version
    
    
    # js 실행
    node [js file name]
    ```

# 00_js_intro

## 00_variable.js

### 기본 문법 

1. 출력

   - `console.log()`

2. Variable Assign 할당 / Declare 선언 

   - `let x = 1` 

     - Declare 선언 `let`은 한 개의 변수에 한 번만 사용할 수 있다.
     - `let`없이 그냥 `x=1` 처럼 사용하면 전역변수 공간에 Assign 할당된다. 
     - (하지만 global 변수는 되도록 사용 X)

   - ```javascript
     // Declare 
     let x = 1 
     // Assign 
     x = 2
     if (x==2) {
         let x = 3
         console.log(x)
     }
     console.log(x)
     
     >> 
     3   // {} 안에서만 x=3으로 선언되었기 때문 
     2   // 전역에서 선언된 x = 2 
     ```

3. Constant variable 상수 선언 

   - 재선언 / 재할당 둘 다 불가. (변경 불가)

   - 상수 변수는 대문자로 작성 

   - ```javascript
     const MY_FAV = 10
     console.log(MY_FAV)
     
     >>
     10
     ```

4. Concatenation & Interpolation 

   - ```javascript
     // 상수(불변) 선언: 대문자로 작성  
     const MY_FAV = 10
     console.log('내가 좋아하는 숫자는 ' + MY_FAV)
     
     // backtick ` ` 사용, ${}안에 변수 
     console.log(`내가 좋아하는 숫자는 ${MY_FAV}`) 
     ```




### 저장 & 제어

#### 1. 무엇을(자료형, Data type) 

- `type()` in python === `typeof` in python 
- 숫자 / 글자 / Boolean : Primitive types 원시자료형
  - 숫자 
    - `NaN` : Not a Number (type은 number)
    - `(-)Infinity` 
  - 글자
    - `(``)` , `('')`, `("")`
  - Boolean
    - `true` (cf: `True`엔 아무것도 없다. `undefined`)
    - `false`
  - Empty Value
    - `undefined`: default, `typeof undefined`는 undefined
    - `null`: `typeof null`은 `object`다.
    - `null == undefined` >> true 
    - `null === undefined` >> false : `===`는 strict하게 비교하는 것.(객체타입까지 비교) 

#### 2. 어디에(identifier 변수명, Container type)

- 상수명: `ALLCAP`

- 변수명, 함수명: `camelCase`

- 클래스: `PascalCase`

- `prompt()`: `const userName = prompt('당신의 이름을 입력!')`: input 입력 팝업 생성 



## 01_functions.js

### 논리 / 조건 / 제어 

- JS에서 `==`와 `===`의 차이  (묵시적 형변환)

  - JS는 시작이 브라우저 조작언어였기 때문에, 매우 유연하게 작성되었음
  - JS는 임의적으로 (자동) 형변환을 통해 연산해줌(혼파망..)
    - `'5'==5` >> `true`
    -  `'1'-1` >>`0`
    - `'2'+5` >> `'25'`
  - 따라서 데이터타입까지 비교하는 `===`를 사용한다거나 아예 TS(Typescript)를 사용하자..

- [논리연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/논리_연산자(Logical_Operators))

  - `||` : or 
  - `&&`: and
  - `!`: not
  - `true ? '참':'아니오'`: `?` 이전의 값이 참이면 `?`에 뒤따라 오는 값이 반환, 거짓이면 뒤쪽 값 반환

- 조건문

  - `alert()`: 경고창 팝업 생성

    - ```javascript
      //만약 이름이 3자 이상이면
      // 이름이 3자 이상입니다
      // 아니면
      // 3자 이하입니다.
      
      if (userName.length >= 3){
          alert('이름이 3자 이상입니다.')
      } else {
          alert('이름이 3자 이하입니다.')
      }
      ```

- 반복문: https://www.opentutorials.org/module/570/4962

  - ```javascript
    1. for (변수 of container) { 실행 }
    
    // lambda와 비슷, function을 인자로 넣기 (python의 map과 유사한 것 )
    2. container.forEach(function() { 실행 })    
    
    3. container.forEach(i => {실행})
    
    // C 스타일
    4. for (let i = 1; i <= 10; i++) {실행}
    ```

- [함수 생성](https://velog.io/@imacoolgirlyo/JS-자바스크립트의-Functions-함수)

  - ```javascript
    // 함수 선언문 Function Statements
    function functionName(param1, param2, ..){
    	return sth sth sth 
    }
    
    // 함수 생성 후 functionName을 호출하면 함수 자체가 출력됨 
    ```

  - ```javascript
    // 함수 표현식 Function Expressions *이렇게만 사용할 것*
    const functionName = function(param1, param2 ..){
        return sth sth 
    }
    ```

  - 표현식 정의를 사용해야하는 이유: 호이스팅 Hoisting 때문이다. 

  - 자바스크립트는 선언된 변수와 함수를 먼저 메모리에 저장한 이후에 코드를 위에서부터 차례대로 실행한다. 결론, 함수 표현식은 호이스팅이 되지 않고 함수 선언으로 선언된 함수는 호이스팅 된다. 즉 함수가 정의되기 전에 함수를 호출할 수 있다.... 함수표현식만 사용하자.. 



## 02_array.js

- indexing  : `const nums = [1,2,3,4]`

  - ```javascript
    // 첫인자
    console.log(nums[0])
    // 마지막인자  '-1' 안된다..
    console.log(nums[nums.length-1])
    ```

- 조작

  - ```javascript
    // Stack 처럼 사용 가능 
    // push
    nums.push(0)
    // pop()
    nums.pop()
    ```

  - ```javascript
    // Queue 처럼 사용 가능 
    // unshift 맨 앞에 넣기 
    nums.unshift(5)
    // shift 맨 앞자리 pop
    nums.shift()
    ```

  - ```javascript
    // includes: python 'in'
    console.log(nums.includes(2)) //true
    console.log(nums.includes(100)) //false
    ```

  - ```javascript
    // indexOf: indexing
    console.log(nums.indexOf(3)) // 3의 index 반환 
    ```

## 03_objects.js

- ```javascript
  // JS는 '키'로 작성하지 않아도 찰떡같이 알아서 작성해줌 
  const me = {
      name:'john',
      sleep:function(){        // 함수 넣어서도 사용가능 
          console.log('zZZ')
      },
      appleProducts: {         // 딕셔너리처럼 넣어서 사용가능 
          macBook:'2018Pro',
          iPad:'2018Pro',
      },
  }
  ```

- ```javascript
  // 하지만 호출시에는 '키'로 꼭 붙여줘야함 
  console.log(me['name']) // john
  
  // property 접근처럼, '.'으로도 접근 가능  
  console.log(me.name) // john 
  
  // 함수 호출 가능 
  console.log(me.sleep) // [Function: sleep]
  console.log(me.sleep()) // zZZ
  
  // dot notation 
  console.log(me.appleProducts.macBook) // 2018Pro
  ```

# 01_js_browser

### 00_dino.html

- ```javascript
  // '#id'로 id가 지정된 query select 가능 
  const dino = document.querySelector('#dino')
  // object로 만들어준다..
  dino.src // dino의 src 조회 가능, dot notation으로 확인가능 
  // query selector를 사용하면 굳이 자식 > 자식 등 매번 하나하나 부를 필요없이 바로 사용할 수 있다.
  ```

- ```javascript
  const bg = dino.parentNode
  const bg = dino.parentElement
  const bg = document.querySelector('.bg')
  // 모두 같음, dino의 parent를 가져오는 것 
  ```

- ```javascript
  bg.firstElementChild.remove()
  //dino가 삭제된다.
  ```

- ```javascript
  const newDino = document.createElement('img')
  bg.appendChild(newDino)
  bg.insertBefore(newDino, bg.firstElementChild)
  
  //여러 방법.. 
  ```

- ```javascript
  // eventlistener : 움직임/ 동작 감지 등등 
      const dino = document.querySelector('#dino')
  
      dino.addEventListener('mousedown', function(e) {
          isDown = true;
          offset = [
              dino.offsetLeft - e.clientX,
              dino.offsetTop - e.clientY
          ];
      }, true);
  
      document.addEventListener('mouseup', function() {
          isDown = false;
      }, true);
  ```

  - https://www.w3schools.com/jsref/dom_obj_event.asp


### 01_shopping_list.html

```html
<body>
  <h1>My Shopping List</h1>
  Enter a new item: <input id="item-input" type="text">
  <button id="add-button">Add Item</button>
  <ul id="shopping-list">

  </ul>

  <script>
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')
    
    button.addEventListener('click', e => {
      const itemName = input.value 
      input.value=''

      const item = document.createElement('li')
      item.innerText = itemName

      const deleteButton = document.createElement('button')
      deleteButton.innerText = 'delete'
      item.appendChild(deleteButton)

      deleteButton.addEventListener('click', e =>{
        item.remove()
      })

      shoppingList.appendChild(item)
    })
  </script>
</body>
```







### 02_giphy.html & main.js

- - 



# 02_js_async

### Asynchronous 비동기 VS Synchronous 동기

- http://latentflip.com/loupe
- https://nesoy.github.io/articles/2017-01/Synchronized
- 1. **JS는 기본적으로 Synchronous한 언어이다.** 단, 몇 개의 함수를 Asynchronous하게 구현한 것이다.
  2. **JS의 엔진은 내부적으로 Multi-thread다.** 그냥 single-thread처럼 보이는 것
- JS는 웹브라우저 조작을 위한 언어로 시작되었기 때문에 request/Response/Call을 비동기적으로 구현  
- 전체 파일을 확인하면서 실행하는 순서는
  1. 위에서부터 차례대로 바로 실행되는 함수는 실행
  2. 시간이 오래 걸리는 함수는 stack에서 관리
  3. 병렬적이라면 위에서부터 실행 
  4. 비동기적으로 실행되는 함수가 다수일 때, 먼저 호출되었더라도, `eventloop`가 실행중인 함수들을 계속 확인하면서 실행이 완료되었는지 확인하고, 먼저 완료된 함수부터 결과를 return 한다. 
  5. 이러한 비동기적인 코드를 관리하기 위해서 callback 함수로 관리한다. 
- 대표적인 Async함수
  - `addEventListener`
  - `setTimeout`
  - `XMLHttpRequest`
  - `readFile & writeFile`

### 01_async_file.read.js

- `fs`의 `readFile & writeFile`은 async하다. 
- 동기적으로 사용하려면 `readFileSync & writeFileSync`를 사용가능 

```javascript
const fs = require('fs') 
let content = ''
fs.readFile('products.json', (err, data) => {
	console.log('파일 읽기')
    console.log(JSON.parse(data))
    setTimeout(()=>{console.log('1초 기다려라')},1000)
})
>> '파일 읽기'

content = fs.readFileSync('products.json')
console.log(JSON.parse(content))
console.log('끝')
>> 'content'출력
>> '끝'출력


```



### 02_axios.js & 00_dog.html

- `Promise`: `callback`대신 사용 	





# Django RECAP 좋아요 버튼 수정

- `base.html`에 `axios`CDN 추가 
- `detail.html`의 좋아요 ` 버튼에 `data-id="{{ article.pk }}"` 추가,  `id='like-button'`지정 
- `detail.html`의 `<script>`에서 button에 `addEventListener`
- `article.pk`는 `const articleId = e.target.dataset.id` 처럼 `target`을 이용해 가져온다.

```javascript
// (페이지 로드 없이 제자리에서 로드한다.)
// 좋아요 버튼을 클릭하면, 좋아요 DB를 업데이트하고, 버튼을 바꾼다. (EventListener사용))
const likeButton = document.querySelector('#like-button')

likeButton.addEventListener('click', function(e){
  // 좋아요 DB를 변경 (like함수) == articles/<aricle:pk>/like로 요청보냄 
  const articleId = e.target.dataset.id
  axios.get(`/articles/${articleId}/like/`)
      .then(response => {
        document.querySelector('#like-count').innerText = response.data.count
        if (response.data.liked){
          // e.target.className은 안의 내용을 전부 갈아엎어버리기 때문에 안쓰는게 좋다. 
          
          console.log(e.target.classList)
          e.target.classList.remove('btn-primary')
          e.target.classList.add('btn-outline-primary')
          e.target.innerText = 'Unlike'
        } else {
          console.log(e.target.classList)
          e.target.classList.remove('btn-outline-primary')
          e.target.classList.add('btn-primary')
          e.target.innerText = 'Like'
        }
      })
})
```

