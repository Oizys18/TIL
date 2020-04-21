# Vue tips & problem solving 
## 공부습관
- 빈번사용 Component들 라이브러리 사용없이 직접 만들어서 사용하기
- webpack 직접 생성하기


## Web title 변경 
- https://stackoverflow.com/questions/54951082/vue-cli-title-option-for-htmlwebpackplugin-does-not-work
- https://cli.vuejs.org/guide/webpack.html#modifying-options-of-a-plugin

### 문제
- VueCLI3 프로젝트 중 상단 타이틀을 변경하고자 `public/index.html`을 확인했으나, title이 `<title><%= htmlWebpackPlugin.options.title %></title>`로 설정된 것을 확인. Html Webpack 과 관련된 것으로 확인하고 하드코딩하지 않고 타이틀을 변경하고자 함.

### 해결
- root에 `vue.config.js` 파일을 신규생성 
```javascript
module.exports = {
    chainWebpack: config => {
      config
      .plugin('html')
      .tap(args => {
        args[0].title = 'NEW TITLE'
        return args
      })
    }
  }
```
- 웹팩의 플러그인 설정을 수정하는 방식이다. 공식문서에서 확인할 수 있듯이 새로운 로더를 추가하거나 간단한 설정을 수정할 수도 있다.
- `vue inspect --rules`, `vue inspect --plugins` 명령어를 통해 규칙과 플러그인을 모두 출력해볼 수 있다.


