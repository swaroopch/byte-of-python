# Exceptions

Exceptions occur when _exceptional_ situations occur in your program. For example, what if you are going to read a file and the file does not exist? Or what if you accidentally deleted it when the program was running? Such situations are handled using **exceptions**.

Similarly, what if your program had some invalid statements? This is handled by Python which **raises** its hands and tells you there is an **error**.

## Errors

Consider a simple `print` function call. What if we misspelt `print` as `Print`? Note the capitalization. In this case, Python _raises_ a syntax error.

```python
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
```

Observe that a `NameError` is raised and also the location where the error was detected is printed. This is what an **error handler** for this error does.

## Exceptions

We will **try** to read input from the user. Enter the first line below and hit the `Enter` key. When your computer prompts you for input, instead press `[ctrl-d]` on a Mac or `[ctrl-z]` with Windows and see what happens. (If you're using Windows and neither option works, you can try `[ctrl-c]` in the Command Prompt to generate a KeyboardInterrupt error instead).

```python
>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

Python raises an error called `EOFError` which basically means it found an _end of file_ symbol (which is represented by `ctrl-d`) when it did not expect to see it.

## Handling Exceptions

We can handle exceptions using the `try..except` statement. We basically put our usual statements within the try-block and put all our error handlers in the except-block.

Example (save as `exceptions_handle.py`):

<pre><code class="lang-python">{% include "./programs/exceptions_handle.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/exceptions_handle.txt" %}</code></pre>

**How It Works**

We put all the statements that might raise exceptions/errors inside the `try` block and then put handlers for the appropriate errors/exceptions in the `except` clause/block. The `except` clause can handle a single specified error or exception, or a parenthesized list of errors/exceptions. If no names of errors or exceptions are supplied, it will handle _all_ errors and exceptions.

Note that there has to be at least one `except` clause associated with every `try` clause. Otherwise, what's the point of having a try block?

If any error or exception is not handled, then the default Python handler is called which just stops the execution of the program and prints an error message. We have already seen this in action above.

You can also have an `else` clause associated with a `try..except` block. The `else` clause is executed if no exception occurs.

In the next example, we will also see how to get the exception object so that we can retrieve additional information.

## Raising Exceptions

You can _raise_ exceptions using the `raise` statement by providing the name of the error/exception and the exception object that is to be _thrown_.

The error or exception that you can raise should be a class which directly or indirectly must be a derived class of the `Exception` class.

Example (save as `exceptions_raise.py`):

<pre><code class="lang-python">{% include "./programs/exceptions_raise.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/exceptions_raise.txt" %}</code></pre>

**How It Works**

Here, we are creating our own exception type. This new exception type is called `ShortInputException`. It has two fields - `length` which is the length of the given input, and `atleast` which is the minimum length that the program was expecting.

In the `except` clause, we mention the class of error which will be stored `as` the variable name to hold the corresponding error/exception object. This is analogous to parameters and arguments in a function call. Within this particular `except` clause, we use the `length` and `atleast` fields of the exception object to print an appropriate message to the user.

## Try ... Finally {#try-finally}

Suppose you are reading a file in your program. How do you ensure that the file object is closed properly whether or not an exception was raised? This can be done using the `finally` block.

Save this program as `exceptions_finally.py`:

<pre><code class="lang-python">{% include "./programs/exceptions_finally.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/exceptions_finally.txt" %}</code></pre>

**How It Works**

We do the usual file-reading stuff, but we have arbitrarily introduced sleeping for 2 seconds after printing each line using the `time.sleep` function so that the program runs slowly (Python is very fast by nature). When the program is still running, press `ctrl + c` to interrupt/cancel the program.

Observe that the `KeyboardInterrupt` exception is thrown and the program quits. However, before the program exits, the finally clause is executed and the file object is always closed.

Notice that a variable assigned a value of 0 or `None` or a variable which is an empty sequence or collection is considered `False` by Python. This is why we can use `if f:` in the code above.

Also note that we use `sys.stdout.flush()` after `print` so that it prints to the screen immediately.

## The with statement {#with}

Acquiring a resource in the `try` block and subsequently releasing the resource in the `finally` block is a common pattern. Hence, there is also a `with` statement that enables this to be done in a clean manner:

Save as `exceptions_using_with.py`:

<pre><code class="lang-python">{% include "./programs/exceptions_using_with.py" %}</code></pre>

**How It Works**

The output should be same as the previous example. The difference here is that we are using the `open` function with the `with` statement - we leave the closing of the file to be done automatically by `with open`.

What happens behind the scenes is that there is a protocol used by the `with` statement. It fetches the object returned by the `open` statement, let's call it "thefile" in this case.

It _always_ calls the `thefile.__enter__` function before starting the block of code under it and _always_ calls `thefile.__exit__` after finishing the block of code.

So the code that we would have written in a `finally` block should be taken care of automatically by the `__exit__` method. This is what helps us to avoid having to use explicit `try..finally` statements repeatedly.

More discussion on this topic is beyond scope of this book, so please refer [PEP 343](http://www.python.org/dev/peps/pep-0343/) for a comprehensive explanation.

## Summary

We have discussed the usage of the `try..except` and `try..finally` statements. We have seen how to create our own exception types and how to raise exceptions as well.

Next, we will explore the Python Standard Library.
