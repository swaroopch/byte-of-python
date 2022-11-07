# 더 많은 것들

지금까지 앞으로 여러분이 사용하게 될 파이썬의 여러 주요한 기능들에 대해 다뤄 보았습니다. 이 챕터에서는, 여러분이 앞으로 파이썬을 사용하면서 추가로 알아두면 좋을 몇 가지를 다뤄 보겠습니다.

## 튜플 넘기기

함수의 실행 결과로 두 개 이상의 값을 반환하고 싶을 때가 있지 않았나요? 파이썬에서는 할 수 있습니다. 단순히 튜플을 넘겨 주기만 하면 됩니다.

```python
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
```

위와 같이 `a, b = <계산식>` 과 같이 해 주면 계산식의 결과로 넘어온 튜플이 자동으로 두 값에 알맞게 들어가게 됩니다.

이것을 활용하면 두 변수의 값을 바꾸어야 할 때 다음과 같이 할 수 있습니다:

```python
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

## 특별한 메소드들

클래스에는 `__init__` 이나 `__del__` 메소드처럼 특별한 일을 하는 몇 개의 메소드들이 있습니다.

이러한 특별한 메소드들을 이용하면 파이썬에서 지원하는 내장 형식들이 동작하는 방식을 똑같이 흉내낼 수 있습니다. 예를 들어, 여러분이 새로 만든 클래스에서 `x[key]` 와 같은 형태의 인덱싱 연산을 가능하게 하고 싶을 경우 (리스트나 튜플처럼), 클래스에 `__getitem__()` 메소드를 구현해 주면 됩니다. 사실 파이썬에 내장된 `list` 클래스도 이러한 방식으로 구현되어 있습니다!

아래에 몇 개의 유용한 특별한 메소드의 목록이 있습니다. 모든 특별한 메소드들에 대해 알고 싶으시면, [공식 설명서](http://docs.python.org/3/reference/datamodel.html#special-method-names)를 읽어 보세요.

- `__init__(self, ...)`
    - 이 메소드는 객체가 새로 생성될 때 호출됩니다.

- `__del__(self)`
    - 이 메소드는 객체가 메모리에서 제거되기 직전에 호출됩니다 (그러나 이것은 언제 호출될 지 그 시점이 분명하지 않으므로 가능하면 사용을 피하세요).

- `__str__(self)`
    - `print` 문이라던가 `str()` 등이 사용될 경우 호출되어 객체의 문자열 표현을 반환합니다.

- `__lt__(self, other)`
    - _작음_ 연산자 (<) 가 사용될 경우 호출됩니다. 이와 비슷하게, 모든 연산자(+, >, 등등)에 해당하는 특별한 메소드들이 하나씩 따로 존재합니다.

- `__getitem__(self, key)`
    - `x[key] `형태의 인덱싱 연산이 사용될 경우 호출됩니다.

- `__len__(self)`
    - 열거형 객체의 길이를 얻어오기 위한 내장 함수 `len()` 이 사용될 경우 호출됩니다.

## 한 줄짜리 블록

지금까지 여러분이 작성한 프로그램에서는 각 블록이 서로 다른 들여쓰기 단계에 따라 구분되어 있었을 것입니다. 그렇지만 한 가지 예외가 있습니다. 만약 블록에 딱 한 개의 명령만 존재하는 경우, 특히 조건문이나 반복문을 사용할 때, 한 줄에 해당 명령을 이어서 지정해 줄 수 있습니다. 아래 예제를 보면 이것을 좀 더 명확하게 이해할 수 있을 것입니다:

```python
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

위와 같이, 한 줄짜리 블록은 새로 블록을 생성하지 않고 그 줄 뒤에 이어서 사용됩니다. 이러한 방식을 사용하면 여러분의 프로그램을 몇 줄 _줄여줄_ 수는 있겠지만, 디버깅을 할 때와 같은 경우를 제외하고는 가능하면 이 방법을 사용하지 않기를 강력히 권합니다. 그 주된 이유는 적절한 들여쓰기를 사용할 경우, 그 아래에 추가 명령을 삽입하기가 좀 더 쉬워지기 때문입니다.

## 람다 (Lambda) 함수

`lambda` 문은 새 함수 객체를 만들 때 사용됩니다. 기본적으로 `lambda` 문은 한 줄짜리 수식으로, 파라미터를 받는 부분과 람다 함수 본체로 구성되어 있습니다. 이렇게 만들어진 함수를 호출하면, 지정된 수식의 계산 결과가 함수의 결과값으로 반환됩니다.

예제 (`more_lambda.py` 로 저장하세요):

<pre><code class="lang-python">{% include "./programs/more_lambda.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/more_lambda.txt" %}</code></pre>

**동작 원리**

여기서 `list` 의 `sort` 메소드는 `key` 매개 변수를 인자로 받는데, 이것은 어떻게 리스트를 정렬할 것인지를 결정해주는 것입니다 (주로 오름차순으로 할 지 내림차순으로 할 지를 지정해 주는 데 쓰는 경우가 많습니다). 위 예제에서는 우리가 정의한 특별한 방식대로 정렬을 해 주려고 하며, 따라서 정렬 순서를 결정해 줄 수 있는 함수를 하나 만들어 주어야 합니다. 이 때 `def` 블록을 사용하여 함수를 생성하지 않고 lambda 식을 사용하여 새 함수를 그 자리에서 바로 만들어 주었습니다.

## 리스트 축약 (Comprehension)

