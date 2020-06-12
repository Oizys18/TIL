# Web TIPS 

## 에러핸들링 
```
There might be a problem with the project dependency tree.
It is likely not a bug in Create React App, but something you need to fix locally.

The react-scripts package provided by Create React App requires a dependency:

  "webpack": "3.10.0"

Don't try to install it manually: your package manager does it automatically.
However, a different version of webpack was detected higher up in the tree:
```
- react-start-app으로 생성한 프로젝트를 `yarn start` 하려고 했을 때 발생.
- webpack 버전의 문제지만, yarn이 함께 제시한 방법을 모두 사용해봐도 해결 불가했음
- `.env`를 root에 생성후 `SKIP_PREFLIGHT_CHECK=true`를 추가하면 해결된다. 


## 프론트 체크리스트 
- https://github.com/kesuskim/Front-End-Checklist
- 배포 전 확인해야할 좋은 내용들이 들어있다.
- 또한 google chrome lighthouse 기능도 좋음..!