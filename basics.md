# 파이썬 기초 지식

3장에서는 `hello world`만을 출력하는 간단한 프로그램을 만들어 보았지만, 이번에는 상수와 변수 같은 다양한 개념을 배워 보고 `hello world` 이외의 다른 문자열을 출력하는 방법을 배워보겠습니다.

## 주석

주석은 보통 `#` 뒤에 오는 문자열을 가리키며, 다른 사람들이 프로그램을 쉽게 이해할 수 있도록 하기 위해 사용합니다.

다음은 주석의 사용 예입니다.

```python
print('hello world') # print()는 문자열을 화면에 표시한다.
```

```python
# print()는 문자열을 화면에 표시한다.
print('hello world')
```

주석은 주로 이런 경우에 많이 사용합니다.

- `"이 부분은 프로그램이 실행되면 이렇게 되겠지"` 같은 가정에 대해 자세히 적어놓고 싶을 때
- 문제 해결 중에 내린 중요한 결정이나 세부적인 내용을 설명할 필요가 있을 때
- 프로그램을 짜다가 막히는 부분을 적어놓고 싶을 때

[*Code tells you how, comments should tell you why*](http://www.codinghorror.com/blog/2006/12/code-tells-you-how-comments-tell-you-why.html).

주석은 작성한 프로그램을 다른 사람들이 보았을 때 그 내용을 쉽게 이해할 수 있도록 합니다. 프로그램을 몇 달 뒤에 다시 봤을 때 이해가 잘 안될 것 같으면 주석을 반드시 적어놓으세요.

## 리터럴

`5`, `1.23`, `'This is a string'`, `"It's a string!"`처럼 절대 변하지 않는 데이터 그 자체를 리터럴(literals)이라고 부릅니다.

리터럴([literal](https://dictionary.cambridge.org/dictionary/english/literal))은 영어로 '문자 그대로의'라는 뜻으로, _문자 그대로_ 값을 사용하기 때문에 붙은 이름입니다. 예를 들어, 숫자 `2`는 항상 2라는 값을 나타내고 절대로 변하지 않습니다.

> **참고: 다른 프로그래밍 언어에서 배우는 상수(constant)와 리터럴의 차이점은 다음과 같습니다.**
> - 상수는 정의한 다음에 그 값을 지정해주어야 합니다.
> - 리터럴은 변수나 상수에 지정되거나 단독으로 쓰이는 값 그 자체를 말합니다.

## 숫자

파이썬에서 숫자는 `2` 같은 정수형와 `3.23`나 `52.3E-4`같은 실수형으로 나눌 수 있습니다.

실수형 변수에서 `E`는 10의 제곱을 뜻합니다. 예를 들면, `52.3E-4`는 `52.3 * 10^-4^`와 같은 뜻입니다.

> **숙련된 프로그래머라면 참고하세요**
> 
> 파이썬 3에서 `long` 타입은 존재하지 않으며, `int` 타입에 모든 크기의 정수를 저장할 수 있습니다.

## 문자열

문자열은 단어나 문장처럼 여러 개의 문자가 모인 것을 말합니다.

문자열은 파이썬 프로그래머라면 반드시 알아두어야 하는 부분이므로, 다음 내용을 잘 기억해두도록 합시다.

### 따옴표

문자열은 `'Quote me on this'`이나 `"What's your name?"`처럼 작은 따옴표나 큰 따옴표 안에 저장합니다. 따옴표 안에 있는 스페이스나 탭 등의 공백은 그대로 저장됩니다.

여러 줄의 문자열은 `"""`이나 `'''` 안에 저장합니다. `"""`이나 `'''` 안에서는 다음과 같이 작은 따옴표나 큰 따옴표를 자유롭게 사용할 수 있습니다.

```python
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
```

### 문자열은 절대 수정할 수 없다

문자열은 한번 만들면 절대로 다시 수정할 수 없습니다. Although this might seem like
a bad thing, it really isn't. We will see why this is not a limitation in the various programs that
we see later on.

> **C/C++ 프로그래머라면 참고하세요**
> 
> There is no separate `char` data type in Python. There is no real need for it and I am sure you won't miss it.

<!-- -->

> **Perl/PHP 프로그래머라면 참고하세요**
> 
> Remember that single-quoted strings and double-quoted strings are the same - they do not differ in any way.

### format() 메소드 사용하기

Sometimes we may want to construct strings from other information. This is where the `format()` method is useful.

Save the following lines as a file `str_format.py`:

```python
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

Output:

```
$ python str_format.py
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

**How It Works**

A string can use certain specifications and subsequently, the `format` method can be called to substitute those specifications with corresponding arguments to the `format` method.

Observe the first usage where we use `{0}` and this corresponds to the variable `name` which is the first argument to the format method. Similarly, the second specification is `{1}` corresponding to `age` which is the second argument to the format method. Note that Python starts counting from 0 which means that first position is at index 0, second position is at index 1, and so on.

Notice that we could have achieved the same using string concatenation:

```python
name + ' is ' + str(age) + ' years old'
```

but that is much uglier and error-prone. Second, the conversion to string would be done automatically by the `format` method instead of the explicit conversion to strings needed in this case. Third, when using the `format` method, we can change the message without having to deal with the variables used and vice-versa.

Also note that the numbers are optional, so you could have also written as:

```python
age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
```

which will give the same exact output as the previous program.

We can also name the parameters:

```python
age = 20
name = 'Swaroop'

print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))
```

which will give the same exact output as the previous program.

Python 3.6 introduced a shorter way to do named parameters, called "f-strings":

```python
age = 20
name = 'Swaroop'

print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string
```

which will give the same exact output as the previous program.

What Python does in the `format` method is that it substitutes each argument value into the place of the specification. There can be more detailed specifications such as:

```python
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

Output:

```
0.333
___hello___
Swaroop wrote A Byte of Python
```

Since we are discussing formatting, note that `print` always ends with an invisible "new line" character (`\n`) so that repeated calls to `print` will all print on a separate line each. To prevent this newline character from being printed, you can specify that it should `end` with a blank:

```python
print('a', end='')
print('b', end='')
```

Output is:

```
ab
```

Or you can `end` with a space:

```python
print('a', end=' ')
print('b', end=' ')
print('c')
```

Output is:

```
a b c
```

### 이스케이프 문자

Suppose, you want to have a string which contains a single quote (`'`), how will you specify this string? For example, the string is `"What's your name?"`. You cannot specify `'What's your name?'` because Python will be confused as to where the string starts and ends. So, you will have to specify that this single quote does not indicate the end of the string. This can be done with the help of what is called an _escape sequence_. You specify the single quote as `\'` : notice the backslash. Now, you can specify the string as `'What\'s your name?'`.

Another way of specifying this specific string would be `"What's your name?"` i.e. using double quotes. Similarly, you have to use an escape sequence for using a double quote itself in a double quoted string. Also, you have to indicate the backslash itself using the escape sequence `\\`.

What if you wanted to specify a two-line string? One way is to use a triple-quoted string as shown [previously](#triple-quotes) or you can use an escape sequence for the newline character - `\n` to indicate the start of a new line. An example is:

```python
'This is the first line\nThis is the second line'
```

Another useful escape sequence to know is the tab: `\t`. There are many more escape sequences but I have mentioned only the most useful ones here.

One thing to note is that in a string, a single backslash at the end of the line indicates that the string is continued in the next line, but no newline is added. For example:

```python
"This is the first sentence. \
This is the second sentence."
```

is equivalent to

```python
"This is the first sentence. This is the second sentence."
```

### 순수 문자열

If you need to specify some strings where no special processing such as escape sequences are handled, then what you need is to specify a _raw_ string by prefixing `r` or `R` to the string. An example is:

```python
r"Newlines are indicated by \n"
```

> **정규 표현식을 사용하기 전 꼭 확인하세요**
> 
> Always use raw strings when dealing with regular expressions. Otherwise, a lot of backwhacking may be required. For example, backreferences can be referred to as `'\\1'` or `r'\1'`.

## 변수

Using just literal constants can soon become boring - we need some way of storing any information and manipulate them as well. This is where _variables_ come into the picture. Variables are exactly what the name implies - their value can vary, i.e., you can store anything using a variable. Variables are just parts of your computer's memory where you store some information. Unlike literal constants, you need some method of accessing these variables and hence you give them names.

## Identifier Naming

Variables are examples of identifiers. _Identifiers_ are names given to identify _something_. There are some rules you have to follow for naming identifiers:

- The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) or an underscore (`_`).
- The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (`_`) or digits (0-9).
- Identifier names are case-sensitive. For example, `myname` and `myName` are _not_ the same. Note the lowercase `n` in the former and the uppercase `N` in the latter.
- Examples of _valid_ identifier names are `i`, `name_2_3`. Examples of _invalid_ identifier names are `2things`, `this is spaced out`, `my-name` and `>a1b2_c3`.

## Data Types

Variables can hold values of different types called _data types_. The basic types are numbers and strings, which we have already discussed. In later chapters, we will see how to create our own types using [classes](./oop.md#classes).

## Object

Remember, Python refers to anything used in a program as an _object_.  This is meant in the generic sense. Instead of saying "the _something_"', we say "the _object_".

> **Note for Object Oriented Programming users**:
>
> Python is strongly object-oriented in the sense that everything is an object including numbers, strings and functions.

We will now see how to use variables along with literal constants. Save the following example and run the program.

## How to write Python programs

Henceforth, the standard procedure to save and run a Python program is as follows:

### For PyCharm

1. Open [PyCharm](./first_steps.md#pycharm).
2. Create new file with the filename mentioned.
3. Type the program code given in the example.
4. Right-click and run the current file.

NOTE: Whenever you have to provide [command line arguments](./modules.md#modules), click on `Run` -> `Edit Configurations` and type the arguments in the `Script parameters:` section and click the `OK` button:

![PyCharm command line arguments](./img/pycharm_command_line_arguments.png)

### For other editors

1. Open your editor of choice.
2. Type the program code given in the example.
3. Save it as a file with the filename mentioned.
4. Run the interpreter with the command `python program.py` to run the program.

### Example: Using Variables And Literal Constants

Type and run the following program:

```python
# Filename : var.py
i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)
```

Output:

```
5
6
This is a multi-line string.
This is the second line.
```

**How It Works**

Here's how this program works. First, we assign the literal constant value `5` to the variable `i` using the assignment operator (`=`). This line is called a statement because it states that something should be done and in this case, we connect the variable name `i` to the value `5`. Next, we print the value of `i` using the `print` statement which, unsurprisingly, just prints the value of the variable to the screen.

Then we add `1` to the value stored in `i` and store it back. We then print it and expectedly, we get the value `6`.

Similarly, we assign the literal string to the variable `s` and then print it.

> **Note for static language programmers**
> 
> Variables are used by just assigning them a value. No declaration or data type definition is needed/used.

## Logical And Physical Line

A physical line is what you _see_ when you write the program. A logical line is what _Python sees_ as a single statement. Python implicitly assumes that each _physical line_ corresponds to a _logical line_.

An example of a logical line is a statement like `print 'hello world'` - if this was on a line by itself (as you see it in an editor), then this also corresponds to a physical line.

Implicitly, Python encourages the use of a single statement per line which makes code more readable.

If you want to specify more than one logical line on a single physical line, then you have to explicitly specify this using a semicolon (`;`) which indicates the end of a logical line/statement. For example:

```python
i = 5
print(i)
```

is effectively same as

```python
i = 5;
print(i);
```

which is also same as

```python
i = 5; print(i);
```

and same as

```python
i = 5; print(i)
```

However, I *strongly recommend* that you stick to *writing a maximum of a single logical line on each single physical line*. The idea is that you should never use the semicolon. In fact, I have _never_ used or even seen a semicolon in a Python program.

There is one kind of situation where this concept is really useful: if you have a long line of code, you can break it into multiple physical lines by using the backslash. This is referred to as _explicit line joining_:

```python
s = 'This is a string. \
This continues the string.'
print(s)
```

Output:

```
This is a string. This continues the string.
```

Similarly,

```python
i = \
5
```

is the same as

```python
i = 5
```

Sometimes, there is an implicit assumption where you don't need to use a backslash. This is the case where the logical line has a starting parentheses, starting square brackets or a starting curly braces but not an ending one. This is called *implicit line joining*. You can see this in action when we write programs using [list](./data_structures.md#lists) in later chapters.

## 들여쓰기 (Indentation)

Whitespace is important in Python. Actually, *whitespace at the beginning of the line is important*. This is called _indentation_. Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements.

This means that statements which go together _must_ have the same indentation. Each such set of statements is called a *block*. We will see examples of how blocks are important in later chapters.

One thing you should remember is that wrong indentation can give rise to errors. For example:

```python
i = 5
# Error below! Notice a single space at the start of the line
 print('Value is', i)
print('I repeat, the value is', i)
```

When you run this, you get the following error:

```
  File "whitespace.py", line 3
    print('Value is', i)
    ^
IndentationError: unexpected indent
```

Notice that there is a single space at the beginning of the second line. The error indicated by Python tells us that the syntax of the program is invalid i.e. the program was not properly written. What this means to you is that _you cannot arbitrarily start new blocks of statements_ (except for the default main block which you have been using all along, of course). Cases where you can use new blocks will be detailed in later chapters such as the [control flow](./control_flow.md#control_flow).

> **How to indent**
> 
> Use four spaces for indentation. This is the official Python language recommendation. Good editors will automatically do this for you. Make sure you use a consistent number of spaces for indentation, otherwise your program will not run or will have unexpected behavior.

<!-- -->

> **Note to static language programmers**
> 
> Python will always use indentation for blocks and will never use braces. Run `from __future__ import braces` to learn more.

## 정리

Now that we have gone through many nitty-gritty details, we can move on to more interesting stuff such as control flow statements. Be sure to become comfortable with what you have read in this chapter.

