# Vue.js

- https://kr.vuejs.org/v2/guide/index.html

## 정의

- 사용자 인터페이스를 만들기 위한 **프로그레시브 프레임워크**
- SPA 완벽 지원
- 선언적 렌더링
- 컴포넌트 시스템
- 

- [Vue.js 창작자 Evan You 인터뷰](http://blog.naver.com/PostView.nhn?blogId=fastcampus&logNo=220969253285&refer=개발자스럽다)

- https://medium.com/hivelab-dev/vue-js-spa-tutorial-part1-d74aca1bba58 

- JS를 사용하는 이유? Browser에서 (html page의) `Client Side Rendering`을 하기 위함. 
  - 새로운 페이지 로드 없이 현 페이지에서 Render 
  - 근본적으로 UX의 극대화를 위해서이다. 
  
- Django의 Rendering은 `Server Side Rendering`
  
  - Request와 Response의 구조
  
- `SPA`: Single Page Application: 한 페이지에서 지속적으로 렌더
  
  - Vue.js
  - Angular.js
  - React.js 
  
-  VScode extensions

   -  Vetur
   -  Vue VSCode Snippets

-  VSCODE Vue파일 tab:2 설정 : `ctrl + shift + p` > `settings.json` 추가 

   -  ```
      "[vue]": {
              "editor.tabSize": 2
          } 
      ```

   -  vscode 윈도우 우측 하단 spaces:2로 설정 

-   https://ovenapp.io/ 

## 상식

- 기존의 MTV 모델

- 기존의 MTV 모델과 달리, Vue에서는 View와 Model이 하나로 묶임

-  https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=ko 
  - Vue 크롬 extensions : Vue 디버깅 가능! 

- 템플릿 안에서는 최대한 계산/연산을 줄이고, 인스턴스(특히 메소드)에서 모든 연산을 끝내고 값만 주는게 제일 좋다. (convention)


<hr>

## 기본 문법

### Vue 인스턴스

```javascript
// Vue클래스를 app에 저장
const app = new Vue({
    // vue 인스턴스(view model)이 어떤 HTML 요소에 Mount(적용)될지를 지정
    el: '#app',
    
    // Vue 인스턴스가 사용할 data
    data: {
      자료이름(identifier):값,
    },
    
    // Vue 인스턴스가 사용할 메소드들 
    methods: {
      함수정의:{},
    },
    
    // 미리 계산된 값을 반환한다. -> **Caching**
    computed: {}, 
    
    // Vue 인스턴스의 data 변경을 관찰하고 이에 반응 
    watch: {
        지켜볼 data: {
        	// 이름 변경 금지
        	// handler 메소드 정의 -> 지켜볼 데이터가 변경되었을 때 실행할 함수()  
        	handler(지켜볼 data){
			},
            // deep copy 한다는 것 
            deep: true,
    	},
    },
  })
```

### Vue Directive

```html
<p v-for>반복문</p>
<p v-if v-else v-else-if>조건문</p>
<p v-model>모델</p>
<p v-on:이벤트>이벤트</p> === <p @이벤트></p>
<p v-bind:html속성이름>바인딩</p> === <p :html속성이름></p>
<p v-html></p>
<p v-text></p>
<p v-show></p>
```

<hr>

#  00_vuejs_intro

## 00_vue_start.html

- Vue로 Todolist 만들기

- `v-on`의 축약형: `@`

  - ```html
    <!-- Vue를 사용할 div를 생성 -->
    <div id="app">
        <h1>댓글달기</h1>
        <input type="text" v-model="msg">
        <p>{{ msg }}</p>
    <div>
        <h2>좋아요</h2>
        <!-- @를 통해 사용할 수 도 있다...!!!! -->
        <!-- <button v-on:click='like'>좋아요</button> -->
        <button @click='like'>좋아요</button>
        <p>좋아요 갯수 : {{ likeCount }}</p>
      </div>
    ```

- `for`문:  `v-for='i for iterator'` 사용

  - ```html
    <ul>
        <li v-for='todo in todos'>
            {{ todo.content }}
        </li>
    </ul>
    ```
    
  - **주의!** `v-for`를 사용해 데이터를 순회할 때, 데이터는 꼭 `id` column을 통해 키 값을 줘야한다. 

    ```
    1. Vue는 최대한 자원을 아끼려고 한다. 재사용이 가능해 보이는 부분이 있으면 그대로 사용한다. 
    따라서 비슷한 데이터가 있으면 지워야하는데도 안 지울 수도 있다.. 
    2. Vue는 id값을 지정해주지 않으면 데이터 중 어떤 데이터를 렌더해야하는 지 헷갈려 한다..
    ```

- `if`문: `v-if='조건'` 사용, `else`문: `v-else` 사용

  - ```html
    # v-if에 해당되면 todo 출력,
    # 나머지는 v-else 부분의 '[완료]' 출력
    <ul>
          <li v-for='todo in todos' v-if='!todo.completed'>
            {{ todo.content }}
            {{ todo.completed }}
          </li>
          <li v-else>[완료]</li>
        </ul>
    
    ```

- `complete` 체크 기능 추가

  - iterator의 개체를 object로 넣는다.

  - ```javascript
    data: {
            todos: [
              { content:'헬스', completed:false},
              { content:'알고리즘공부', completed:false},
              { content:'TIL 정리', completed:false},
          ]
          },
    ```

  - methods 수정

  - ```javascript
    methods: {
            // changeName: function(){}의 축약형,
            check(todo) {
              todo.completed = !todo.completed
            },
          }
    ```

- static 파일 사용하기 : `v-bind`

  - `v-bind`의 축약형: `:`, 동적 자료를 사용하려면 `v-bind`꼭 사용!

  - ```html
    # v-bind 태그 사용후 data에서 불러온다.
    <img v-bind:src="imgSrc">
    # v-bind의 축약형 ':'
    <img :src="imgSrc">
    ```

  - ```javascript
    data: {
        imgSrc:"URL",
    }
    ```

  - style 적용에도 사용한다!

    - 적용할 곳에 `:class='red'` 추가

    - data에 `red: "red",`

    - ```html
      <style>
        .red {
          color:red;
        }
        </style>
      ```

- Boolean : `V-model`

  - Vue.js

    ```
    1. 적용하고자 하는 태그에 v-model="<model>" 적용
    2. data에 <model> 추가
    ```
    
  
- 조건에 따른 클래스 적용

  - ```
    :class="{completed:false}"
    
    ```

이후 method에서 조건 추가한 function 적용한다.

- `select`

  - 조건에 따른 리스트 출력 

  - ```html
    <select v-model="status">
          <option value="all" selected>전체보기</option>
          <option value="active">진행중</option>
          <option value="completed">완료</option>
        </select>
    ```

- `v-for`의 `id` 필수적으로 bind할 id를 줘야함 : Vue에서 개별 DOM 노드들을 추적하고 기존 엘리먼트를 재사용, 재정렬하기 위해서 `v-for`의 각 항목들에 고유한 key 속성을 제공해야 합니다. `key`에 대한 이상적인 값은 각 항목을 식별할 수 있는 고유한 ID입니다. 이 특별한 속성은 1.x 버전의 `track-by`와 거의 비슷하지만 속성처럼 작동하기 때문에 `v-bind`를 사용하여 동적 값에 바인딩 해야합니다. (여기서는 약어를 이용합니다.)

  ```
  <div v-for="item in items" v-bind:key="item.id">
    <!-- content -->
  </div>
  ```

  반복되는 DOM 내용이 단순한 경우나 의도적인 성능 향상을 위해 기본 동작에 의존하지 않는 경우를 제외하면, 가능하면 언제나 `v-for`에 `key`를 추가하는 것이 좋습니다.

## 01_methods_computed.html

- `computed`와 `methods`의 차이?

  - ```
    1. computed와 methods는 둘 다 리로드가 될 때마다 새로 계산된다.
    단, 예를 들어 아래와 같은 경우 Toggle 시 computed는 리로드 전까지 최초 로드에 Caching됐던 값을 반환하지만 Methods는 Toggle될 때마다 새로운 값을 반환한다.
    
    >> 즉 계속해서 새로운 값을 반환할 필요가 없는 연산의 경우 Computed를 사용해 효율성을 높이자!
    
    2. methods는 템플릿에서 호출할 때 {{ method() }}
       computed는 템플릿에서 호출할 때 {{ computed }} -> 이미 계산된 값이니까!
    ```

  - ```html
    <button @click="visible = !visible">Toggle</button>
        <ul v-if="visible">
          <li>methods로 불렸을 때 : {{ dateMethod() }}</li>
          <li>computed로 불렸을 때 : {{ dateComputed }}</li>
        </ul>
    ```

  - ```javascript
    methods: {
          dateMethod(){
            return new Date()
          }
        },
        computed: {
          dateComputed(){
            return new Date()
          }
        },
    ```

<hr>

# 01_vuejs_component

## [Component](https://kr.vuejs.org/v2/guide/components.html#컴포넌트가-무엇인가요)

컴포넌트는 Vue의 가장 강력한 기능 중 하나입니다. 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화하는 데 도움이 됩니다. 상위 수준에서 컴포넌트는 Vue의 컴파일러에 의해 동작이 추가된 사용자 지정 엘리먼트입니다. 경우에 따라 특별한 `is` 속성으로 확장 된 원시 HTML 엘리먼트로 나타날 수도 있습니다.

Vue 컴포넌트는 Vue 인스턴스이기도 합니다. 그러므로 모든 옵션 객체를 사용할 수 있습니다. (루트에만 사용하는 옵션은 제외) 그리고 같은 라이프사이클 훅을 사용할 수 있습니다.

- `Vue.component('컴포넌트 이름',{컴포넌트 속성})`
  - 컴포넌트 이름: `kebab-case(todo-list)` or `PascalCase(TodoList) `

### component 속성

- `template` 

  - ``` `: 백틱을 사용해서 입력
  - 최상단에는 단 하나의 태그만 존재 가능 (`<div></div>`등) 
  - 이후 `html`에서 `<component name> </component name>`으로 컴포넌트 사용가능

- `data `

  - 반드시 `함수`형태로 넣어야 한다.

  - 각자 고유한 내부 상태를 만들기 위해, 새로운 데이터 객체를 반환해야 한다.

  - ``` javascript
    data: function () {
      return {
        object: 0
      }
    }
    ```

- `methods`

  - 일반적인 view model과 동일하게 메소드 추가 후 사용 가능

#### Pass props and Emit events

![Props-events](https://kr.vuejs.org/images/props-events.png)

-  Vue.js에서 부모-자식 컴포넌트 관계는 **props는 아래로, events 위로** 라고 요약 할 수 있습니다. 부모는 **props**를 통해 자식에게 데이터를 전달하고 자식은 **events**를 통해 부모에게 메시지를 보냅니다. 어떻게 작동하는지 보겠습니다. 

- 개별 컴포넌트가 서로 다른 값을 표현하려면 props/events 지정 필요

- `props`

  ```javascript
  // 1. Array로 표현
  props: ['category']
  
  // 2. key-value로 자료형 표현
  props: {
  	category: String
  }
  
  // 3. Object로 옵션 추가 ( required, validator를 통한 조건 )
  props: {
  	category: {
  		type: String,  // category의 타입 지정
  		required: true,  // 필수지정 (blank=false)
  		validator: function(value) {  // validator!
              if (value.length !== 0) {
  				return true
              } else {
              	return false
              }
  		}
  	}
  }``
  ```

  1. `templates`와 같은 레벨에 ` props` 추가
  2.  `template: '<span>{{ 정의한 props }}</span>' `삽입
  3.  `<compoName message="안녕하세요!"></compoName>` 각 컴포넌트에서 지정


### Single File Component

- `<filename>.vue` 파일

## 01_todo_component.html













