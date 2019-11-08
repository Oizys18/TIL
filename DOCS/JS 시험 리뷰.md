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

3. `typeof`로 모든 자료형 찍어보자 

```
- object
[] 
{} 


- number
1


- string
"hello" 

```

4. 조건/반복

5. 배열  : Array Helper Methods **중요** 
   - 모드 한 번 다 실행해보기 / 뭐 리턴하는지 해보기/ 오류나면 뭐가 나오는지? 어떻게 되는지?

```
.filter() -> return:array 어떻게 쓰는지 기억하기  
.forEach
.push()
.pop()
.join()
.map() -> return: ???
```

```
forEach
map
filter
find
every
some
reduce 
한번씩 다 뽑아보기 중요 중요
```

6. Object

```
key-value
```

7. `JSON`과 `JS Object` 구분

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

```
syntactic sugar 와 관련된 내용은 직접 정리하세요.return문이 한 줄
일 때, 인자가 없을 때, 인자가 하나일 때 등
```

11. DOM 

```
1. Event Listener 구분
2. DOM selector 
	2개 구분
```

12. Axios 

```
기본 활용법 복습  :::: 샘플코드 잘 보기
```

13. Ajax 객관식 나올 것 







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

