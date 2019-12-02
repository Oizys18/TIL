# Youtube-Searcher

- `Vue` project에서 `console.log` 사용하려면 

  - `package.json` - `eslintConfig`에서 예외처리가 필요하다.

  ```json
  "eslintConfig": {
      "root": true,
      "env": {
        "node": true
      },
      "extends": [
        "plugin:vue/essential",
        "eslint:recommended"
      ],
      "rules": {
        "no_console": "off"
      },
      "parserOptions": {
        "parser": "babel-eslint"
      }
    },
  ```

# `$emit` : 데이터 전송 및 처리

- 부모-자식 간 데이터 일치화를 시키지 않으면, 컴포넌트가 다중화되고 복잡해질 때 문제가 발생할 수 있다.

## `App.vue`

- `template`

```html
<template>
  <div>
     <h1>Youtube Searcher</h1>
     <SearchBar @inputChange = 'onInputChange'/>  // 해당 자식 컴포넌트에게 발생한 이벤트 처리
  </div>
</template>
```

- `script`

```javascript
export default {
  ...
  methods: {
    onInputChange (inputValue) {  // InputChange 관련 메소드 정의
      console.log(inputValue)
    }
  }
}
```



## `components/SearchBar.vue`

- `script`

```javascript
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      console.log(event.target.value)
      this.$emit() // $emit 메소드:
    }		       // 자식 컴포넌트가 부모 컴포넌트로 data 전송
  }				   // $emit('event', data)
}
```



# Youtube-Data API

- request 보낼 주소 : ` https://www.googleapis.com/youtube/v3/search ` 
- ` https://www.googleapis.com/youtube/v3/search?key=API_KEY 