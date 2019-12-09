# Web 상식

## Browser storage

`Application - storage`

- `session storage `
  - 브라우저가 켜진 상태까지만 지속되는 저장소
  - ex) 로그인 정보, 
- `local storage`
  - 브라우저가 닫혀도 지속되는 저장소

## LocalStorage API (Web api)

- https://developer.mozilla.org/ko/docs/Web/API/Window/localStorage

- localStorage는 string으로 저장하기 때문에 데이터 처리를 해야 합니다.
  - 저장할 때 : JSON.stringify 
  - 읽을 때 : JSON.parse

```js
// Create
localStorage.setItem('key','value')

// Read
localStorage.getItem('key')

// Update
localStorage.setItem('existingKey','newValue')

// Delete
localStorage.removeItem('key')

// Count
localStorage.length
```

## Declarative Programming 

- 선언형 프로그래밍(== Descriptive Programming)

- 내가 만드려는 것을 묘사하면 자동으로 만들어주는 것

  - `Reactive Programming ` : 데이터 변화에 반응 (자동 적용/반영)
  - `Responsive Programming` : device 화면크기에 반응