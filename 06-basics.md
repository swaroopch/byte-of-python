# Basics

Just printing 'Hello World' is not enough, is it? You want to do more than that - you want to take some input, manipulate it and get something out of it. We can achieve this in Python using constants and variables, and we'll learn some other concepts as well in this chapter.

## Comments

*Comments* are any text to the right of the `#` symbol and is mainly useful as notes for the reader of the program.

For example:

~~~python
print('Hello World') # Note that print is a function
~~~

or:

~~~python
# Note that print is a function
print('Hello World')
~~~

Use as many useful comments as you can in your program to:

- explain assumptions
- explain important decisions
- explain important details
- explain problems you're trying to solve
- explain problems you're trying to overcome in your program, etc.

[*Code tells you how, comments should tell you why.*](http://www.codinghorror.com/blog/2006/12/code-tells-you-how-comments-tell-you-why.html)

This is useful for readers of your program so that they can easily understand what the program is doing. Remember, that person can be yourself after six months!

## Literal Constants

An example of a literal constant is a number like `5`, `1.23`, or a string like `'This is a string'`or `"It's a string!"`. It is called a literal because it is *literal* - you use its value literally. The number `2` always represents itself and nothing else - it is a *constant* because its value cannot be changed. Hence, all these are referred to as literal constants.

## Numbers

Numbers are mainly of two types - integers and floats.

An examples of an integer is `2` which is just a whole number.

Examples of floating point numbers (or *floats* for short) are `3.23` and `52.3E-4`. The `E` notation indicates powers of 10. In this case, `52.3E-4` means `52.3 * 10^-4^`.

Note for Experienced Programmers

:   There is no separate `long` type. The `int` type can be an integer of any size.

## Strings

A string is a *sequence* of *characters*. Strings are basically just a bunch of words.

You will be using strings in almost every Python program that you write, so pay attention to the following part.

### Single Quote

You can specify strings using single quotes such as `'Quote me on this'`. All white space i.e. spaces and tabs are preserved as-is.

### Double Quotes

Strings in double quotes work exactly the same way as strings in single quotes. An example is `"What's your name?"`

### Triple Quotes

You can specify multi-line strings using triple quotes - (`"""` or `'''`). You can use single quotes and double quotes freely within the triple quotes. An example is:

~~~python
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
~~~

### Strings Are Immutable

This means that once you have created a string, you cannot change it. Although this might seem like a bad thing, it really isn't. We will see why this is not a limitation in the various programs that we see later on.

Note for C/C++ Programmers

:   There is no separate `char` data type in Python. There is no real need for it and I am sure you won't miss it.

Note for Perl/PHP Programmers

:   Remember that single-quoted strings and double-quoted strings are the same - they do not differ in any way.

### The format method

Sometimes we may want to construct strings from other information. This is where the `format()` method is useful.

Save the following lines as a file `str_format.py`:

~~~python
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
~~~

Output:

~~~
$ python3 str_format.py
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
~~~

How It Works:

A string can use certain specifications and subsequently, the *format* method can be called to substitute those specifications with corresponding arguments to the `format` method.

Observe the first usage where we use `{0}` and this corresponds to the variable `name` which is the first argument to the format method. Similarly, the second specification is `{1}` corresponding to `age` which is the second argument to the format method. Note that Python starts counting from 0 which means that first position is at index 0, second position is at index 1, and so on.

Notice that we could have achieved the same using string concatenation: `name + ' is ' + str(age) + ' years old'` but that is much uglier and error-prone. Second, the conversion to string would be done automatically by the `format` method instead of the explicit conversion to strings needed in this case. Third, when using the `format` method, we can change the message without having to deal with the variables used and vice-versa.

Also note that the numbers are optional, so you could have also written as:

~~~python
age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
~~~

which will give the same exact output as the previous program.

What Python does in the `format` method is that it substitutes each argument value into the place of the specification. There can be more detailed specifications such as:

~~~python
 decimal (.) precision of 3 for float '0.333'
>>> '{0:.3}'.format(1/3)
 fill with underscores (_) with the text centered
 (^) to 11 width '___hello___'
>>> '{0:_^11}'.format('hello')
 keyword-based 'Swaroop wrote A Byte of Python'
>>> '{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python')
~~~

## Variable

Using just literal constants can soon become boring - we need some way of storing any information and manipulate them as well. This is where *variables* come into the picture. Variables are exactly what the name implies - their value can vary, i.e.,  you can store anything using a variable. Variables are just parts of your computer's memory where you store some information. Unlike literal constants, you need some method of accessing these variables and hence you give them names.

## Identifier Naming

Variables are examples of identifiers. *Identifiers* are names given to identify *something*. There are some rules you have to follow for naming identifiers:

- The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) or an underscore ('_').
- The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores ('_') or digits (0-9).
- Identifier names are case-sensitive. For example, `myname` and `myName` are **not** the same. Note the lowercase `n` in the former and the uppercase `N` in the latter.
- Examples of *valid* identifier names are `i`, `__my_name`, `name_23`. Examples of ''invalid'' identifier names are `2things`, `this is spaced out`, `my-name`, `>a1b2_c3` and `"this_is_in_quotes"`.

