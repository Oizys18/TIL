# 11_JS engines

## Virtual Machine 가상 머신

- 가상머신: 주어진 컴퓨터 시스템의 가상 머신 또는 소프트웨어 구동 에뮬레이션 유형 
  - Mac의 Parallels 
- 프로세스 가상머신: 덜 기능적, 하나의 프로그램이나 프로세스만 실행할 수 있다. 
  - Windows의 Wine
- JS엔진은 JS 코드를 해석하고 실행하도록 특별히 설계된 프로세스 가상 머신의 일종이다.
- 웹 페이지를 구성하여 브라우저의 성능을 향상시키는 *레이아웃 엔진*과 코드를 해석하고 실행하는* 낮은 수준의 Javascript 엔진*을 구별하는 것이 중요하다.

## JS 엔진이란? 

- 자바스크립트 코드를 마이크로프로세서가 이해할 수 있는 낮은 레벨 또는 기계 코드로 변환하는 프로그램입니다.
- 각 Javascript 엔진은 ECMAScript(스크립팅 언어 표준) 버전을 구현한다.
  - Rhino
  - JavaScriptCore
  - SpiderMonkey
- Javascript 엔진의 기본 작업은 개발자가 작성한 Javascript 코드를 빠르게 변환하고, 애플리케이션에 내장화 하거나 브라우저가 해석 가능하도록 최적화 하는 것이다.

## JS엔진의 동작

- WebKit의 **JavascriptCore**와 Google의 **V8** 엔진이 주요 엔진이다. NativeScript가 이것들을 활용하기 때문이다. 이 두 엔진은 코드 처리를 다르게 처리한다.

  **JavaScriptCore**는 스크립트를 해석하고 최적화하는 일련의 단계를 수행한다. 어휘 분석을 수행하여 소스를 일련의 토큰 또는 식별 된 의미의 문자열로 나눕니다. 그런 다음 구문 분석기에서 토큰을 분석하고 구문 트리로 작성한다. 4 개의 JIT (just-in-time) 프로세스가 파서에 의해 생성 된 바이트 코드를 분석, 실행한다. 간단히 말해서, JavaScriptCore는 소스 코드를 가져 와서 문자열로 분해한다. (별명은 렉스).이 문자열은 컴파일러가 이해할 수있는 바이트 코드로 변환 한 다음 실행한다. (Rhino, SpiderMonkey도 이와 같이 작동한다.)

- V8은 중간에 바이트 코드를 생성하고 그것을 다시 기계코드로 변환한다.

## Chrome V8엔진

- C++, 오픈소스, Chrome(클라이언트) 및 Nodejs(서버) 모두에 사용된다.

- ECMA-262에 지정된 대로 ECMAScript를 구현합니다.

- V8은 JS 실행 성능(속도)을 높이기 위해 인터프리터 대신 JavaScript 코드로 보다 효율적인 기계 코드로 변환합니다. 

- **V8 엔진은 독립 실행형으로 실행할 수 있으며, C++ 프로그램을 통해 내장할 수 있습니다.**

  ![img](https://camo.githubusercontent.com/a2436c7072425bb1b1bd02b883b124168866019e/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a504133515a5f374557676f44474e794a49445f374d412e706e67)

- C++는 하드 드라이브의 파일 및 폴더를 처리하는 것과 같이 하드웨어에 훨씬 가깝기 때문에 JavaScript에 비해 프로그래밍 언어로서의 기능이 더 많기 때문에 강력한 기능입니다. 코드를 C++로 작성하고 JavaScript에서 사용할 수 있도록 함으로써 JavaScript에 더 많은 기능을 추가할 수 있습니다. Node.js 자체는 서버측 프로그래밍 및 네트워킹 애플리케이션을 지원하는 V8 엔진의 C++ 구현입니다.

###  V8의 bytecode 형식

![https://cdn-images-1.medium.com/max/1600/1*ZIH_wjqDfZn6NRKsDi9mvA.png](https://camo.githubusercontent.com/36473487fa613a134665bb0a7fe13a979ec527ed/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a5a49485f776a7144665a6e364e524b734469396d76412e706e67)

- V8이 자바스크립트 코드를 컴파일 할때, parser는 추상적인 문법 트리를 생성합니다. 이 문법트리는 자바스크립트의 문법구조의 트리를 나타냅니다. Ignition(the interpreter) 해석기 는 이 문법 트리로부터 바이트 코드를 생성합니다. TurboFan (the optimizing compiler)컴파일러는 결국 이 바이트 코드를 갖게되고 optimized된 머신코드를 이거로부터 생성하게 됩니다.

- **Bytecode는 머신 코드의 추상화입니다.** 만약 바이트 코드가 물리적 CPU와 같은 계산적인 모델과 같게 디자인되었다면 바이트 코드를 머신 코드로 컴파일링 하는 것은 쉽습니다. 그래서 인터프리터가 종종 레지스터이거나 스택 머신인 이유입니다. **Ignition은 누산기 레지스터를 지닌 레지스터 머신입니다.(데이터를 기억시키기 전에 보관하는 레지스터 또는 기억 장소에서 호출되어 보관되는 레지스터.)**

![https://cdn-images-1.medium.com/max/1600/1*aal_1sevnb-4UaX8AvUQCg.png](https://camo.githubusercontent.com/e3b64ea6c4b19902cda42f6196d18532049027c5/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a61616c5f317365766e622d34556158384176555143672e706e67)

### 숨겨진 클래스

- JS는 프로토타입 기반 언어 : 복제 프로세스를 사용하여 클래스와 객체가 생성되지 않습니다.
- JavaScript는 또한 동적으로 유형이 지정됩니다. 유형 및 유형 정보는 명시 적이지 않으며 속성은 즉석에서 객체에 추가 및 삭제할 수 있습니다.

![img](https://github.com/Lee-hyuna/33-js-concepts-kr/wiki/resource/scarlett/11/hiddenclass.png)

- 객체 속성을 저장하기 위해 사전과 같은 데이터 구조를 사용하고 (대부분의 자바 스크립트 엔진과 마찬가지로) 속성 위치를 확인하기 위해 동적 룩업을 수행하는 대신 V8은 런타임에 숨겨진 클래스를 생성하여 유형 시스템의 내부 표현을 가짐으로써 속성 액세스 시간을 향상시킬 수 있습니다. 
- (레이아웃이 동일하다면, p와 q는 V8에 의해 생성 된 것과 동일한 숨겨진 클래스에 속한다. 이는 숨겨진 클래스를 사용하는 또 다른 이점을 강조합니다. V8에서는 속성이 동일한 객체를 그룹화 할 수 있습니다.)
- 생성된 객체에 새로운 프로퍼티를 추가한다면 새로운 숨겨진 클래스를 만든다. 따라서 숨겨진 클래스 작성을 최소한으로 유지하기 위해 객체를 생성한 후 속성을 추가하지 말고 같은 순서로 객체 멤버를 항상 초기화 해야한다.

![image-20200617095545832](https://i.imgur.com/7ZOVfso.png)