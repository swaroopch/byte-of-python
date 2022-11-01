# 예외 처리

예외 (Exception) 란 말 그대로 프로그램에서 벌어지는 _예외적인_ 상황을 뜻합니다. 예를 들자면 여러분이 파일을 읽고자 할 때 그 파일이 존재하지 않는 경우라던지, 또는 프로그램이 한참 실행중인데 그 파일을 갑자기 지워버렸다던지 하는 경우 등입니다. 이러한 상황을 ***예외 (Exception)** 를 활용하여 처리할 수 있습니다.

비슷하게 여러분의 프로그램에 부적절한 명령문이 있을 경우 어떻게 될까요? 이런 경우 파이썬은 프로그램에 오류 (**error**) 가 있음을 제기 (**raise**) 해 줍니다.

## 오류 (Error)

간단한 `print` 함수를 호출하는 상황을 생각해 봅시다. 이 때 `print` 를 `Print` 라고 잘못 입력했을 경우 어떻게 될까요 (대/소문자 구분에 유의해 주세요)? 이 경우, 파이썬은 구문 오류를 _발생_ (_raise_) 시킵니다.

```python
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
```

위와 같이 `NameError` 가 발생되었고 오류가 발생한 위치가 표시됩니다. 이렇게 오류를 처리해 주는 부분을 **오류 핸들러** 라 합니다.

## 예외 (Exception)

이번에는 사용자로부터 뭔가를 입력 받는 것을 시도하는 (**try**) 경우를 생각해 봅시다. 아래 예제에서의 첫 줄을 입력하고 `Enter` 를 누릅니다. 여러분의 컴퓨터가 입력을 받기 위해 대기중일 때, 어떠한 것을 입력하는 대신 `[ctrl-d]` (Mac OS) 또는 `[ctrl-z]` (Windows) 를 누르고 어떻게 되는지 살펴봅시다 (만약 여러분이 Windows를 사용중인데 둘 다 안 되는 경우 `[ctrl-c]`를 대신 눌러 보세요. 다만 이 경우 아래와 달리 `KeyboardInterrupt` 오류가 표시될 것입니다).

