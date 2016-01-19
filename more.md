# More

So far we have covered a majority of the various aspects of Python that you will use. In this chapter, we will cover some more aspects that will make our knowledge of Python more well-rounded.

## Passing tuples around

Ever wished you could return two different values from a function? You can. All you have to do is use a tuple.

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

Notice that the usage of `a, b = <some expression>` interprets the result of the expression as a tuple with two values.

This also means the fastest way to swap two variables in Python is:

```python
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

## Special Methods

There are certain methods such as the `__init__` and `__del__` methods which have special significance in classes.

Special methods are used to mimic certain behaviors of built-in types. For example, if you want to use the `x[key]` indexing operation for your class (just like you use it for lists and tuples), then all you have to do is implement the `__getitem__()` method and your job is done. If you think about it, this is what Python does for the `list` class itself!

Some useful special methods are listed in the following table. If you want to know about all the special methods, [see the manual](http://docs.python.org/3/reference/datamodel.html#special-method-names).

- `__init__(self, ...)`
    - This method is called just before the newly created object is returned for usage.

- `__del__(self)`
    - Called just before the object is destroyed (which has unpredictable timing, so avoid using this)

- `__str__(self)`
    - Called when we use the `print` function or when `str()` is used.

- `__lt__(self, other)`
    - Called when the _less than_ operator (&lt;) is used. Similarly, there are special methods for all the operators (+, >, etc.)

- `__getitem__(self, key)`
    - Called when `x[key]` indexing operation is used.

- `__len__(self)`
    - Called when the built-in `len()` function is used for the sequence object.

## Single Statement Blocks

We have seen that each block of statements is set apart from the rest by its own indentation level. Well, there is one caveat. If your block of statements contains only one single statement, then you can specify it on the same line of, say, a conditional statement or looping statement. The following example should make this clear:

```python
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

Notice that the single statement is used in-place and not as a separate block.  Although, you can use this for making your program _smaller_, I strongly recommend avoiding this short-cut method, except for error checking, mainly because it will be much easier to add an extra statement if you are using proper indentation.

## Lambda Forms

A `lambda` statement is used to create new function objects. Essentially, the `lambda` takes a parameter followed by a single expression only which becomes the body of the function and the value of this expression is returned by the new function.

Example (save as `more_lambda.py`):

<pre><code class="lang-python">{% include "./programs/more_lambda.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/more_lambda.txt" %}</code></pre>

**How It Works**

Notice that the `sort` method of a `list` can take a `key` parameter which determines how the list is sorted (usually we know only about ascending or descending order). In our case, we want to do a custom sort, and for that we need to write a function but instead of writing a separate `def` block for a function that will get used in only this one place, we use a lambda expression to create a new function.

## List Comprehension

List comprehensions are used to derive a new list from an existing list. Suppose you have a list of numbers and you want to get a corresponding list with all the numbers multiplied by 2 only when the number itself is greater than 2. List comprehensions are ideal for such situations.

Example (save as `more_list_comprehension.py`):

<pre><code class="lang-python">{% include "./programs/more_list_comprehension.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/more_list_comprehension.txt" %}</code></pre>

**How It Works**

Here, we derive a new list by specifying the manipulation to be done (`2*i`) when some condition is satisfied (`if i > 2`). Note that the original list remains unmodified.

The advantage of using list comprehensions is that it reduces the amount of boilerplate code required when we use loops to process each element of a list and store it in a new list.

## Receiving Tuples and Dictionaries in Functions

There is a special way of receiving parameters to a function as a tuple or a dictionary using the `*` or `**` prefix respectively. This is useful when taking variable number of arguments in the function.

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

Because we have a `*` prefix on the `args` variable, all extra arguments passed to the function are stored in `args` as a tuple.  If a `**` prefix had been used instead, the extra parameters would be considered to be key/value pairs of a dictionary.

## The assert statement {#assert}

The `assert` statement is used to assert that something is true. For example, if you are very sure that you will have at least one element in a list you are using and want to check this, and raise an error if it is not true, then `assert` statement is ideal in this situation. When the assert statement fails, an `AssertionError` is raised.

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

The `assert` statement should be used judiciously. Most of the time, it is better to catch exceptions, either handle the problem or display an error message to the user and then quit.

## Decorators {#decorator}

Decorators are a shortcut to applying wrapper functions. This is helpful to "wrap" functionality with the same code over and over again. For example, I created a `retry` decorator for myself that I can just apply to any function and if any exception is thrown during a run, it is retried again, till a maximum of 5 times and with a delay between each retry. This is especially useful for situations where you are trying to make a network call to a remote computer:

<pre><code class="lang-python">{% include "./programs/more_decorator.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/more_decorator.txt" %}</code></pre>

**How It Works**

See:

- http://www.ibm.com/developerworks/linux/library/l-cpdecor.html
- http://toumorokoshi.github.io/dry-principles-through-python-decorators.html

## Differences between Python 2 and Python 3 {#two-vs-three}

See:

- ["Six" library](http://pythonhosted.org/six/)
- [Porting to Python 3 Redux by Armin](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
- [Python 3 experience by PyDanny](http://pydanny.com/experiences-with-django-python3.html)
- [Official Django Guide to Porting to Python 3](https://docs.djangoproject.com/en/dev/topics/python3/)
- [Discussion on What are the advantages to python 3.x?](http://www.reddit.com/r/Python/comments/22ovb3/what_are_the_advantages_to_python_3x/)

## Summary

We have covered some more features of Python in this chapter and yet we haven't covered all the features of Python. However, at this stage, we have covered most of what you are ever going to use in practice. This is sufficient for you to get started with whatever programs you are going to create.

Next, we will discuss how to explore Python further.
