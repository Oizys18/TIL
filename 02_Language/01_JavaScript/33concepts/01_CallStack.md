# 01_CallStack
- https://velog.io/@jakeseo_me/2019-03-15-2303-%EC%9E%91%EC%84%B1%EB%90%A8-rmjta5a3xh
- original source of this posting is from https://medium.com/@gaurav.pandvia/understanding-javascript-function-executions-tasks-event-loop-call-stack-more-part-1-5683dea1f5ec If the original author requests deletion, it will be deleted immediately.

- Translated by Jake Seo (서진규)

  - https://velog.io/@jakeseo_me
  - https://github.com/n00nietzsche

## 함수 실행에 대한 이해 
- 자바스크립트는 `하나의 스레드`로 단 `1개의 동시성`만 다루는 언어
    - 한 번에 1개의 작업만 다룰 수 있다. 
    - JS의 `Heap` `Queue` `Stack` -> 크롬의 `V8` 내부에 구현되어 있다.
### 1. 콜스택 CallStack
- 함수의 호출을 기록하는 자료구조
- 우리가 프로그램 안에서 위치한 곳 
- 함수 실행 시 스택에 `push` 된다. 
- 함수로부터 반환 받을 때, 스택에서 `pop` 된다.


### 2. 힙 Heap
- 오브젝트(객체)들은 힙 내부에 할당
- 거의 구조화되지 않은 영역(unstructured)의 메모리
- 변수와 객체들의 모든 메모리 할당이 여기서 일어남.
### 3. 큐 Queue

### 4. 이벤트 루프 Event Loop