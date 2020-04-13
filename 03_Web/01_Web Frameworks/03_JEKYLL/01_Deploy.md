# Github page deploying

- 기본적으로 Jekyll은 Github page와 연동이 되기 때문에 쉽게 업로드가 가능하다.

## 준비

### Github 저장소 생성

- 저장소명은 필수적으로 `USERNAME.github.io`로 생성해야한다. 
- 이후 저장소명이 그대로 URL이 된다. 
  - ex) repo name: oizys18.github.io  ->  URL: https://oizys18.github.io

```
프로젝트 별 페이지 만들기

프로젝트 별로 페이지를 만들 수도 있습니다. 이 때는 프로젝트 이름이 yourname.github.io가 아니어도 상관 없으며 이미 존재하는 프로젝트에 페이지를 만들 수도 있습니다. 다만 이렇게 만든 페이지는 yourname.github.io/projectname의 url로 접속하게 됩니다.

참고 [https://dreamgonfly.github.io/2018/01/27/jekyll-remote-theme.html]
```

### Jekyll Add & Commit & Push

- 이전에 생성한 Jekyll 폴더 내용을 모두 방금 생성한 저장소로 `git push` 한다.

## 결과

- 생성된 URL 주소로 접속하면 초기 Jekyll 세팅 그대로 작성된 것을 확인할 수 있다. 

- 새로운 `post`를 작성하려면 로컬 저장소의 `_posts`에 markdown 형식으로 작성하면 된다.

