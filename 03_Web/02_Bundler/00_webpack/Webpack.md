# Webpack

## 참고

- https://kdydesign.github.io/2017/11/04/webpack-tutorial/
- https://jusungpark.tistory.com/52 **추후 따라해보기!
- https://nesoy.github.io/articles/2019-02/Webpack
- https://ko.wikipedia.org/wiki/%EC%9B%B9%ED%8C%A9

## 개요

```
웹팩(Webpack 또는 webpack)은 오픈 소스 자바스크립트(JS) 모듈 번들러이다. 주로 자바스크립트(JS)를 위한 모듈 번들러이지만 호환 플러그인을 포함하는 경우 HTML, CSS, 심지어는 이미지와 같은 프론트엔드 자산들을 변환할 수 있다. 웹팩은 의존성이 있는 모듈을 취하여 해당 모듈을 대표하는 정적 자산들을 생성한다.

웹팩은 의존성을 취한 다음 의존성 그래프를 만듦으로써 웹 개발자들이 웹 애플리케이션 개발 목적을 위해 모듈 방식의 접근을 사용할 수 있게 도와준다. 명령 줄을 통해서 사용할 수 있으며, "webpack.config.js"이라는 이름의 구성 파일을 사용하여 구성할 수 있다. 이 파일을 사용하면 프로젝트를 위해 로더, 플러그인 등을 정의할 수 있다. (웹팩은 로더를 통해 상당한 확장이 가능하므로 개발자들이 파일을 함께 번들링할 때 수행하기 원하는 사용자 지정 작업을 작성할 수 있다.) createapp.dev라는 이름의 도구는 이 구성 파일의 생성 과정을 단순하게 만들어 준다.
- 위키피디아
```

`웹팩은 프로젝트의 구조를 분석하고 자바스크립트 모듈을 비롯한 관련 리소스들을 찾은 다음 이를 브라우저에서 이용할 수 있는 번들로 묶고 패킹하는 모듈 번들러(Module bundler)다.`

## 웹팩의 필요성 
- 웹의 자바스크립트 + 대규모 의존성 트리의 복잡성에 대응하기 위해 아래와 같은 방법이 고안됨
  - 한 프로그램으로 작동하는 하나의 파일을 여러 파일로 분할하고 구성할 수 있는 자바스크립트 모듈
  - 향후 자바스크립트에서 제공될 기능을 미리 이용할 수 있게 해주는 자바스크립트 전처리기(pre-processor)와 자바스크립트로 컴파일되는 언어 (ex. CoffeeScript, TypeScript)
- 위와 같은 방식을 사용하려면 파일을 브라우저가 이해할 수 있도록 번들로 묶고 변환(트랜스파일 및 컴파일)하는 이전에는 없던 추가 단계를 거쳐야하기 때문에 웹팩이 필요하다.


## 작동원리
```
웹팩은 프로젝트 전체를 한 단위로 분석한다. 즉, 지정한 메인 파일에서 시작해 자바스크립트의 require(webpack commonJS 모듈 지원)과 import(ES6)문을 참고해 프로젝트의 모든 의존성을 조사하고 로더를 이용해 처리한 후 번들로 묶은 자바스크립트 파일을 생성한다.
```