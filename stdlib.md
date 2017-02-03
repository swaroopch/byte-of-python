# Standard Library {#stdlib}

The Python Standard Library contains a huge number of useful modules and is part of every standard Python installation. It is important to become familiar with the Python Standard Library since many problems can be solved quickly if you are familiar with the range of things that these libraries can do.

We will explore some of the commonly used modules in this library. You can find complete details for all of the modules in the Python Standard Library in the ['Library Reference' section](http://docs.python.org/3/library/) of the documentation that comes with your Python installation.

Let us explore a few useful modules.

> CAUTION: If you find the topics in this chapter too advanced, you may skip this chapter. However, I highly recommend coming back to this chapter when you are more comfortable with programming using Python.

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

If you do not have the `cat` command, then you can just open the `test.log` file in a text editor.

**How It Works**

We use three modules from the standard library - the `os` module for interacting with the operating system, the `platform` module for information about the platform i.e. the operating system and the `logging` module to *log* information.

First, we check which operating system we are using by checking the string returned by `platform.platform()` (for more information, see `import platform; help(platform)`). If it is Windows, we figure out the home drive, the home folder and the filename where we want to store the information. Putting these three parts together, we get the full location of the file. For other platforms, we need to know just the home folder of the user and we get the full location of the file.

We use the `os.path.join()` function to put these three parts of the location together. The reason to use a special function rather than just adding the strings together is because this function will ensure the full location matches the format expected by the operating system.

We configure the `logging` module to write all the messages in a particular format to the file we have specified.

Finally, we can put messages that are either meant for debugging, information, warning or even critical messages. Once the program has run, we can check this file and we will know what happened in the program, even though no information was displayed to the user running the program.

## Module of the Week Series {#motw}

There is much more to be explored in the standard library such as [debugging](http://docs.python.org/3/library/pdb.html),
[handling command line options](http://docs.python.org/3/library/argparse.html), [regular expressions](http://docs.python.org/3/library/re.html) and so on.

The best way to further explore the standard library is to read Doug Hellmann's excellent [Python Module of the Week](http://pymotw.com/2/contents.html) series (also available as a [book](http://amzn.com/0321767349)) and reading the [Python documentation](http://docs.python.org/3/).

## Summary

We have explored some of the functionality of many modules in the Python Standard Library. It is highly recommended to browse through the [Python Standard Library documentation](http://docs.python.org/3/library/) to get an idea of all the modules that are available.

Next, we will cover various aspects of Python that will make our tour of Python more _complete_.