## Data Types

Variables can hold values of different types called **data types**. The basic types are numbers and strings, which we have already discussed. In later chapters, we will see how to create our own types using [classes](#object-oriented-programming).

## Object

Remember, Python refers to anything used in a program as an *object*.  This is meant in the generic sense. Instead of saying 'the *something*', we say 'the *object*'.

Note for Object Oriented Programming users

:   Python is strongly object-oriented in the sense that everything is an object including numbers, strings and functions.

We will now see how to use variables along with literal constants. Save the following example and run the program.

## How to write Python programs

Henceforth, the standard procedure to save and run a Python program is as follows:

#. Open your editor of choice, such as Komodo Edit.
#. Type the program code given in the example.
#. Save it as a file with the filename mentioned.
#. Run the interpreter with the command `python3 program.py` to run the program.

## Example: Using Variables And Literal Constants

~~~python
 Filename : var.py
i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)
~~~

Output:

~~~
$ python3 var.py
5
6
This is a multi-line string.
This is the second line.
~~~

How It Works:

Here's how this program works. First, we assign the literal constant value `5` to the variable `i` using the assignment operator (`=`). This line is called a statement because it states that something should be done and in this case, we connect the variable name `i` to the value `5`.  Next, we print the value of `i` using the `print` function which, unsurprisingly, just prints the value of the variable to the screen.

Then we add `1` to the value stored in `i` and store it back. We then print it and expectedly, we get the value `6`.

Similarly, we assign the literal string to the variable `s` and then print it.

Note for static language programmers

:   Variables are used by just assigning them a value. No declaration or data type definition is needed/used.

### Logical And Physical Line

A physical line is what you *see* when you write the program. A logical line is what *Python sees* as a single statement. Python implicitly assumes that each *physical line* corresponds to a *logical line*.

An example of a logical line is a statement like `print('Hello World')` - if this was on a line by itself (as you see it in an editor), then this also corresponds to a physical line.

Implicitly, Python encourages the use of a single statement per line which makes code more readable.

If you want to specify more than one logical line on a single physical line, then you have to explicitly specify this using a semicolon (`;`) which indicates the end of a logical line/statement. For example,

~~~python
i = 5
print(i)
~~~

is effectively same as

~~~python
i = 5;
print(i);
~~~

and the same can be written as

~~~python
i = 5; print(i);
~~~

or even

~~~python
i = 5; print(i)
~~~

However, I **strongly recommend** that you stick to **writing a maximum of a single logical line on each single physical line**. The idea is that you should never use the semicolon. In fact, I have *never* used or even seen a semicolon in a Python program.

There is one kind of situation where this concept is really useful : if you have a  long line of code, you can break it into multiple physical lines by using the backslash. This is referred to as **explicit line joining**:

~~~python
s = 'This is a string. \
This continues the string.'
print(s)
~~~

This gives the output:

~~~
This is a string. This continues the string.
~~~

Similarly,

~~~python
print\
(i)
~~~

is the same as

~~~python
print(i)
~~~

Sometimes, there is an implicit assumption where you don't need to use a backslash. This is the case where the logical line has a starting parentheses, starting square brackets or a starting curly braces but not an ending one. This is called **implicit line joining**. You can see this in action when we write programs using [lists](#list) in later chapters.

### Indentation

Whitespace is important in Python. Actually, **whitespace at the beginning of the line is important**. This is called **indentation**. Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements.

This means that statements which go together **must** have the same indentation. Each such set of statements is called a **block**. We will see examples of how blocks are important in later chapters.

One thing you should remember is that wrong indentation can give rise to errors. For example:

~~~python
i = 5
 print('Value is ', i) # Error! Notice a single space at the start of the line
print('I repeat, the value is ', i)
~~~

When you run this, you get the following error:

~~~
  File "whitespace.py", line 4
    print('Value is ', i) # Error! Notice a single space at the start of the line
    ^
IndentationError: unexpected indent
~~~

Notice that there is a single space at the beginning of the second line. The error indicated by Python tells us that the syntax of the program is invalid i.e. the program was not properly written. What this means to you is that *you cannot arbitrarily start new blocks of statements* (except for the default main block which you have been using all along, of course). Cases where you can use new blocks will be detailed in later chapters such as the [Control Flow](#control-flow).

How to indent

:   Use only spaces for indentation, with a tab stop of 4 spaces. Good editors like Komodo Edit will automatically do this for you. Make sure you use a consistent number of spaces for indentation, otherwise your program will show errors.

Note to static language programmers

:   Python will always use indentation for blocks and will never use braces. Run `from __future__ import braces` to learn more.

## Summary

Now that we have gone through many nitty-gritty details, we can move on to more interesting stuff such as control flow statements. Be sure to become comfortable with what you have read in this chapter.
