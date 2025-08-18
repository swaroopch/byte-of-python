# Operators and Expressions {#op-exp}

Most statements (logical lines) that you write will contain _expressions_. A simple example of an expression is `2 + 3`. An expression can be broken down into operators and operands.

_Operators_ are functionality that do something and can be represented by symbols such as `+` or by special keywords. Operators require some data to operate on and such data is called _operands_. In this case, `2` and `3` are the operands.

## Operators

We will briefly take a look at the operators and their usage.

Note that you can evaluate the expressions given in the examples using the interpreter interactively. For example, to test the expression `2 + 3`, use the interactive Python interpreter prompt:

```python
>>> 2 + 3
5
>>> 3 * 5
15
>>>
```

Here is a quick overview of the available operators:

- `+` (plus)
    - Adds two objects
    - `3 + 5` gives `8`. `'a' + 'b'` gives `'ab'`.

- `-` (minus)
    - Gives the subtraction of one number from the other; if the first operand is absent it is assumed to be zero.
    - `-5.2` gives a negative number and `50 - 24` gives `26`.

- `*` (multiply)
    - Gives the multiplication of the two numbers or returns the string repeated that many times.
    - `2 * 3` gives `6`. `'la' * 3` gives `'lalala'`.

- `**` (power)
    - Returns x to the power of y
    - `3 ** 4` gives `81` (i.e. `3 * 3 * 3 * 3`)

- `/` (divide)
    - Divide x by y
    - `13 / 3` gives `4.333333333333333`

- `//` (divide and floor)
    - Divide x by y and round the answer _down_ to the nearest integer value. Note that if one of the values is a float, you'll get back a float.
    - `13 // 3` gives `4`
    - `-13 // 3` gives `-5`
    - `9//1.81` gives `4.0`

- `%` (modulo)
    - Returns the remainder of the division
    - `13 % 3` gives `1`. `-25.5 % 2.25` gives `1.5`.

- `<<` (left shift)
    - Shifts the bits of the number to the left by the number of bits specified. (Each number is represented in memory by bits or binary digits i.e. 0 and 1)
    - `2 << 2` gives `8`. `2` is represented by `10` in bits.
    - Left shifting by 2 bits gives `1000` which represents the decimal `8`.

- `>>` (right shift)
    - Shifts the bits of the number to the right by the number of bits specified.
    - `11 >> 1` gives `5`.
    - `11` is represented in bits by `1011` which when right shifted by 1 bit gives `101`which is the decimal `5`.

- `&` (bit-wise AND)
    - Bit-wise AND of the numbers: if both bits are `1`, the result is `1`. Otherwise, it's `0`.
    - `5 & 3` gives `1` (`0101 & 0011` gives `0001`)
    
- `|` (bit-wise OR)
    - Bitwise OR of the numbers: if both bits are `0`, the result is `0`. Otherwise, it's `1`. 
    - `5 | 3` gives `7` (`0101 | 0011` gives `0111`)
    
- `^` (bit-wise XOR) 
    - Bitwise XOR of the numbers: if both bits (`1 or 0`) are the same, the result is `0`. Otherwise, it's `1`.
    - `5 ^ 3` gives `6` (`O101 ^ 0011` gives `0110`)

- `~` (bit-wise invert)
    - The bit-wise inversion of x is -(x+1)
    - `~5` gives `-6`. More details at http://stackoverflow.com/a/11810203

- `<` (less than)
    - Returns whether x is less than y. All comparison operators return `True` or `False`. Note the capitalization of these names.
    - `5 < 3` gives `False` and `3 < 5` gives `True`.
    - Comparisons can be chained arbitrarily: `3 < 5 < 7` gives `True`.

- `>` (greater than)
    - Returns whether x is greater than y
    - `5 > 3` returns `True`. If both operands are numbers, they are first converted to a common type. Otherwise, it always returns `False`.

- `<=` (less than or equal to)
    - Returns whether x is less than or equal to y
    - `x = 3; y = 6; x <= y` returns `True`

- `>=` (greater than or equal to)
    - Returns whether x is greater than or equal to y
    - `x = 4; y = 3; x >= 3` returns `True`

- `==` (equal to)
    - Compares if the objects are equal
    - `x = 2; y = 2; x == y` returns `True`
    - `x = 'str'; y = 'stR'; x == y` returns `False`
    - `x = 'str'; y = 'str'; x == y` returns `True`

- `!=` (not equal to)
    - Compares if the objects are not equal
    - `x = 2; y = 3; x != y` returns `True`

