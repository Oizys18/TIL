# Scheduling 

- 함수가 즉시 실행되지 않고 특정 시간에 실행되도록 결정하는 것. ( == `scheduling a call`)

- 둘 다 콜백이기 때문에 지연시간 0ms를 줘도 다른 기본 함수보다 늦게 실행됨

  - 제로 타임 아웃 스케쥴링`setTimeout (func, 0)`(`setTimeout (func)`과 동일)은

     "가능한 한 빨리, 그러나 현재 코드가 완료된 후에"호출을 스케쥴하는데 사용된다.

- 함수를 `setInterval/setTimeout`에 넘기면 내부 참조가 함수 안에 생기고 garbage collection을 회피함! 

- CPU 자원 많이 먹는 수행을 `setTimeout`이용해서 분리시킬 수 있다.

- 모든 스케쥴링 방법은 정확한 지연을 보장하지 않는다. 브라우저 내부 타이머가 아래와 같은 이유로 느려질 수 있다.

  - CPU에 과부하가 있습니다.
  - 브라우저 탭이 백그라운드 모드에 있습니다.
  - 노트북이 배터리로 작동합니다.

## setTimeout

```js
let timerId = setTimeout(func|code, [delay], [arg1], [arg2], ...)
// func|code: 함수 또는 코드뭉치들을 실행합니다. 대게는 함수입니다. 역사적인 이유로 인해 일련의 코드를 전달할 수는 있지만 권장하지는 않습니다.

// delay: 동작하기 전 딜레이 시간입니다. 단위는 밀리세컨드(1000ms = 1 초), 디폴트는 0

// arg1, arg2…: 함수에 전달될 인자들 ( IE9 는 지원을 하지 않습니다. )
// 첫번째 인자로 문자열을 넘겨줘도 문자열로 함수를 만든다. (권장되지 않음)
// ex) setTimeout("alert('Hello')", 1000);
// 함수의 레퍼런스를 입력해야한다. 
setTimeout(sayHi(), 1000); // 잘못된 코드. sayHi함수가 아닌 sayHi()의 결과물을 인자로 넘겨주게 된다.
```

- 특정시간 간격 후에 한번 실행됩니다.
- 용도
  - CPU가 많이 사용되는 작업을 여러 조각으로 나누어 스크립트가 "정지"하지 않도록 하기.
  - 프로세스가 진행되는 동안 브라우저가 다른 작업을 수행하게 되도록 하기 (진행률 막대를 그립니다).

## setInterval

```javascript
let timerId = setInterval(func|code, [delay], [arg1], [arg2], ...)
```

- 모든 인자값들은 `setTimeout`과 같은 의미를 지니고 있습니다. 하지만 `setTimeout`과른 다르게 그것은 함수를 한번만 동작시키지 않습니다. 시간의 간격이 주어지면 규칙적으로 실행하게 됩니다.

- 특정시간 간격동안 주기적으로 실행됩니다.(**setInterval**은 코드가 정확한 간격으로 콜 스택에 전달될 것을 보장한다.)

### setInterval을 쓰면 안되는 이유

- 사용된 코드 블록에서 오류가 발생하면 실행을 중지하지 않고 잘못된 코드를 계속 실행한다.
- 한번 interval을 설정하면, clearInterval을 하거나 세션이 끝날 때까지 계속해서 프로세스로 존재한다.
- 본직적으로 JS는 single threaded기 때문에, 지정한 지연 시간보다 함수 실행이 오래 걸리는 경우 설정 시간과는 다르게 작동할 수 있으며, 잘못된 시간으로 반복 작동될 수 있다. **setInterval**은 코드가 정확한 간격으로 콜 스택에 전달될 것을 보장할 뿐, 실제 코드 실행 시간은 지정한 지연시간과 아무 관련이 없다.
- setTimeout으로 대체할 수 있다. (권장!)

## clearTimeout / clearInterval

- 실행 취소 할 수 있다.

```javascript
let timerId = setTimeout(...);
clearTimeout(timerId);

// repeat with the interval of 2 seconds
let timerId = setInterval(() => alert('tick'), 2000);
// after 5 seconds stop
setTimeout(() => { clearInterval(timerId); alert('stop'); }, 5000);
```

## 재귀적 `setTimeout`

```javascript
// setInterval
let timerId = setInterval(() => alert('tick'), 2000);

// recursive setTimeout
let timerId = setTimeout(function tick() {
  alert('tick');
  timerId = setTimeout(tick, 2000); 
}, 2000);
```