```python
>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

그러면 파이썬은 `EOFError` 라는 오류를 발생시키는데, 이때 EOF란 파일의 끝 (*end of file*) 을 의미하며 (파일의 끝은 `ctrl-d` 에 의해 표현됩니다), 파이썬이 갑자기 파일의 끝이 올 것을 예상하지 못했기 때문에 위와 같은 오류가 발생하는 것입니다.

## 예외 처리

예외는 `try..except` 문을 통해 처리할 수 있습니다. 이것은 try 블록 안에 명령을 입력하고, 발생할 수 있는 각 예외 상황을 처리해줄 수 있는 _오류 핸들러_ 를 except 블록에 입력해 주면 됩니다.

예제 (`exceptions_handle.py` 로 저장하세요):

<pre><code class="lang-python">{% include "./programs/exceptions_handle.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/exceptions_handle.txt" %}</code></pre>

**동작 원리**

이 예제에서는 예외가 발생할 수 있는 명령문들을 `try` 블록에 넣어 주었으며 오류 또는 예외를 적절하게 처리해 줄 오류 핸들러를 `except` 절 (또는 블록) 에 넣어 주었습니다. `except` 절에서는 지정된 한 개의 오류 혹은 예외를 처리할 수도 있고, 괄호로 묶여진 모든 오류나 예외들의 목록을 처리해 줄 수도 있습니다. 만일 오류나 예외를 특별히 지정하지 않은 경우에는 _모든_ 오류 및 예외를 처리하게 됩니다.

이 때 모든 `try` 절에는 적어도 한 개의 `except` 절이 있어야 합니다. 아니면 try 블록을 사용할 아무런 이유가 없겠지요?

만약 어떤 오류나 예외든지 이처럼 처리되지 않는 경우, 기본 파이썬 오류 핸들러가 호출되는데 그러면 이에 의해 프로그램의 수행이 중단되며 해당하는 오류 메시지가 출력됩니다. 위 예제에서는 기본적인 파이썬 오류 핸들러가 어떻게 동작하는지 확인해 보았습니다.

또한 `try..except` 블록에는 추가로 `else` 절을 붙여줄 수 있습니다. 이 때 `else` 절은 어떤 예외도 발생하지 않았을 경우 호출됩니다.

다음으로는 예외 객체를 얻어오는 방법과 이를 통해 예외에 대한 추가 정보를 얻어오는 방법에 대해 알아보겠습니다.

## 예외 발생시키기

`raise` 문에 오류나 예외의 이름을 넘겨 주는 것을 통해 예외를 직접 발생(_raise_) 시킬 수 있습니다. 그러면 예외 객체가 _throw_ 됩니다.

이 때 발생시킬 수 있는 오류나 예외는 반드시 직접적으로든 간접적으로든 Exception 클래스에서 파생된 클래스이어야 합니다.

예제 (`exceptions_raise.py` 로 저장하세요):

<pre><code class="lang-python">{% include "./programs/exceptions_raise.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/exceptions_raise.txt" %}</code></pre>

**동작 원리**

위 예제에서는 `ShortInputException` 이라고 하는 새로운 예외 형식을 직접 하나 만들어 보았습니다. 여기에는 두 개의 필드가 있습니다. 하나는 `length` 필드로 주어진 입력의 길이를 의미하며, 또 하나는 `atleast` 필드로 프로그램이 요구하는 최소한의 길이를 의미합니다.

이제 `except` 절에서 `as` 를 이용하여 해당 오류의 클래스를 좀 더 짧은 이름의 변수로 대신하여 사용할 수 있게 해 줍니다. 여기서 새로 정의한 예외 형식에 정의한 필드와 값의 관계는 마치 함수에서의 매개 변수와 인수의 관계와 비슷합니다. 마지막으로 이 오류를 처리해주는 `except` 절에서는 해당 예외 객체의 `length` 와 `atleast` 필드를 이용하여 사용자에게 적절한 결과를 출력해 줍니다.

## Try ... Finally 문 {#try-finally}

프로그램이 파일을 읽고 있는 상황을 가정해 봅시다. 이 때 예외가 발생할 경우, 예외의 발생 여부와 상관없이 파일 객체를 항상 닫아 주도록 할 수는 없을까요? 이를 위해 `finally` 블록을 사용합니다.

아래 프로그램을 `exceptions_finally.py` 로 저장하세요:

<pre><code class="lang-python">{% include "./programs/exceptions_finally.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/exceptions_finally.txt" %}</code></pre>

**동작 원리**

위 예데는 단순히 파일을 읽는 코드이지만, 파일에서 한 줄을 읽어올 때마다 `time.sleep` 함수를 호출하여 2초씩 멈추게 하는 인위적인 코드를 집어넣어 프로그램이 천천히 실행되도록 해 주었습니다 (파이썬은 원래 굉장히 빠릅니다). 프로그램이 실행중일 때, `ctrl + c` 를 눌러 프로그램을 강제로 중단 (interrupt) 시켜 봅시다.

그러면 `KeyboardInterrupt` 예외가 발생되며 프로그램이 종료됩니다. 그러나 프로그램이 종료되기 전에 finally 절이 실행되므로 열어주었던 파일 객체는 항상 닫히게 됩니다.

여기서 0, `None`, 빈 열거형 객체 등은 파이썬에서 `거짓 (False)` 에 해당하는 것으로 처리됩니다. 위 예제에서 `if f:` 를 쓸 수 있는 이유입니다.

또한 여기서 `print` 문 뒤에 `sys.stdout.flush()` 를 사용하여 화면에 결과를 곧바로 출력하도록 해 주었습니다.

## with 문 {#with}

`try` 블록에서 어떠한 시스템 자원을 가져오고 `finally` 문에서 이를 해제하여 주는 것은 자주 활용되는 패턴입니다. 그렇지만, `with` 문을 활용하면 이것을 좀 더 깔끔하게 작성해 줄 수 있습니다:

`exceptions_using_with.py` 로 저장하세요:

<pre><code class="lang-python">{% include "./programs/exceptions_using_with.py" %}</code></pre>

**동작 원리**

위 예제는 이전의 예제와 동일한 결과를 출력합니다. 차이점은 `open` 함수를 사용할 때 `with` 문을 사용하였다는 것입니다. 그러면 파일을 직접 닫아 주지 않아도 `with open` 이 자동으로 파일을 닫아 줍니다.

그러면 `with` 문은 어떻게 자동으로 이러한 것들을 처리해 주는 것일까요? 우선 `with` 문은 `open` 문이 반환해 주는 객체를 받아 오는데, 일단 여기서는 이것을 "thefile" 이라고 해 봅시다.

with 문은 항상 `thefile.__enter__` 함수를 호출한 뒤 해당 블록의 코드를 실행하며, 실행이 끝난 후에는 항상 `thefile.__exit__` 를 호출합니다.

따라서 `finally` 블록에서 써 줬어야 했을 코드가 `__exit__` 메소드에 의해 자동적으로 이루어지는 것입니다. 따라서 `with`를 쓰면 매번 `try..finally` 문을 명시적으로 쓰지 않고도 같은 일을 할 수 있습니다.

이에 대한 좀 더 자세한 설명은 이 책이 다루는 범위를 벗어납니다. 자세한 설명은 [PEP 343](http://www.python.org/dev/peps/pep-0343/) 을 읽어 보시기 바랍니다.

## 요약

지금까지 `try..except` 문과 `try..finally` 문의 사용법을 배워 보았습니다. 또 사용자 정의 예외 형식을 만드는 법과 예외를 일으키는 법에 대해서도 알아 보았습니다.

다음으로, 파이썬 표준 라이브러리에 대해 알아 보겠습니다.
