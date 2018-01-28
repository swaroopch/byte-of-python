# Input and Output {#io}

There will be situations where your program has to interact with the user. For example, you would want to take input from the user and then print some results back. We can achieve this using the `input()` function and `print` function respectively.

For output, we can also use the various methods of the `str` (string) class. For example, you can use the `rjust` method to get a string which is right justified to a specified width. See `help(str)` for more details.

Another common type of input/output is dealing with files. The ability to create, read and write files is essential to many programs and we will explore this aspect in this chapter.

## Input from user

Save this program as `io_input.py`:

<pre><code class="lang-python">{% include "./programs/io_input.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/io_input.txt" %}</code></pre>

**How It Works**

We use the slicing feature to reverse the text. We've already seen how we can make [slices from sequences](./data_structures.md#sequence) using the `seq[a:b]` code starting from position `a` to position `b`. We can also provide a third argument that determines the _step_ by which the slicing is done. The default step is `1` because of which it returns a continuous part of the text. Giving a negative step, i.e., `-1` will return the text in reverse.

The `input()` function takes a string as argument and displays it to the user. Then it waits for the user to type something and press the return key. Once the user has entered and pressed the return key, the `input()` function will then return that text the user has entered.

We take that text and reverse it. If the original text and reversed text are equal, then the text is a [palindrome](http://en.wiktionary.org/wiki/palindrome).

### Homework exercise

Checking whether a text is a palindrome should also ignore punctuation, spaces and case. For example, "Rise to vote, sir." is also a palindrome but our current program doesn't say it is. Can you improve the above program to recognize this palindrome?

If you need a hint, the idea is that...[^1]

## Files

You can open and use files for reading or writing by creating an object of the `file` class and using its `read`, `readline` or `write` methods appropriately to read from or write to the file. The ability to read or write to the file depends on the mode you have specified for the file opening. Then finally, when you are finished with the file, you call the `close` method to tell Python that we are done using the file.

Example (save as `io_using_file.py`):

<pre><code class="lang-python">{% include "./programs/io_using_file.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/io_using_file.txt" %}</code></pre>

**How It Works**

Note that we can create a new file object simply by using the `open` method.  We open (or create it if it doesn't already exist) this file by using the built-in `open` function and specifying the name of the file and the mode in which we want to open the file. The mode can be a read mode (`'r'`), write mode (`'w'`) or append mode (`'a'`). We can also specify whether we are reading, writing, or appending in text mode (`'t'`) or binary mode (`'b'`). There are actually many more modes available and `help(open)` will give you more details about them. By default, `open()` considers the file to be a 't'ext file and opens it in 'r'ead mode.

In our example, we first open/create the file in write text mode and use the `write` method of the file object to write  our string variable `poem` to the file and then we finally `close` the file.

Next, we open the same file again for reading. We don't need to specify a mode because 'read text file' is the default mode. We read in each line of the file using the `readline` method in a loop. This method returns a complete line including the newline character at the end of the line. When an _empty_ string is returned, it means that we have reached the end of the file and we 'break' out of the loop.

In the end, we finally `close` the file.

We can see from our `readline` output that this program has indeed written to and read from our new `poem.txt` file.

## Pickle

Python provides a standard module called `pickle` which you can use to store _any_ plain Python object in a file and then get it back later. This is called storing the object *persistently*.

Example (save as `io_pickle.py`):

<pre><code class="lang-python">{% include "./programs/io_pickle.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/io_pickle.txt" %}</code></pre>

**How It Works**

To store an object in a file, we have to first `open` the file in __w__rite __b__inary mode and then call the `dump` function of the `pickle` module. This process is called _pickling_.

Next, we retrieve the object using the `load` function of the `pickle` module which returns the object. This process is called _unpickling_.

## Unicode

So far, when we have been writing and using strings, or reading and writing to a file, we have used simple English characters only.  Both English and non-English characters can be represented in Unicode (please see the articles at the end of this section for more info), and Python 3 by default stores string variables (think of all that text we wrote using single or double or triple quotes) in Unicode.  

> NOTE: If you are using Python 2, and we want to be able to read and write other non-English languages, we need to use the `unicode` type, and it all starts with the character `u`, e.g. `u"hello world"`

```python
>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
```

When data is sent over the Internet, we need to send it in bytes... something your computer easily understands.  The rules for translating Unicode (which is what Python uses when it stores a string) to bytes is called encoding.  A popular encoding to use is UTF-8.  We can read and write in UTF-8 by using a simple keyword argument in our `open` function.

<pre><code class="lang-python">{% include "./programs/io_unicode.py" %}</code></pre>

**How It Works**

We use  io.open  and then use the `encoding` argument in the first open statement to encode the message, and then again in the second open statement when decoding the message.  Note that we should only use encoding in the open statement when in text mode.

Whenever we write a program that uses Unicode literals (by putting a `u` before the string) like we have used above, we have to make sure that Python itself is told that our program uses UTF-8, and we have to put  `# encoding=utf-8`  comment at the top of our program.  

You should learn more about this topic by reading:

- ["The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"](http://www.joelonsoftware.com/articles/Unicode.html)
- [Python Unicode Howto](http://docs.python.org/3/howto/unicode.html)
- [Pragmatic Unicode talk by Nat Batchelder](http://nedbatchelder.com/text/unipain.html)

## Summary

We have discussed various types of input/output, about file handling, about the pickle module and about Unicode.

Next, we will explore the concept of exceptions.

---

[^1]: Use a tuple (you can find a list of _all_ [punctuation marks here](http://grammar.ccc.commnet.edu/grammar/marks/marks.htm)) to hold all the forbidden characters, then use the membership test to determine whether a character should be removed or not, i.e. forbidden = (`!`, `?`, `.`, ...).