리스트 축약 (또는 리스트 컴프리헨션) 은 이미 존재하는 하나의 리스트를 기반으로 또 다른 리스트를 생성할 때 사용됩니다. 예를 들어 숫자로 이루어진 리스트가 하나 있을 때 이 리스트의 모든 항목에 대해 각 항목이 2 보다 클 경우에만 2 를 곱해준 리스트를 생성하고 싶다고 해 봅시다. 리스트 축약은 이러한 종류의 상황에 적절하게 사용될 수 있습니다.

예제 (`more_list_comprehension.py` 로 저장하세요):

<pre><code class="lang-python">{% include "./programs/more_list_comprehension.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/more_list_comprehension.txt" %}</code></pre>

**동작 원리**

위 예제에서는 기존 리스트에서 특정 조건 (`if i > 2`)을 만족하는 항목에 대해 2 를 곱해주는 조작을 가한 (`2*i`) 새 리스트를 생성하였습니다. 이 때 기존 리스트는 변경되지 않습니다.

리스트 축약을 사용하면 반복문을 사용하여 리스트에 있는 각각의 항목에 접근하고 새 리스트를 생성하는 등 많은 양의 코드를 한번에 줄여서 쓸 수 있는 장점이 있습니다.

## 함수 인자를 튜플이나 사전 형태로 넘겨받기

`*` 혹은 `**` 을 활용하면 함수의 매개 변수를 튜플이나 사전 형태로 넘겨받을 수도 있습니다. 이 방법은 함수의 인자의 개수가 정해지지 않은 함수를 정의하고 싶을 때 유용하게 사용됩니다.

```python
>>> def powersum(power, *args):
...     '''Return the sum of each argument raised to the specified power.'''
...     total = 0
...     for i in args:
...         total += pow(i, power)
...     return total
...
>>> powersum(2, 3, 4)
25
>>> powersum(2, 10)
100
```

변수 `args` 앞에 `*` 을 붙여 주면, 함수로 넘겨진 모든 다른 인수들이 args 라는 튜플에 담겨진 형태로 함수에 넘어오게 됩니다. `*` 대신 `**` 을 앞에 붙여 주면, 이번에는 인수들이 사전의 형태, 즉 키/값 쌍의 형태로 변환되어 넘어오게 됩니다.

## assert 문 {#assert}

`assert` 문은 어떤 조건이 참인지 확실하게 하고 싶을 때 사용됩니다. 예를 들어, 리스트에 반드시 적어도 한 개의 항목이 담겨 있어야 하는 상황을 가정해 봅시다. 이 때 그렇지 않은 경우 오류 메시지가 나타나야 할 것입니다. 이러한 경우 assert 문을 활용할 수 있으며, 이는 주어진 조건이 참이 아닌 경우, AssertionError 를 발생시킵니다.

아래 예제의 `pop()` 메소드는 리스트의 마지막 아이템을 반환한 뒤 이를 삭제하는 메소드입니다.

```python
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

`assert` 문은 신중하게 사용하여야 합니다. 보통 이렇게 하기보다는 예외 처리 구문을 작성하여, 문제가 무엇인지 확인하고 사용자에게 오류 메시지를 보여준 뒤 프로그램을 종료하게 하는 과정을 거치도록 하는 것이 낫습니다.

## 데코레이터 {#decorator}

데코레이터는 어떤 함수를 감싸 주는 함수를 축약하여 간단하게 표현한 것입니다. 이것은 특정 코드를 "감싸는" 일을 계속 반복하여 해야 할 경우 유용하게 사용됩니다. 아래 예제에서는 어떤 함수가 실행되는 중에 오류가 발생하면 최대 5 번 까지, 일정 간격을 두고 재실행하게 하는 `retry` 데코레이터를 만들어 주었습니다. 이러한 데코레이터는 여러분이 원격 컴퓨터에 네트워크를 통해 접속을 시도하거나 하는 상황 등에서 유용하게 활용될 수 있습니다:

<pre><code class="lang-python">{% include "./programs/more_decorator.py" %}</code></pre>

실행 결과:

<pre><code>{% include "./programs/more_decorator.txt" %}</code></pre>

**동작 원리**

다음을 참고하세요:

- [Video : Python Decorators Made Easy](https://youtu.be/MYAEv3JoenI) 
- http://www.ibm.com/developerworks/linux/library/l-cpdecor.html
- http://toumorokoshi.github.io/dry-principles-through-python-decorators.html

## 파이썬 2와 3의 차이점 {#two-vs-three}

다음을 참고하세요:

- ["Six" library](http://pythonhosted.org/six/)
- [Porting to Python 3 Redux by Armin](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
- [Python 3 experience by PyDanny](http://pydanny.com/experiences-with-django-python3.html)
- [Official Django Guide to Porting to Python 3](https://docs.djangoproject.com/en/dev/topics/python3/)
- [Discussion on What are the advantages to python 3.x?](http://www.reddit.com/r/Python/comments/22ovb3/what_are_the_advantages_to_python_3x/)

## 요약

이 챕터에서는 파이썬의 여러 기능에 대해 좀 더 다양하게 살펴보았습니다. 아직 우리가 파이썬의 모든 기능을 다 짚고 넘어온 것은 아니지만, 여러분이 실전에서 사용할 수 있을 만큼은 충분히 다루었습니다. 이제 앞으로 무엇을 더 배워야 할 지에 대해서는 앞으로 여러분이 어떤 프로그램을 만들게 될 지에 따라 여러분이 직접 결정하면 될 것입니다.

다음으로 파이썬을 좀 더 자세히 공부해 볼 수 있는 방법에 대해 알아보겠습니다.
