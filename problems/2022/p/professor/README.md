# Problem Set 4: Little Professor

[![IMAGE_ALT](https://img.youtube.com/vi/ZuJwzH9BIgs/maxresdefault.jpg)](https://www.youtube.com/watch?v=ZuJwzH9BIgs&t=2s)

One of David’s first toys as a child, funny enough, was [Little Professor](https://en.wikipedia.org/wiki/Little_Professor), a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display `4 + 0 = `, David would (hopefully) answer with 4. If the toy were to display `4 + 1 = `, David would (hopefully) answer with `5`. If David were to answer incorrectly, the toy would display `EEE`. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., `4 + 0 = 4` or `4 + 1 = 5`).

In a file called `professor.py`, implement a program that:

- Prompts the user for a level, $\ n$. If the user does not input `1`, `2`, or `3`, the program should prompt again.

- Randomly generates ten (10) math problems formatted as `X + Y = `, wherein each of `X` and `Y` is a non-negative integer with $\ n$ digits. No need to support operations other than addition (`+`).

- Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.

- The program should ultimately output the user’s score, a number out of 10.

Structure your program as follows, wherein `get_level` prompts (and, if need be, re-prompts) the user for a level and returns `1`, `2`, or `3`, and `generate_integer` returns a randomly generated non-negative integer with `level` digits or raises a `ValueError` if `level` is not `1`, `2`, or `3`:

```python
import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
```

## Hints

- Note that you can raise an exception like `ValueError` with code like:

```python
raise ValueError
```

- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).
