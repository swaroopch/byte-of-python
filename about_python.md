# 파이썬, 누구냐 넌

파이썬은 간결하고 기능이 강력한 프로그래밍 언어 중 하나로, 복잡한 문법이나 프로그래밍 언어 구조에 신경쓰는 대신 문제 해결에만 집중할 수 있게 해줍니다.

공식 파이썬 프로그래밍 언어 소개에 따르면,

> 파이썬은 배우기 쉽고 기능도 강력한 프로그래밍 언어입니다. 파이썬은 효율적인 하이 레벨 데이터 구조를 제공하며, 단순하고 효율적으로 객체 지향 프로그래밍을 할 수 있게 도와줍니다. 파이썬의 우아한 문법, 동적 타이핑과 소스 코드를 바로 실행할 수 있게 하는 인터프리터 언어의 특성이 여러 분야의 다양한 플랫폼에서 어떠한 프로그램이든 빠르게 개발할 수 있게 도와줄 것입니다.

파이썬의 다양한 기능은 아래의 `파이썬의 기능`에서 자세히 설명하도록 하겠습니다.

## '파이썬'이라는 이름의 유래

파이썬을 개발한 프로그래머 귀도 반 로섬(Guido van Rossum, 1956~)은 영국 방송사 BBC의 "Monty Python's Flying Circus"라는 쇼를 보고 자신이 개발한 프로그래밍 언어에 파이썬이라는 이름을 붙였습니다. 그는 몸으로 먹이가 될 사냥감을 감싼 다음, 사냥감을 서서히 조여서 죽이는 비단뱀(python)을 특히 싫어한다고 말했습니다.

## 파이썬의 기능

### 간결함

<!-- strict english: really formal/correct english with no slang or improper usage -->

파이썬은 매우 간단하고 깔끔한 프로그래밍 언어입니다. 잘 짜여진 파이썬 프로그램의 소스 코드를 읽어보면 마치 맞춤법을 철저하게 지키는 영어 지문을 읽는 것 같다는 생각이 들 것입니다. 파이썬은 이렇게 문법이 복잡하지 않고 의사 코드(pseudo-code)처럼 이해하기 쉬워, 프로그래밍 문제 해결에만 집중할 수 있게 해줍니다.

### 배우기 쉬운 언어

파이썬은 정말 배우기 쉬운 언어로, 위에서 설명했듯이 문법도 매우 단순합니다.

### 오픈 소스

_자유 오픈 소스 소프트웨어_(FLOSS, Free/Libré and Open Source Software)는 자유롭게 배포할 수 있고, 소스 코드가 공개되어 있으며, 그 소스 코드를 마음대로 수정할 수 있고, 다른 자유 소프트웨어에 포함할 수 있는 소프트웨어를 말합니다.
파이썬은 자유 오픈 소스 소프트웨어로, 더 많은 지식을 공유하고자 하는 파이썬 커뮤니티에 의해 계속 개선이 이루어지고 있습니다.

### 고급 언어

파이썬은 고급 프로그래밍 언어(high-level language)에 속하며, C언어같은 저급 프로그래밍 언어(low-level language)처럼 프로그램의 메모리를 직접 관리할 필요가 없습니다.

### 강력한 휴대성

Due to its open-source nature, Python has been ported to (i.e. changed to make it work on) many platforms. All your Python programs can work on any of these platforms without requiring any changes at all if you are careful enough to avoid any system-dependent features.

파이썬은 GNU/Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE와 PocketPC 등의 다양한 운영 체제(operating system)에서 사용할 수 있습니다.

