# HTML/CSS

## HTML
ㅊ
### Bootstrap feedback

```css
1. Semantic한 코드를 작성하기 위해 Tag를 최대한 활용하자 
- Label 등 
2. 한 문서에 동일한 id 2개 이상 만들기 금지 
3. Padding과 Margin의 차이 
4. card에 이미지를 넣을 때, 좌우 상단이 카드 크기를 넘어서면 자동으로 rounded 적용

.card-img-top {
  width: 100%;
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}
```

### viewport

```html
현재 사용자가 보고있는 화면의 크기 : 스마트폰 때문에 화면 크기가 다양해짐 
<meta name="viewport" content="width=device-width, initial-scale=1.0">
: initial-scale에서 content(device-width)로 조정될 것이라는 뜻
```

### Flex

- https://flexboxfroggy.com/#ko
- https://developer.mozilla.org/ko/docs/Web/CSS/flex

```css
- 요소를 직접 align하지 않고, 요소가 포함된 FlexBox를 이동시킬 수 있음
- 가로축 row와 세로축 column을 기준으로 작동 (z축 없다)
- axis 설정 안하면 기본값은 row
```

- `flex-direction:`

```css
: row;
: column;
: row-reverse;
: column-reverse;

# reverse 시 start/end도 뒤바뀜
```

- `justify-content:`

```css
- row 기준 수정 시 입력
- 초기 설정 없이도 bootstrap은 row : class사용, flex를 통해 정렬하고 있었다. 
: center; # 중앙정렬
: left; # row 설정시 좌측 정렬 
: right; # row 설정시 우측 정렬
: flex-end; # 설정한 flex-direction의 end로 보냄 
: flex-start; # 설정한 flex-direction의 start로 보냄 (기본 설정값)
: space-between; #contents를 끝까지 펼치고 content간의 여백을 균등하게 분배한다. 
: space-around; #contents를 포함, 전체 여백까지 포함해 여백을 균등 분배 
```

- `align-items:`

```css
: center; # 기준 축이 column일 때, 세로 중앙 정렬됨

cf) flex-wrap 상태에서 contents overflow 시 space-around로 자동 설정 (x,y 축 모두)
```

- `flex-wrap:`

```css
CSS flex-wrap property는 flex-item 요소들이 강제로 한줄에 배치되게 할 것인지, 또는 가능한 영역 내에서 벗어나지 않고 여러행으로 나누어 표현 할 것인지 결정하는 속성입니다.

:nowrap; # default
:wrap; # 영역(container 등)을 넘지 않고 여러행으로 나누어 표현 
:wrap-reverse; # 배열 시 content를 거꾸로 
```

- `order:`

```css
개별 item의 위치를 조정가능 
cf) index는 0부터 시작, 위치는 기존 위치 기준
 
.red{
  order:-3;
}
```

- `align-self:`

```css
개별 요소에 적용할 수 있는 속성
align-items가 사용하는 값들을 인자로 받으며, 값들은 지정한 요소에만 적용됨

.some_item{
  align-self:flex-end;
}
```

- `flex-flow:`

```css
flex-direction과 flex-wrap이 자주 같이 사용되기 때문에, flex-flow가 이를 대신할 수 있습니다. 이 속성은 공백문자를 이용하여 두 속성의 값들을 인자로 받습니다.

예를 들어, 요소들을 가로선 상의 여러줄에 걸쳐 정렬하기 위해 flex-flow: row wrap을 사용할 수 있습니다.

#pond {
  display: flex;
flex-flow:column wrap;
}
```

- align-content:

```css
개구리들이 연못의 사방에 퍼져있고, 수련잎은 연못의 위쪽에 모여있습니다. align-content를 사용하여 여러 줄 사이의 간격을 지정할 수 있습니다. 이 속성은 다음의 값들을 인자로 받습니다:

flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.
이 속성을 사용하는 방법이 어려울 수 있습니다. align-content는 여러 줄들 사이의 간격을 지정하며, align-items는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정합니다. 한 줄만 있는 경우, align-content는 효과를 보이지 않습니다.
```

### media 

```html
  <style>
    h1{
      color:darksalmon
    }
    @media (max-width: 1024px){
      h1 {
        color:salmon;
      }
    }
  </style>


# media(x) : x가 True일 경우
```

- Bootstrap4 + flex

```css
/*Vertical Align : flex를 사용해 align-items: center가 편하다.*/

display: flex;
  align-items: center;

/*Horizontal Align : flex를 사용해서,class에 입력 */
justify-content-center
```

## CSS

### CSS 명시도
-- https://iamdaeyun.tistory.com/entry/Lesson-7-CSS-%EC%82%AC%EC%9A%A9%EC%8B%9C-%EB%B0%98%EB%93%9C%EC%8B%9C-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0%EA%B2%83-%EB%AA%85%EC%8B%9C%EB%8F%84
 
#### Cascading 우선순위
- Inline Style > !importnat > id > class > tag 
- 쉼표로 구분된 4개의 숫자로 표현가능 
  - Inline, Id, Class, Tag(element)  : 0,0,0,0  
  ```
  div ul li : 요소가 3개이므로 0,0,0,3
  div.abcDEF ul li : 클래스 1개와 요소3개. 0,0,1,3
  a:hover : 가상클래스 1개, 요소1개. 0,0,1,1
  div.navb a:hover : 클래스 1개, 가상클래스 1개, 요소 2개. 0,0,2,2
  #navbar em : id 1개, 요소 1개. 0,1,0,1
  h2#navi em : id 1개, 요소 2개. 0,1,0,2
  ```
- 명시도 레벨이 높으면 우선순위가 높다.
- Override : 문서 구조는 평가되지 않는다. 같은 우선도를 지닌 스타일이 중복되면 가장 나중에 선언된 것이 적용된다.
- Inline style : 인라인 선언이 우선적용된다.

### CSS 7단위

```
출처: https://webclub.tistory.com/356

- font 단위 
1. rem(root em)
1-2. em :현재의 font-size를 정의
em과 rem과 다른 점은 이 두 단위가 font-family에 의존한다

- viewport 단위 
2&3. vh & vw
4&5. vmin & vmax
    VW(Viewport Width) : 뷰포트 너비의 1% 길이와 동일합니다.
    VH(Viewport Height) : 뷰포트 높이의 1% 길이와 동일합니다.
    VMIN(Viewport Minimum) : 뷰포트 너비 또는 높이를 기준으로 하는 최소 값입니다.
    VMAX(Viewport Maximum) : 뷰포트 너비 또는 높이를 기준으로 하는 최대 값입니다.

6&7. ex & ch 
	현재 폰트와 폰트 사이즈에 의존한다는 점에서 em 그리고 rem과 비슷합니다.
	em과 rem과 다른 점은 이 두 단위가 font-family에 의존한다면 다른 두 단위는 폰트의 특정 수치에 
	기반한다는 점입니다. 
    - ch 단위, 또는 글꼴 단위는 제로 문자인 0의 너비값의 "고급 척도"로 정의됩니다. 
    - ex 단위의 정의는 "현재 폰트의 x-높이값 또는 em의 절반 값"이라고 할 수 있습니다. 
      x-높이값은 소문자 x의 높이값이기도 합니다. 
```

