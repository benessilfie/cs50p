# Problem Set 5: Refueling

In a file called `fuel.py`, reimplement [Fuel Gauge](https://cs50.harvard.edu/python/2022/psets/3/fuel/) from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/), restructuring your code per the below, wherein:

* `convert` expects a `str` in `X/Y` format as input, wherein each of `X` and `Y` is an integer, and returns that fraction as a percentage rounded to the nearest int between `0` and `100`, inclusive. If `X` and/or `Y` is not an integer, or if `X` is greater than `Y`, then `convert` should raise a `ValueError`. If `Y` is `0`, then `convert` should raise a `ZeroDivisionError`.

* `gauge` expects an `int` and returns a `str` that is:

  * `"E"` if that `int` is less than or equal to `1`,
  * `"F"` if that `int` is greater than or equal to `99`,
  * and `"Z%"` otherwise, wherein `Z` is that same `int`.

```python
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_fuel.py`, implement **two or more** functions that collectively test your implementations of `convert` and `gauge` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```bash
pytest test_fuel.py
```

## Hints

* Be sure to include

```python
import fuel
```

or

```python
from fuel import convert, gauge
```

atop `test_fuel.py` so that you can call `covert` and `gauge` in your tests.

* Take care to `return`, not `print`, an `int` in `convert` and a `str` in `gauge`. Only `main` should call `print`

* Note that you can check with pytest whether a function has raised an exception, per [docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions](https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions).
