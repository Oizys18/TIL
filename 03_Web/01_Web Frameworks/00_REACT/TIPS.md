# REACT TIPS

## Binding
- 현재 컴포넌트와 함수 바인딩 `this`
```javascript
// arrow function을 사용하거나 
const hello = () =>{
    console.log("use arrow function")
}

//Constructor에서 bind를 해주면 된다 
this.functionName = this.functionName.bind(this);
```