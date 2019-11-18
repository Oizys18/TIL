# JS 시험 리뷰 :: googledrive 

- Sample 코드 열심히 보기 

- 브라우저 조작용 

  - 브라우저의 객체는 **window**아래의 메소드/프로퍼티를 사용한다.

  - ```
    window 객체 
    	- window.open('URL') 등 
    ```
  
- node에서 윈도우와 같은 것 === `global`


1. `var`, `let`, `const`의 차이 

```
var는 function scoper라서 재선언 가능, 함수 안에서 해도 밖에서 호출 가능 
```

2. 할당과 값의 변경의 차이

```
const numbers = [1,2,3]
numbers.push(4)
console.log(numbers)

오류 안나고 [1,2,3,4] 출력됨 
값을 변경하는 건 재할당이 아님
numbers가 리스트라는 주소값을 저장하는 것 뿐
다른 Array로 바뀌는게 아닌이상, array의 값은 바꿔도 된다 

numbers = [1,2,3,4] >> 오류발생! 

```

`typeof`로 모든 자료형 찍어보자 : 

- 기본 자료형 (primitive)

```

Boolean (true/false) : boolean
null : object
undefined : undefined
number ( Infinity , 양수, 음수 등) : number
string : string
[] : object
{} : object
function : function
```

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

4. 조건/반복

```
if (userName.length >= 3){
    alert('이름이 3자 이상입니다.')
} else {
    alert('이름이 3자 이하입니다.')
}
```

```
1. for (변수 of container) { 실행 }

for (i of arr){
    console.log(i)
}

// lambda와 비슷, function을 인자로 넣기 (python의 map과 유사한 것 )
2. container.forEach(function() { 실행 })    

const arr = [1,2,3]
arr.forEach(function(ele){
	console.log(ele)
})

3. container.forEach(i => {실행})
const arr = [1,2,3]
arr.forEach(i => {
    console.log(i)
})

// C 스타일
4. for (let i = 1; i <= 10; i++) {실행}
```

5. 배열  : Array Helper Methods **중요** 

- 모드 한 번 다 실행해보기 / 뭐 리턴하는지 해보기/ 오류나면 뭐가 나오는지? 어떻게 되는지?

- `const arr = [1,2,3]`

  - filter

  ```javascript
  console.log(arr.filter(i => {
      if (i === 2){
          console.log(i)
      }
  }))
  >> 이 함수는 [] 리턴
  
  arr.filter(i => {
      if (i === 2){
          console.log(i)
      }
  })
  >> 이건 2 리턴
  ```

  - forEach

  ```
  arr.forEach(i => {
  	console.log(i)
  })
  >> 
  1
  2
  3
  ```

  - push

  ```
  console.log(arr.push(4)) >> 4
  console.log(arr) >> [ 1, 2, 3, 4]
  ```

  - pop

  ```
  console.log(arr.pop()) 
  >> 3
  console.log(arr)
  >> [1, 2]
  ```

  - join : type은 string

  ```
  console.log(arr.join()) 
  >> 1,2,3
  console.log(arr.join(''))
  >> 123
  console.log(arr.join(0))   // 값을 넣으면 빈곳을 넣은 값으로 채워서 리턴 
  >> 10203
  ```

  - map

  ![image-20191111005757181](C:\Users\Delta\AppData\Roaming\Typora\typora-user-images\image-20191111005757181.png)

  ```
  console.log(arr.map(function (i, idx, arr) {
      console.log(i, idx)
  }))
  >> 이 함수 자체는 undefined를 출력, 안의 console.log는 아래와 같이 (값, 인덱스 현재 arr)출력 
  1 0 [ 1, 2, 3 ]
  2 1 [ 1, 2, 3 ]
  3 2 [ 1, 2, 3 ]
  [ undefined, undefined, undefined ]
  ```

  - includes

  ```
  python의 a in b 와 동일 
  arr.includes(값)을 하면 true/false의 boolean값 리턴 
  ```

  - indexof

  ```
  index와 동일 
  console.log(arr.indexOf(3)) 
  >> 2 
  넣은 값의 인덱스 위치 알려준다 
  ```

  - find

  ```
  // filter와 비슷하지만 단 하나의 요소만 리턴한다.
  console.log(arr.find(function (n){
      return n % 2 !== 0
  }))
  >> 1 
  (3도 해당되지만, 콜백함수인 function은 리턴이 true인 요소를 찾을 때 까지만 순회하다가 찾으면 거기서 끝난다. 요소 전체의 갯수인 3만큼 호출되지 않고 1번 호출되고 1을 찾은 후 바로 끝남)
  ```

  - every

  ```
  some과 유사하지만 반대의 기능 
  배열의 모든 요소가 특정 조건을 만족하는지 체크할 때 사용
  
  console.log(arr.every(function(i,idx,arr){
  	return i < 3
  }))
  
  >> false : 3이 있기 때문에 false리턴 
  ```

  - some

  ```
  배열의 어떤 요소가 특정 조건을 만족하는가??
  console.log(arr.some(function(i,idx,arr){
  	return i < 3
  }))
  
  >> true 
  ```

  

  - reduce 

    ```
    https://bblog.tistory.com/300
    띠용한 함수다
    ```