- 규칙적으로 뭔가를 실행하는 방법 
  - `setInterval` : 특정 함수를 실행한 순간부터 지정한 지연시간 이후 다시 실행
  - 재귀적 `setTimeout` : 특정 함수가 종료한 순간부터 지정한 지연시간 이후 다시 실행

- **재귀적인 `setTimeout` 은 실행 사이의 지연을 보장하지만, `setInterval`은 그렇지 못합니다.**

-  **`setInterval`로 특정 함수가 호출되는 실제 딜레이간격은 코드상에서 보는거보다 훨씬 덜하다.** 

  함수의 실행도 interval의 한 부분으로 시간이 소비되기 때문이다.

  이것은 함수의 실행이 우리가 기대하고 주어진 값보다 더 길어질수 있습니다.

- **재귀 setTimeout은 고정 지연 을 보장합니다.** 재귀 setTimeout을 사용하면 우리의 메서드가 완전히 실행될 때까지, 다른 실행이 발생하지 않는다.

## requestAnimationFrame

- JS WebAPI의 `window.requestAnimationFrame`, 비동기 함수
- **CSS**의 transition으로 처리하기 어려운 애니메이션이나, **HTML5**의 **Canvas**, **SVG** 등의 애니메이션 구현을 위해서 사용하는 함수 
- 모든 애니메이션을 직접 프레임 단위로 계산해야한다..
- 모니터 주사율과 맞춰서 실행 주기가 결정된다.

### 장점

- 브라우저가 애니메이션을 최적화 할 수 있으므로 애니메이션이 부드럽게 처리된다.
- 비활성 탭의 애니메이션이 중지되어 CPU가 차가워진다.
- 더욱 배터리 친화적이다.

### 차이점

- vs `setTimeout`? 
  - 브라우저가 실행 시기를 결정한다!

- vs `setInterval` ? 
  - 스스로 반복 호출하지 않는다! : 다음 함수 반복하려면 재귀적으로 호출해야한다.
  - `window.requestAnimationFrame`는 timestamp를 주기 때문에 활용하기 좋다.

### setTimeout` / `setInterval 대신 사용해야 하는 이유  

1. setTimeout이나 setInterval은 내부적으로 지연시간을 주지만, 사용자 시스템 자원의 변화로 인해 종종 원하는 시간에 실행되지 않아 애니메이션 프레임 간 일관성 없는 지연 시간 간격이 생긴다.

2. setTimeout이나 setInterval은 사용자 화면을 계속 변경하면 종종 사용자의 화면이 물리적으로 표현되기 전에 불필요한 리플로우를 수행해야 하는 브라우저가 멈춰 있을 때 "레이아웃 스레싱"을 유발하여 변경 사항을 표시합니다. 이것은 페이지 리플로우의 과도한 특징으로 특히 저성능의 모바일 페이지 로드 또는 베터리 소모가 발생하여 매우 좋지 않은 영향을 줍니다.

- `requestAnimationFrame`를 사용하면 다음번에 사용할 화면을 리페인트 시 코드를 실행할 수 있기 때문에 사용자의 브라우저와 동기화되지 않은 작업에 대한 추측과 화면을 변경하기 위한 하드웨어의 준비 상태가 사라집니다.
- `requestAnimationFrame`을 반복적으로 호출하여 애니메이션을 만들면 사용자의 컴퓨터가 매번 화면을 변경할 준비가 되었을 때 애니메이션 코드가 호출되어 더 부드럽고 효율적인 애니메이션을 만들 수 있습니다. 또한 `requestAnimationFrame`을 통해 호출되고 브라우저의 백그라운드 탭에서 실행되는 코드는 일시 중지되거나 사용자 시스템 리소스를 추가로 저장하기 위해 2프레임 이하로 느려지기 때문에 애니메이션을 실행하는 데 아무런 의미가 없습니다.

### requestAnimationFrame 이해 및 사용

```javascript
// requestAnimationFrame(callback)

// div를 원래 위치에서 5픽셀 이동시키는 함수 (재귀)
var adiv = document.getElementById('mydiv')
var leftpos = 0
function movediv(timestamp){
    leftpos += 5
    adiv.style.left = leftpos + 'px'
    requestAnimationFrame(movediv) // 재귀적 호출
}
requestAnimationFrame(movediv) 
```

- 콜백 함수에는 requestAnimationFrame()이 호출된 정확한 시간을 나타내는 타임 스탬프가 자동으로 전달됩니다.

- 취소 가능 

  - ```
    cancelAnimationFrame()
    ```

- 단, 시간을 사용자가 직접 정의할 수 없기 때문에 조건문을 통해 작동 조절해야한다.