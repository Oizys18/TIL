# DOM과 Layout

## DOM(Document Object Model) 문서 객체 모델

![img](https://camo.githubusercontent.com/92540c082d40d0df9de1fa079650221a303757ab/68747470733a2f2f7777772e6775727539392e636f6d2f696d616765732f4a6176615363726970742f6a617661736372697074385f312e706e67)

-  프로그래밍 언어가 웹 사이트의 내용, 구조 및 스타일을 조작 할 수있게 해주는 인터페이스입니다. JavaScript는 인터넷 브라우저에서 DOM에 연결하는 클라이언트 측 스크립팅 언어입니다.

- [XML](https://ko.wikipedia.org/wiki/XML)이나 [HTML](https://ko.wikipedia.org/wiki/HTML) 문서에 접근하기 위한 인터페이스

- 웹 문서는 텍스트 파일로 만들어져있어서, 브라우저가 이해할 수 있는 구조로 메모리에 올리려면 가공이 필요하다. 브라우저의 렌더링 엔진은 웹 문서를 로드한 후, 파싱하여 웹 문서를 브라우저가 이해할 수 있는 구조로 구성하여 메모리에 적재한다. 이렇게 모든 요소와 요소의 어트리뷰트, 텍스트를 각각의 객체로 만들고 이들 객체를 부자 관계를 표현할 수 있는 트리 구조로 구성한 것이 DOM이다.

- DOM은 자바스크립트를 통해 동적으로 변경할 수 있으며 변경된 DOM은 렌더링에 반영된다.

- DOM은 언어에 구속력이 없거나 특정 프로그래밍 언어와 독립적으로 작성되었지만이 리소스 전체에서 JavaScript의 HTML DOM 구현에 초점을 맞추고 참조합니다.

- HTML 문서의 기본은 태그다.

  Document Object Model(DOM)에 따르면 모든 HTML 태그는 객체다.

  한 태그에 둘려쌓여진 중첩된 태그를 "children"이라고 한다. 또한 태그 안에 있는 글자(text)도 객체이다.

  이 모든 객체들(태그)은 Javascript를 사용하여 접근이 가능하다.

```html
<!DOCTYPE html>
<html lang="en">

  <head>
    <title>Learning the DOM</title>
  </head>

  <body>
    <h1>Document Object Model</h1>
  </body>

</html>
// 이와 같은 html 소스 코드가 브라우저에서 구현되면 dom이 생성된다.
```

### Document object

- `document` 객체는 웹 사이트에 액세스하고 수정할 수있는 많은 **속성** 및 **메서드**가있는 내장 객체입니다.

- html source code와 다른점 ? : 
  - DOM은 클라이언트 측 JavaScript에 의해 수정됩니다.
  - 브라우저가 자동으로 소스 코드의 오류를 수정합니다.
- Dom에서 수정한 것은 소스코드에 반영되지 않는다. html소스는 변경되지 않으며, 즉 Client 측 JS의 영향을 받지 않는다.
-  DOM이 HTML 소스 코드와 다른 출력을 갖는 다른 인스턴스는 소스 코드에 오류가있는 경우입니다. 한 가지 일반적인 예는`table` 태그입니다.`tbody` 태그가`table` 내부에 필요하지만 개발자는 종종 HTML에 태그를 포함하지 않습니다. 브라우저는 자동으로 오류를 수정하고 `tbody`를 추가하여 DOM을 수정합니다. DOM은 닫히지 않은 태그도 수정합니다.

## 개념 요약

- 내가 작성한 HTML 코드가 DOM인가? `NO`
- 브라우저에서 `View Source` 한 것이 DOM인가? `NO`
  - 둘 다 소스코드다.
- DevTools 패널의 코드가 DOM인가? `Kinda Yes`
  - DOM의 시각적 표현이다.

- 자바스크립트는 DOM을 조작 할 수 있습니다.
  - 예를 들어 `getElementById`를 사용한다던가..
- 텍스트 노드의 특수  문자
  - 줄바꿈: `↵` (Javascript에선 `\n`)
  - 공백: `␣`
- `<head>` 이전의 공백과 줄바꿈은 무시된다.
- 만약 `</body>` 뒤에 무언가를 넣으면, HTML 스펙이 모든 내용들은 `<body>` 안에 있어야한다고 요구하기 때문에 결국엔 자동적으로 `<body>`안으로 이동하게 된다. 그래서 `</body>` 뒤엔 공백이 없을수도 있다.
- 태그는 엘리먼트 노드가되어 구조를 형성한다.
- 텍스트는 텍스트 노드가 된다.
- 기타등등, HTML에 있는 모든 것들은, 심지어 주석에 까지도 DOM에 존재한다.

### Ajax and Templating

- 여기서 너무 깊게 들어가지는 않겠지만, Ajax를 이용하여 다른곳의 컨텐츠를 페이지에 올린다면, DOM은 원래의 HTML과는 다르게 작동 할 것이라는걸 상상할 수 있을 것입니다. 일종의 데이터 로딩 및 [클라이언트측 템플릿](https://css-tricks.com/video-screencasts/127-basics-of-javascript-templating/) 사용과 동일합니다.

### JavaScript vs. the DOM

- JavaScript는 브라우저가 읽고 사용하는 언어입니다. 하지만 DOM은 그 일이 일어나는 곳입니다. 실제로 "JavaScript Thing"이라고 생각할 수있는 것은 "DOM API"입니다.

  예를 들어 요소에 `mouseenter` 이벤트를 감시하는 JavaScript를 작성할 수 있습니다. 그러나 "element"는 실제로 DOM node입니다. DOM node의 DOM 속성을 통해 해당 수신기를 연결합니다. 해당 이벤트가 발생하면 그 이벤트를 발생시키는 것은 DOM node입니다.

### **HTML안의 모든 것들은, 심지어 주석도, DOM의 일부가 된다.**

HTML의 맨 처음에있는 `` 지시자 조차도 DOM 노드다. DOM 트리에서 `` 은 `` 바로 앞에 존재한다. 우리는 그 노드를 건들지 않을 것이고, 그런 이유로 다이어그램에 그리지도 않을 것이지만 그 자리에 존재하고 있다.

전체 문서를 나타내는 `document` 객체는 공식적으로 DOM 노드이기도 하다.

[12개의 노드 유형](https://dom.spec.whatwg.org/#node)이 있다. 실제로 이 문서에서 그중 4개를 썼다.

1. `document` - DOM의 "시작 지점"
2. 엘리먼트 노드 - HTML 태그, 트리 구성 블록
3. 텍스트 노드 - 텍스트 포함
4. 주석 - 때로는 정보를 표시 할 수 있지만, 표시되지는 않는다. JS는 DOM을 통해 접근할 수 있다.