# 28_함수 성능과 빅 오(Big O) 표기법

- *Big O is **the worst-case scenario growth curve** for the complexity of an algorithm*
- 입력 시간에 따라 알고리즘이 실행되는 데 걸리는 시간을 수학적으로 표현한 것
- 알고리즘의 전체 단계를 대수로 바꾸고 문제의 전체 복잡성에 큰 영향을 미치지 않는 하위 상수 및 계수를 제외한다.

```
Regular       Big-O

2             O(1)   --> It's just a constant number
2n + 10       O(n)   --> n has the largest effect
5n^2          O(n^2) --> n^2 has the largest effect
```

## Constant Complexity (일정한 복잡성) : O(1)

```js
const firstElemEven = (array) => {
 return array[0] %2 === 0 ? true : false;
}
```

- **복잡성(항목 수)에 관계없이 시간(문자)이 일정**
- JavaScript 함수에 대한 최상의 시나리오
- ex) 배열조회, 해시테이블 삽입 

## Linear Complexity(선형 복잡성) : O(N)

```js
const hasValue = (array, value) => {
   for (var i = 0; i < array.length; i++){
       if (array[i] === value){
          return true;
       } 
    }
    return false;
}
```

- 성능이 입력 데이터 세트의 크기에 비례하여 선형적으로 증가하는 알고리즘
- 최악의 경우 시간(문자)은 항목 수와 함께 증가
- 크기가 증가함에 따라 시간 복잡성이 증가하고 동일한 속도로 증가
- ex) 배열의 요소 인쇄

## Logarithmic Complexity (로그 복잡성) : O(log N)

- search/sort 알고리즘의 기본이며, **대규모 수집을 처리할 때 가장 효율적인 접근방식**
- 실행 시간이 증가하지만 속도는 감소
- ex) [이진검색](https://en.wikipedia.org/wiki/Binary_search_tree)

## Quadratic - time : O(N^2)  2차시간

```js
const findMatch = (string) => {
   for (var i = 0; i < string.length; i++){
      for ( var j = i+1; j < string.length; j++){
         if (string[i] === string[j]) {
            return true;
         }
      }
   }
   return false;
}
```

- 로그 복잡도의 역수
- 함수의 실행 시간이 입력 크기의 제곱에 비례함
- 2차 복잡성으로 실행 시간이 증가하는 속도로 증가
- ex) 두 개의 중첩 된 for- 루프 내에서 상수 시간 연산, 두 정수 목록 비교, 버블 정렬 비교

## Exponential Time : **O(2^n)**  지수시간

```js
const fib = (num) => {
   if (num <= 1){
     return 1;
   }
   return fib(num - 1) + fib(num - 2);
}
```

- 작업을 수행하는 데 걸리는 단계 수는 n 제곱 (상수)에 대한 상수
- 크기 n의 입력이 주어지면 작업을 수행하는 데 걸리는 단계의 수는 n의 제곱 (상당히 큰 수)
- 일반적으로 그 정도를 모르고 가능한 모든 조합 또는 순열을 시도해야하는 상황

## 시간복잡도 및 성능표 

![1594078403516](https://github.com/Oizys18/TIL/blob/master/images/02_Language/big-o-graph.png?raw=true)

###  Big O 표기와 입력 데이터 크기에 따른 성능

| Big O 표기     | 10 개 일때 | 100 개 일때 | 1000 개 일때 |
| -------------- | ---------- | ----------- | ------------ |
| **O(1)**       | 1          | 1           | 1            |
| **O(log N)**   | 3          | 6           | 9            |
| **O(N)**       | 10         | 100         | 1000         |
| **O(N log N)** | 30         | 600         | 9000         |
| **O(N^2)**     | 100        | 10000       | 1000000      |
| **O(2^N)**     | 1024       | 1.26e+29    | 1.07e+301    |
| **O(N!)**      | 3628800    | 9.3e+157    | 4.02e+2567   |

### 자료 구조 작업별 복잡도

| 자료 구조          | 접근   | 검색   | 삽입   | 삭제   | 비고                          |
| ------------------ | ------ | ------ | ------ | ------ | ----------------------------- |
| **배열**           | 1      | n      | n      | n      |                               |
| **스택**           | n      | n      | 1      | 1      |                               |
| **큐**             | n      | n      | 1      | 1      |                               |
| **연결 리스트**    | n      | n      | 1      | 1      |                               |
| **해시 테이블**    | -      | n      | n      | n      | 완벽한 해시 함수의 경우 O(1)  |
| **이진 탐색 트리** | n      | n      | n      | n      | 균형 트리의 경우 O(log(n))    |
| **B-트리**         | log(n) | log(n) | log(n) | log(n) |                               |
| **Red-Black 트리** | log(n) | log(n) | log(n) | log(n) |                               |
| **AVL 트리**       | log(n) | log(n) | log(n) | log(n) |                               |
| **Bloom Filter**   | -      | 1      | 1      | -      | 거짓 양성이 탐색 중 발생 가능 |

### 정렬 알고리즘 복잡도

| 이름          | 최적     | 평균                         | 최악        | 메모리 | 동일값 순서유지 | 비고                                                         |
| ------------- | -------- | ---------------------------- | ----------- | ------ | --------------- | ------------------------------------------------------------ |
| **거품 정렬** | n        | n2                           | n2          | 1      | Yes             |                                                              |
| **삽입 정렬** | n        | n2                           | n2          | 1      | Yes             |                                                              |
| **선택 정렬** | n2       | n2                           | n2          | 1      | No              |                                                              |
| **힙 정렬**   | n log(n) | n log(n)                     | n log(n)    | 1      | No              |                                                              |
| **병합 정렬** | n log(n) | n log(n)                     | n log(n)    | n      | Yes             |                                                              |
| **퀵 정렬**   | n log(n) | n log(n)                     | n2          | log(n) | No              | 퀵 정렬은 보통 제자리(in-place)로 O(log(n)) 스택공간으로 수행됩니다. |
| **셸 정렬**   | n log(n) | 간격 순서에 영향을 받습니다. | n (log(n))2 | 1      | No              |                                                              |
| **계수 정렬** | n + r    | n + r                        | n + r       | n + r  | Yes             | r - 배열내 가장 큰 수                                        |
| **기수 정렬** | n * k    | n * k                        | n * k       | n + k  | Yes             | k - 키값의 최대 길이                                         |



## 참고

- [초보몽키](https://wayhome25.github.io/cs/2017/04/20/cs-26-bigO/)
- [stackoverflow](https://stackoverflow.com/questions/11514308/big-o-of-javascript-arrays)
- 