[Kivy](http://kivy.org)같은 프레임워크를 사용해 컴퓨터 게임을 만들거나 iPhone, iPad나 Android 앱을 개발할 수도 있습니다.

### 인터프리터 언어

이제 컴파일 언어와 인터프리터 언어가 무엇인지 설명을 해보겠습니다.

A program written in a compiled language like C or C\++ is converted from the source language i.e. C or C++ into a language that is spoken by your computer (binary code i.e. 0s and 1s) using a compiler with various flags and options. When you run the program, the linker/loader software copies the program from hard disk to memory and starts running it.

Python, on the other hand, does not need compilation to binary. You just _run_ the program directly from the source code. Internally, Python converts the source code into an intermediate form called bytecodes and then translates this into the native language of your computer and then runs it. All this, actually, makes using Python much easier since you don't have to worry about compiling the program, making sure that the proper libraries are linked and loaded, etc. This also makes your Python programs much more portable, since you can just copy your Python program onto another computer and it just works!

### 객체 지향 프로그래밍 언어

Python supports procedure-oriented programming as well as object-oriented programming. In _procedure-oriented_ languages, the program is built around procedures or functions which are nothing but reusable pieces of programs. In _object-oriented_ languages, the program is built around objects which combine data and functionality. Python has a very powerful but simplistic way of doing OOP, especially when compared to big languages like C++ or Java.

### 확장성

파이썬 프로그램 중 공개하고 싶지 않은 알고리즘이나 빠른 계산이 요구되는 부분이 있다면, 그 부분만 C/C\++언어로 구현한 다음 파이썬에서 쓸 수 있습니다.

### 다른 프로그래밍 언어에 포함 가능

파이썬 코드 일부를 C/C\++언어 프로그램에 포함하여 your program's users에게 _scripting_ capabilities를 give할 수 있습니다.

### 확장 가능한 라이브러리

The Python Standard Library is huge indeed. It can help you do various things involving regular expressions,documentation generation, unit testing, threading, databases, web browsers, CGI, FTP, email, XML, XML-RPC, HTML, WAV files, cryptography, GUI (graphical user interfaces), and other system-dependent stuff. Remember, all this is always available wherever Python is installed. This is called the _Batteries Included_ philosophy of Python.

Besides the standard library, there are various other high-quality libraries which you can find at the [Python Package Index](http://pypi.python.org/pypi).

### 정리

파이썬은 강력한 기능을 가진 프로그래밍 언어입니다. 파이썬은 프로그램의 성능을 어느 정도 생각하면서 여러가지 유용한 기능을 더한, 배우기 쉽고 재미있는 언어라고 할 수 있습니다.

## 파이썬 2와 파이썬 3의 비교

파이썬 3의 이전 버전인 '파이썬 2'와 '파이썬 3'의 차이를 알고 싶으시다면 이 부분을 읽어주세요. 이 책은 파이썬 3을 위한 책입니다.

Remember that once you have properly understood and learn to use one version, you can easily learn the differences and use the other one. The hard part is learning programming and understanding the basics of Python language itself. That is our goal in this book, and once you have achieved that goal, you can easily use Python 2 or Python 3 depending on your situation.

For details on differences between Python 2 and Python 3, see:

- [The future of Python 2](http://lwn.net/Articles/547191/)
- [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)
- [Writing code that runs under both Python2 and 3](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef)
- [Supporting Python 3: An in-depth guide](http://python3porting.com)

## 파이썬에 대한 해커들의 생각

다음은 에릭 레이먼드(Eric S. Raymond, 1957~)같이 영향력 있는 해커들이 말하는 파이썬의 장점에 대해 적은 글입니다.

- _Eric S. Raymond_ is the author of "The Cathedral and the Bazaar" and is also the person who coined the term _Open Source_. He says that [Python has become his favorite programming language](http://www.python.org/about/success/esr/). This article was the real inspiration for my first brush with Python.
- _Bruce Eckel_ is the author of the famous 'Thinking in Java' and 'Thinking in C++' books. He says that no language has made him more productive than Python. He says that Python is perhaps the only language that focuses on making things easier for the programmer. Read the [complete interview](http://www.artima.com/intv/aboutme.html) for more details.
- _Peter Norvig_ is a well-known Lisp author and Director of Search Quality at Google (thanks to Guido van Rossum for pointing that out). He says that [writing Python is like writing in pseudocode](https://news.ycombinator.com/item?id=1803815). He says that Python has always been an integral part of Google. You can actually verify this statement by looking at the [Google Jobs](http://www.google.com/jobs/index.html) page which lists Python knowledge as a requirement for software engineers.
