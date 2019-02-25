# 파이썬 표준 라이브러리 {#stdlib}

파이썬 표준 라이브러리는 파이썬을 설치하면 기본적으로 제공되며, 여러가지 모듈이 포함되어 있습니다. 표준 라이브러리는 다양한 문제를 쉽고 빠르게 해결할 수 있게 해주는 모듈이 많이 포함되어 있기 때문에 표준 라이브러리를 많이 사용해보고 각 모듈이 어떤 기능을 제공하는지 꼼꼼히 확인하는 것이 매우 중요합니다.

이번 장에서는 표준 라이브러리에서 많이 사용되는 몇 가지 모듈에 대해 알아보도록 하겠습니다. 파이썬 표준 라이브러리에 포함되어 있는 모듈 목록을 확인하시려면 [파이썬 표준 라이브러리 문서](http://docs.python.org/3/library/)를 확인하시기 바랍니다.

> 아래의 내용이 너무 복잡하다고 생각하시면, 이번 장을 그냥 건너뛰셔도 괜찮습니다. 파이썬 프로그래밍에 어느 정도 익숙해졌다고 생각하시면 아래의 내용을 꼭 읽어주세요.

## `sys` module {#sys}

The `sys` module contains system-specific functionality. We have already seen that the `sys.argv` list contains the command-line arguments.

Suppose we want to check the version of the Python software being used, the `sys` module gives us that information.

<!-- The output should match pythonVersion variable in book.json -->
```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

**How It Works**

The `sys` module has a `version_info` tuple that gives us the version information. The first entry is the major version. We can pull out this information to use it.

## `logging` module {#logging}

What if you wanted to have some debugging messages or important messages to be stored somewhere so that you can check whether your program has been running as you would expect it? How do you "store somewhere" these messages? This can be achieved using the `logging` module.

Save as `stdlib_logging.py`:

<pre><code class="lang-python">{% include "./programs/stdlib_logging.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/stdlib_logging.txt" %}</code></pre>

The `cat` command is used in the command line to read the 'test.log' file.  If the `cat` command is not available, you can open the `test.log` file in a text editor instead.

**How It Works**

We use three modules from the standard library - the `os` module for interacting with the operating system, the `platform` module for information about the platform i.e. the operating system and the `logging` module to *log* information.

First, we check which operating system we are using by checking the string returned by `platform.platform()` (for more information, see `import platform; help(platform)`). If it is Windows, we figure out the home drive, the home folder and the filename where we want to store the information. Putting these three parts together, we get the full location of the file. For other platforms, we need to know just the home folder of the user and we get the full location of the file.

We use the `os.path.join()` function to put these three parts of the location together. The reason to use a special function rather than just adding the strings together is because this function will ensure the full location matches the format expected by the operating system.  Note: the `join()' method we use here that's part of the `os` module is different from the string method `join()` that we've used elsewhere in this book.

We configure the `logging` module to write all the messages in a particular format to the file we have specified.

Finally, we can put messages that are either meant for debugging, information, warning or even critical messages. Once the program has run, we can check this file and we will know what happened in the program, even though no information was displayed to the user running the program.

## Module of the Week Series {#motw}

There is much more to be explored in the standard library such as [debugging](http://docs.python.org/3/library/pdb.html),
[handling command line options](http://docs.python.org/3/library/argparse.html), [regular expressions](http://docs.python.org/3/library/re.html) and so on.

The best way to further explore the standard library is to read Doug Hellmann's excellent [Python Module of the Week](http://pymotw.com/2/contents.html) series (also available as a [book](http://amzn.com/0321767349)) and reading the [Python documentation](http://docs.python.org/3/).

## Summary

We have explored some of the functionality of many modules in the Python Standard Library. It is highly recommended to browse through the [Python Standard Library documentation](http://docs.python.org/3/library/) to get an idea of all the modules that are available.

Next, we will cover various aspects of Python that will make our tour of Python more _complete_.
