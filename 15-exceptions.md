# Exceptions #

Exceptions occur when certain *exceptional* situations occur in your
program.  For example, what if you are going to read a file and the
file does not exist? Or what if you accidentally deleted it when the
program was running? Such situations are handled using **exceptions**.

Similarly, what if your program had some invalid statements? This is
handled by Python which **raises** its hands and tells you there is an
**error**.

## Errors ##

Consider a simple `print` function call. What if we misspelt `print`
as `Print`? Note the capitalization. In this case, Python *raises* a
syntax error.

~~~
>>> Print('Hello World')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Print('Hello World')
NameError: name 'Print' is not defined
>>> print('Hello World')
Hello World
~~~

Observe that a `NameError` is raised and also the location where the
error was detected is printed. This is what an *error handler* for
this error does.

## Exceptions ##

We will **try** to read input from the user. Press `ctrl-d` and see
what happens.

~~~
>>> s = input('Enter something --> ')
Enter something --> 
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s = input('Enter something --> ')
EOFError: EOF when reading a line
~~~

Python raises an error called `EOFError` which basically means it
found an *end of file* symbol (which is represented by `ctrl-d`) when
it did not expect to see it.

## Handling Exceptions ##

We can handle exceptions using the `try..except` statement.  We
basically put our usual statements within the try-block and put all
our error handlers in the except-block.

Example (save as `try_except.py`):

~~~python
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {0}'.format(text))
~~~

Output:

~~~
$ python3 try_except.py
Enter something -->     # Press ctrl-d
Why did you do an EOF on me?

$ python3 try_except.py
Enter something -->     # Press ctrl-c
You cancelled the operation.

$ python3 try_except.py
Enter something --> no exceptions
You entered no exceptions
~~~

How It Works:

We put all the statements that might raise exceptions/errors inside
the `try` block and then put handlers for the appropriate
errors/exceptions in the `except` clause/block. The `except` clause
can handle a single specified error or exception, or a parenthesized
list of errors/exceptions. If no names of errors or exceptions are
supplied, it will handle *all* errors and exceptions.

Note that there has to be at least one `except` clause associated with
every `try` clause. Otherwise, what's the point of having a try block?

If any error or exception is not handled, then the default Python
handler is called which just stops the execution of the program and
prints an error message. We have already seen this in action above.

You can also have an `else` clause associated with a `try..except`
block. The `else` clause is executed if no exception occurs.

In the next example, we will also see how to get the exception object
so that we can retrieve additional information.

## Raising Exceptions ##

You can *raise* exceptions using the `raise` statement by providing
the name of the error/exception and the exception object that is to be
*thrown*.

The error or exception that you can raise should be a class which
directly or indirectly must be a derived class of the `Exception`
class.

Example (save as `raising.py`):

~~~python
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print('ShortInputException: The input was {0} long, expected at least {1}'\
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
~~~

Output:

~~~
$ python3 raising.py
Enter something --> a
ShortInputException: The input was 1 long, expected at least 3

$ python3 raising.py
Enter something --> abc
No exception was raised.
~~~

How It Works:

Here, we are creating our own exception type. This new exception type
is called `ShortInputException`. It has two fields - `length` which is
the length of the given input, and `atleast` which is the minimum
length that the program was expecting.

In the `except` clause, we mention the class of error which will be
stored `as` the variable name to hold the corresponding
error/exception object. This is analogous to parameters and arguments
in a function call. Within this particular `except` clause, we use
the`length` and `atleast` fields of the exception object to print an
appropriate message to the user.

## Try .. Finally ##

Suppose you are reading a file in your program. How do you ensure that
the file object is closed properly whether or not an exception was
raised? This can be done using the `finally` block.

Save this program as `finally.py`:

~~~python
import time

f = None
try:
    f = open("poem.txt")
    while True:  # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="", flush=True)
        time.sleep(2)  # To make sure it runs for a while
except FileNotFoundError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
~~~

Output:

~~~
$ python3 finally.py
Programming is fun
When the work is done
if you wanna make your work also fun:
!! You cancelled the reading from the file.
(Cleaning up: Closed the file)
~~~

How It Works:

We do the usual file-reading stuff, but we have arbitrarily introduced
sleeping for 2 seconds after printing each line using the `time.sleep`
function so that the program runs slowly (Python is very fast by
nature). When the program is still running, press `ctrl-c` to
interrupt/cancel the program.

Observe that the `KeyboardInterrupt` exception is thrown and the
program quits. However, before the program exits, the finally clause
is executed and the file object is always closed.

Note that we use `flush=True` in the call to `print()` so that it
prints to the screen immediately.

## The with statement ##

Acquiring a resource in the `try` block and subsequently releasing the
resource in the `finally` block is a common pattern. Hence, there is
also a `with` statement that enables this to be done in a clean
manner:

Save as `using_with.py`:

~~~python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
~~~

How It Works:

The output should be same as the previous example. The difference here
is that we are using the `open` function with the `with` statement -
we leave the closing of the file to be done automatically by `with
open`.

What happens behind the scenes is that there is a protocol used by the
`with` statement. It fetches the object returned by the `open`
statement, let's call it "thefile" in this case.

It *always* calls the `thefile.__enter__` function before starting the
block of code under it and *always* calls `thefile.__exit__` after
finishing the block of code.

So the code that we would have written in a `finally` block should be
taken care of automatically by the `__exit__`method. This is what
helps us to avoid having to use explicit `try..finally` statements
repeatedly.

More discussion on this topic is beyond scope of this book, so please
refer [PEP 343](http://www.python.org/dev/peps/pep-0343/) for a
comprehensive explanation.

## Summary ##

We have discussed the usage of the `try..except` and `try..finally`
statements. We have seen how to create our own exception types and how
to raise exceptions as well.

Next, we will explore the Python Standard Library.
