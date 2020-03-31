# CNN

## 참고

- https://www.youtube.com/watch?v=9fldE3-yJpg&list=PLQ28Nx3M4Jrguyuwg4xe9d9t2XE639e5C&index=34
- https://excelsior-cjh.tistory.com/152?category=940399
- https://untitledtblog.tistory.com/150
- https://thebook.io/006958/
- https://excelsior-cjh.tistory.com/79?category=1013831
- https://devkihyun.github.io/study/Machine-learining-and-Probability/



## 개요

- 이미지분류에서 가장 빈번히 사용됨
- Convolution layer, pooling layer, fully-connected layer로 구성 
- Convolution + pooling: feature extraction 특징 추출
- fully-connected: classification 분류

## CNN의 구조

- 일반적인 인공신경망은 fully-connected 연산과 ReLU와 같은 비선형 활성 함수 (nonlinear activation function)의 합성으로 정의된 계층을 여러 층 쌓은 구조이다.

- CNN은 합성곱 계층 (convolutional layer)과 풀링 계층 (pooling layer)이라고 하는 새로운 층을 fully-connected 계층 이전에 추가함으로써 원본 이미지에 필터링 기법을 적용한 뒤에 필터링된 이미에 대해 분류 연산이 수행되도록 구성된다.

- 합성곱 계층은 이미지에 필터링 기법이 적용하고, 풀링 계층은 이미지의 국소적인 부분들을 하나의 대표적인 스칼라 값으로 변환함으로써 이미지의 크기를 줄이는 등의 다양한 기능들을 수행한다.

## 합성곱 계층 Convolutional Layer

### 주요 특징

1. Convolution filter의 채널은 convolution layer의 채널 수와 같다. 
2. Output feature maps의 채널은 사용한 Convolution filter의 갯수와 같다.

- 이미지 데이터는 높이X너비X채널의 3차원 텐서 (tensor)로 표현될 수 있다. 만약, 이미지의 색상이 RGB 코드로 표현되었다면, 채널의 크기는 3이 되며 각각의 채널에는 R, G, B 값이 저장된다. (흑백일 경우 channel은 1, 만약 이미지가 아닐경우 channel이 큰 수일 수도 있다.)

- 하나의 합성곱 계층에는 입력되는 이미지의 채널 개수만큼 필터가 존재하며, 각 채널에 할당된 필터를 적용함으로써 합성곱 계층의 출력 이미지가 생성된다. 

- 이미지에 대해 필터를 적용할 때는 필터의 이동량을 의미하는 스트라이드 (stride)를 설정해야한다.  (주로 1로 설정)

- 합성곱을 수행하면, 출력 이미지의 크기는 입력 이미지의 크기보다 작아지게 된다. 그러므로 합성곱 계층을 거치면서 이미지의 크기는 점점 작아지게 되고, 이미지의 가장자리에 위치한 픽셀들의 정보는 점점 사라지게 된다. 이러한 문제점을 해결하기 위해 이용되는 것이 패딩 (padding)이다. 패딩은 입력 이미지의 가장자리에 특정 값으로 설정된 픽셀들을 추가함으로써 입력 이미지와 출력 이미지의 크기를 같거나 비슷하게 만드는 역할을 수행한다. 이미지의 가장자리에 0의 값을 갖는 픽셀을 추가하는 것을 zero-padding이라고 하며, CNN에서는 주로 이러한 zero-padding이 이용된다.

## 풀링 계층 (Pooling Layer)

- CNN에서 합성곱 계층과 ReLU와 같은 비선형 활성 함수를 거쳐서 생성된 이미지는 풀링 계층에 입력된다. 풀링 계층은 주로 max-pooling을 기반으로 구현된다. 