- `not` (boolean NOT)
    - If x is `True`, it returns `False`. If x is `False`, it returns `True`.
    - `x = True; not x` returns `False`.

- `and` (boolean AND)
    - `x and y` returns `False` if x is `False`, else it returns evaluation of y
    - `x = False; y = True; x and y` returns `False` since x is False. In this case, Python will not evaluate y since it knows that the left hand side of the 'and' expression is `False` which implies that the whole expression will be `False` irrespective of the other values. This is called short-circuit evaluation.

- `or` (boolean OR)
    - If x is `True`, it returns True, else it returns evaluation of y
    - `x = True; y = False; x or y` returns `True`. Short-circuit evaluation applies here as well.

## Shortcut for math operation and assignment

It is common to run a math operation on a variable and then assign the result of the operation back to the variable, hence there is a shortcut for such expressions:

```python
a = 2
a = a * 3
```

can be written as:

```python
a = 2
a *= 3
```

Notice that `var = var operation expression` becomes `var operation= expression`.

## Evaluation Order

If you had an expression such as `2 + 3 * 4`, is the addition done first or the multiplication? Our high school maths tells us that the multiplication should be done first. This means that the multiplication operator has higher precedence than the addition operator.

The following table gives the precedence table for Python, from the lowest precedence (least binding) to the highest precedence (most binding). This means that in a given expression, Python will first evaluate the operators and expressions lower in the table before the ones listed higher in the table.

The following table, taken from the [Python reference manual](http://docs.python.org/3/reference/expressions.html#operator-precedence), is provided for the sake of completeness. It is far better to use parentheses to group operators and operands appropriately in order to explicitly specify the precedence. This makes the program more readable. See [Changing the Order of Evaluation](#changing-order-of-evaluation) below for details.

- `lambda` : Lambda Expression
- `if - else` : Conditional expression
- `or` : Boolean OR
- `and` : Boolean AND
- `not x` : Boolean NOT
- `in, not in, is, is not, <, <=, >, >=, !=, ==` : Comparisons, including membership tests and identity tests
- `|` : Bitwise OR
- `^` : Bitwise XOR
- `&` : Bitwise AND
- `<<, >>` : Shifts
- `+, -` : Addition and subtraction
- `*, /, //, %` : Multiplication, Division, Floor Division and Remainder
- `+x, -x, ~x` : Positive, Negative, bitwise NOT
- `**` : Exponentiation
- `x[index], x[index:index], x(arguments...), x.attribute` : Subscription, slicing, call, attribute reference
- `(expressions...), [expressions...], {key: value...}, {expressions...}` : Binding or tuple display, list display, dictionary display, set display

The operators which we have not already come across will be explained in later chapters.

Operators with the _same precedence_ are listed in the same row in the above table. For example, `+` and `-` have the same precedence.

## Changing the Order Of Evaluation {#changing-order-of-evaluation}

To make the expressions more readable, we can use parentheses. For example, `2 + (3 * 4)` is definitely easier to understand than `2 + 3 * 4` which requires knowledge of the operator precedences. As with everything else, the parentheses should be used reasonably (do not overdo it) and should not be redundant, as in `(2 + (3 * 4))`.

There is an additional advantage to using parentheses - it helps us to change the order of evaluation. For example, if you want addition to be evaluated before multiplication in an expression, then you can write something like `(2 + 3) * 4`.

## Associativity

Operators are usually associated from left to right. This means that operators with the same precedence are evaluated in a left to right manner. For example, `2 + 3 + 4` is evaluated as `(2 + 3) + 4`.

## Expressions

Example (save as `expression.py`):

```python
length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
```

Output:

```
$ python expression.py
Area is 10
Perimeter is 14
```

**How It Works**

The length and breadth of the rectangle are stored in variables by the same name. We use these to calculate the area and perimeter of the rectangle with the help of expressions. We store the result of the expression `length * breadth` in the variable `area` and then print it using the `print` function. In the second case, we directly use the value of the expression `2 * (length + breadth)` in the `print` function.

Also, notice how Python _pretty-prints_ the output. Even though we have not specified a space between `'Area is'` and the variable `area`, Python puts it for us so that we get a clean nice output and the program is much more readable this way (since we don't need to worry about spacing in the strings we use for output). This is an example of how Python makes life easy for the programmer.

## Summary

We have seen how to use operators, operands and expressions - these are the basic building blocks of any program. Next, we will see how to make use of these in our programs using statements.
