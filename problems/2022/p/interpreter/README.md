# Problem Set 1: Math Interpreter

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables _users_ to do math, even without knowing Python.

In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:

- `x` is an integer
- `y` is `+`, `-`, `*`, or `/`
- `z` is an integer

## Hints

Recall that a `str` comes with quite a few methods, per the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`, which separates a `str` into a sequence of values, all of which can be assigned to variables at once. For instance, if `expression` is a `str` like `1 + 1`, then

```python
x, y, z = expression.split()
```

will assign `1` to `x`, `+` to `y`, and `1` to `z`.
