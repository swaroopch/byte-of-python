# 모듈

You have seen how you can reuse code in your program by defining functions once. What if you wanted to reuse a number of functions in other programs that you write? As you might have guessed, the answer is modules.

There are various methods of writing modules, but the simplest way is to create a file with a `.py` extension that contains functions and variables.

Another method is to write the modules in the native language in which the Python interpreter itself was written. For example, you can write modules in the [C programming language](http://docs.python.org/3/extending/) and when compiled, they can be used from your Python code when using the standard Python interpreter.

A module can be *imported* by another program to make use of its functionality. This is how we can use the Python standard library as well. First, we will see how to use the standard library modules.

Example (save as `module_using_sys.py`):

<pre><code class="lang-python">{% include "./programs/module_using_sys.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/module_using_sys.txt" %}</code></pre>

**How It Works**

First, we *import* the `sys` module using the `import` statement. Basically, this translates to us telling Python that we want to use this module. The `sys` module contains functionality related to the Python interpreter and its environment i.e. the **sys**tem.

When Python executes the `import sys` statement, it looks for the `sys` module. In this case, it is one of the built-in modules, and hence Python knows where to find it.

If it was not a compiled module i.e. a module written in Python, then the Python interpreter will search for it in the directories listed in its `sys.path` variable. If the module is found, then the statements in the body of that module are run and the module is made *available* for you to use. Note that the initialization is done only the *first* time that we import a module.

The `argv` variable in the `sys` module is accessed using the dotted notation i.e. `sys.argv`. It clearly indicates that this name is part of the `sys` module. Another advantage of this approach is that the name does not clash with any `argv` variable used in your program.

The `sys.argv` variable is a *list* of strings (lists are explained in detail in a [later chapter](./data_structures.md#data-structures)). Specifically, the `sys.argv` contains the list of *command line arguments* i.e. the arguments passed to your program using the command line.

If you are using an IDE to write and run these programs, look for a way to specify command line arguments to the program in the menus.

Here, when we execute `python module_using_sys.py we are arguments`, we run the module `module_using_sys.py` with the `python` command and the other things that follow are arguments passed to the program. Python stores the command line arguments in the `sys.argv` variable for us to use.

Remember, the name of the script running is always the first element in the `sys.argv` list. So, in this case we will have `'module_using_sys.py'` as `sys.argv[0]`, `'we'` as `sys.argv[1]`, `'are'` as `sys.argv[2]` and `'arguments'` as `sys.argv[3]`. Notice that Python starts counting from 0 and not 1.

The `sys.path` contains the list of directory names where modules are imported from. Observe that the first string in `sys.path` is empty - this empty string indicates that the current directory is also part of the `sys.path` which is same as the `PYTHONPATH` environment variable. This means that you can directly import modules located in the current directory. Otherwise, you will have to place your module in one of the directories listed in `sys.path`.

Note that the current directory is the directory from which the program is launched. Run `import os; print(os.getcwd())` to find out the current directory of your program.

## Byte-compiled .pyc files {#pyc}

Importing a module is a relatively costly affair, so Python does some tricks to make it faster. One way is to create *byte-compiled* files with the extension `.pyc` which is an intermediate form that Python transforms the program into (remember the [introduction section](./about_python.md#interpreted) on how Python works?). This `.pyc` file is useful when you import the module the next time from a different program - it will be much faster since a portion of the processing required in importing a module is already done. Also, these byte-compiled files are platform-independent.

NOTE: These `.pyc` files are usually created in the same directory as the corresponding `.py` files. If Python does not have permission to write to files in that directory, then the `.pyc` files will _not_ be created.

## The from..import statement {#from-import-statement}

If you want to directly import the `argv` variable into your program (to avoid typing the `sys.` everytime for it), then you can use the `from sys import argv` statement.

> WARNING: In general, *avoid* using the `from..import` statement, use the `import` statement instead. This is because your program will avoid name clashes and will be more readable.

Example:

```python
from math import sqrt
print("Square root of 16 is", sqrt(16))
```

## A module's `__name__` {#module-name}

Every module has a name and statements in a module can find out the name of their module. This is handy for the particular purpose of figuring out whether the module is being run standalone or being imported. As mentioned previously, when a module is imported for the first time, the code it contains gets executed. We can use this to make the module behave in different ways depending on whether it is being used by itself or being imported from another module. This can be achieved using the `__name__` attribute of the module.

Example (save as `module_using_name.py`):

<pre><code class="lang-python">{% include "./programs/module_using_name.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/module_using_name.txt" %}</code></pre>

**How It Works**

Every Python module has its `__name__` defined. If this is `'__main__'`, that implies that the module is being run standalone by the user and we can take appropriate actions.

## Making Your Own Modules

Creating your own modules is easy, you've been doing it all along!  This is because every Python program is also a module. You just have to make sure it has a `.py` extension. The following example should make it clear.

Example (save as `mymodule.py`):

<pre><code class="lang-python">{% include "./programs/mymodule.py" %}</code></pre>

The above was a sample *module*. As you can see, there is nothing particularly special about it compared to our usual Python program. We will next see how to use this module in our other Python programs.

Remember that the module should be placed either in the same directory as the program from which we import it, or in one of the directories listed in `sys.path`.

Another module (save as `mymodule_demo.py`):

<pre><code class="lang-python">{% include "./programs/mymodule_demo.py" %}</code></pre>

Output:

<pre><code>{% include "./programs/mymodule_demo.txt" %}</code></pre>

**How It Works**

Notice that we use the same dotted notation to access members of the module. Python makes good reuse of the same notation to give the distinctive 'Pythonic' feel to it so that we don't have to keep learning new ways to do things.

Here is a version utilising the `from..import` syntax (save as `mymodule_demo2.py`):

<pre><code class="lang-python">{% include "./programs/mymodule_demo2.py" %}</code></pre>

The output of `mymodule_demo2.py` is same as the output of `mymodule_demo.py`.

Notice that if there was already a `__version__` name declared in the module that imports mymodule, there would be a clash. This is also likely because it is common practice for each module to declare it's version number using this name. Hence, it is always recommended to prefer the `import` statement even though it might make your program a little longer.

You could also use:

```python
from mymodule import *
```

This will import all public names such as `say_hi` but would not import `__version__` because it starts with double underscores.

> WARNING: Remember that you should avoid using import-star, i.e. `from mymodule import *`.

<!-- -->

> **Zen of Python**
> 
> One of Python's guiding principles is that "Explicit is better than Implicit". Run `import this` in Python to learn more.

## The `dir` function {#dir-function}

The built-in `dir()` function returns the list of names defined by an object.
If the object is a module, this list includes functions, classes and variables, defined inside that module.

This function can accept arguments.
If the argument is the name of a module, the function returns the list of names from that specified module.
If there is no argument, the function returns the list of names from the current module.

Example:

```python
$ python
>>> import sys

# get names of attributes in sys module
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# only few entries shown here

# get names of attributes for current module
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

# create a new variable 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# delete/remove a name
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']
```

**How It Works**

First, we see the usage of `dir` on the imported `sys` module. We can see the huge list of attributes that it contains.

Next, we use the `dir` function without passing parameters to it. By default, it returns the list of attributes for the current module. Notice that the list of imported modules is also part of this list.

In order to observe `dir` in action, we define a new variable `a` and assign it a value and then check `dir` and we observe that there is an additional value in the list of the same name. We remove the variable/attribute of the current module using the `del` statement and the change is reflected again in the output of the `dir` function.

A note on `del`: This statement is used to *delete* a variable/name and after the statement has run, in this case `del a`, you can no longer access the variable `a` - it is as if it never existed before at all.

Note that the `dir()` function works on *any* object. For example, run `dir(str)` for the attributes of the `str` (string) class.

There is also a [`vars()`](http://docs.python.org/3/library/functions.html#vars) function which can potentially give you the attributes and their values, but it will not work for all cases.

## Packages

By now, you must have started observing the hierarchy of organizing your programs. Variables usually go inside functions. Functions and global variables usually go inside modules. What if you wanted to organize modules? That's where packages come into the picture.

Packages are just folders of modules with a special `__init__.py` file that indicates to Python that this folder is special because it contains Python modules.

Let's say you want to create a package called 'world' with subpackages 'asia', 'africa', etc. and these subpackages in turn contain modules like 'india', 'madagascar', etc.

This is how you would structure the folders:

```
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

Packages are just a convenience to organize modules hierarchically. You will see many instances of this in the [standard library](./stdlib.md#stdlib).

## Summary

Just like functions are reusable parts of programs, modules are reusable programs. Packages are another hierarchy to organize modules. The standard library that comes with Python is an example of such a set of packages and modules.

We have seen how to use these modules and create our own modules.

Next, we will learn about some interesting concepts called data structures.