6. Object

```
key-value로 이루어진 데이터구조
```

7. `JSON`과 `JS Object` 구분

```
Object: Javascript Engin 메모리 안의 데이터구조
JSON: Javascript Object Notation, 객체의 내용을 기술하기 위한 Text 파일
```

8. js object

```
const students = {john:'hi', ashely:'hey'}
const school = {
	students,
}

요렇게 됨 

>> school = {
	students:{
		john:'hi',
		ashely:'hey'
	}
}

오브젝트 value에 함수 할당도 가능 
```

9. method

```
메서드 정의 시 arrow function 사용 X 
```

10. 함수

 https://www.zerocho.com/category/JavaScript/post/5816c858ca15d50015d924ae 

```
syntactic sugar 와 관련된 내용은 직접 정리하세요.
return문이 한 줄
일 때, 인자가 없을 때, 인자가 하나일 때 등
```

11. DOM 

    - querySelector 와 querySelectorAll()의 차이

    ```
    querySelector()는 인자인 'selectors'에 해당하는 HTML element 중 첫번째 오브젝트 하나를 리턴하고,  querySelectorAll()는 'selectors'에 해당하는 모든 오브젝트를 array로 리턴한다.
    ```

```
1. Event Listener 구분
click – 마우스버튼을 클릭하고 버튼에서 손가락을 떼면 발생한다.
mouseover – 마우스를 HTML요소 위에 올리면 발생한다.
mouseout – 마우스가 HTML요소 밖으로 벗어날 때 발생한다.
mousemove – 마우스가 움직일때마다 발생한다. 마우스커서의 현재 위치를 계속 기
록하는 것에 사용할 수 있다.
keypress – 키를 누르는 순간에 발생하고 키를 누르고 있는 동안 계속해서 발생한다.
keydown – 키를 누를 때 발생한다.
keyup – 키를 눌렀다가 떼는 순간에 발생한다.
load – 웹페이지에서 사용할 모든 파일의 다운로드가 완료되었을때 발생한다.
scroll – 스크롤바를 드래그하거나 키보드(up, down)를 사용하거나 마우스 휠을 사용
해서 웹페이지를 스크롤할 때 발생한다. 페이지에 스크롤바가 없다면 이벤트는 발생하
지 않다.
change – 폼 필드의 상태가 변경되었을 때 발생한다. 라디오 버튼을 클릭하거나 셀렉
트 박스에서 값을 선택하는 경우를 예로 들수 있다.
input - input 또는 textarea 요소의 값이 변경되었을 때
submit - form을 submit 할 때
```

12. Axios 

 💡 axios는 브라우저에서 XHRXMLHttpRequest)를 보내주고 

그 결과를 promise 객체로 반환해주는 라이브러리이다.  

```javascript
//기본 활용법 복습  :::: 샘플코드 잘 보기
catBtn.addEventListener('click', e => {
    const URL = "https://api.thecatapi.com/v1/images/search"
    // imgs.innerHTML = null
    axios.get(URL)
        .then(result => {
            let imgURL = result.data[0].url
            const elem = document.createElement('img')
            elem.src = imgURL
            imgs.appendChild(elem)
            elem.style.height='300px'
            elem.style.width='300px'
            elem.className = 'rounded flex img-thumbnail'
        })
})
```

axios는 비동기!!! 

![image-20191111012524002](C:\Users\Delta\AppData\Roaming\Typora\typora-user-images\image-20191111012524002.png)



13. Ajax 객관식 

![image-20191111012630837](C:\Users\Delta\AppData\Roaming\Typora\typora-user-images\image-20191111012630837.png)

![image-20191111012641259](C:\Users\Delta\AppData\Roaming\Typora\typora-user-images\image-20191111012641259.png)



## Django

- `좋아요` 붙였던 코드 읽기

```python
@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 만약 좋아요 리스트에 현재 접속중인 유저가 있다면
    # -> 해당 유저는 좋아요를 했다.
    user = request.user

    # article_pk 로 넘어온 글의 like_users에 현재 접속중인 유저를 추가한다.
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True


    context = {
        'liked': liked,
        'count': article.like_users.count(),
        }
    return JsonResponse(context)
```

```
<script>
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
</script>
```

- GET -> POST로 바꾸기

```javascript
detail에서 
axios.get() 을 axios.post()로 바꾼후, csrf를 보내줘야함

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.post(`/articles/${articleId}/like/`){}
```

