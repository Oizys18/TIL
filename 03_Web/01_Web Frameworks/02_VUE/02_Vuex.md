# Vuex

https://vuex.vuejs.org/kr/

https://kdydesign.github.io/2019/05/09/vuex-tutorial/

## 정의

- 상태관리패턴 + 라이브러리

- State / View / Action 

### Vuex가 없는 기존 App의 문제점

- 단방향 데이터 흐름
  - View -> Action -> State -> View ....
  - 공통의 상태를 공유하는 여러 컴포넌트가 있는 경우 단순함이 빠르게 저하된다 === 성능저하
- 발생하는 문제
  1. 여러 뷰가 같은 상태에 의존함
     - 지나치게 중첩된 컴포넌트를 통과하는 prop은 장황할 수 있으며 형제 컴포넌트에서는 작동하지 않음. 
  2. 서로 다른 뷰의 작업이 동일한 상태를 반영해야 함
     - 직접 부모/자식 인스턴스를 참조하거나 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화 하려는 등의 해결 방법을 사용해야 함. (but 유지보수 불가능/불안정한 코드로 변경될 것)

### 해결법

- 컴포넌트에서 공유된 상태를 추출, 전역 싱글톤으로 관리해야 한다. 
  - 컴포넌트 트리가 하나의 큰 뷰가 되고 모든 컴포넌트는 트리에 상관없이 상태에 액세스/동작 트리거 가능
  - 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의, 분리함으로써 코드의 구조와 유지 관리 기능을 향상시킨다.

![Vuex 처리방식](https://vuex.vuejs.org/vuex.png)

## 용어 및 기본문법

### Store

- 모든 Vuex app의 중심에는 store가 있다. 

- app 상태를 보유하고 있는 컨테이너

- Vuex 저장소가 일반 전역 개체와 다른 점 두 가지

  1. vuex store는 반응형: 상태를 검색할 때 저장소의 상태가 변경되면 효율적으로 대응/업데이트

  2. 저장소의 상태를 직접 변경할 수 없다. 유일한 방법은 명시적인 커밋을 이용한 변이. 





## 시작하기(Vue CLI3)

1. `vue create project-name`
2. pick a preset > `Manually select features`
3. Check the features > `Babel`, `Router`, `Vuex`, `Linter`
4. Use history mode for router ? `Y`

