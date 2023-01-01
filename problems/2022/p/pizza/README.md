# Problem Set 6: Pizza Py

[![IMAGE_ALT](https://img.youtube.com/vi/TkABR72j7jU/maxresdefault.jpg)](https://youtu.be/TkABR72j7jU)

Perhaps the most popular place for pizza in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Pinocchio’s Pizza & Subs](https://www.pinocchiospizza.net), aka Noch’s, known for its [Sicilian pizza](https://www.pinocchiospizza.net/sicilian_vs_regular.html), which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its [menu](https://www.pinocchiospizza.net/menu.html) too, per this CSV file of Sicilian pizzas, [sicilian.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv), below:

```csv
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95
```

See [regular.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv) for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), like this one:

```asciiart
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
```

In a file called `pizza.py`, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using `tabulate`, a package on PyPI at [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Format the table using the library’s `grid` format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`.

## Hints

- Recall that the `csv` module comes with quite a few methods, per [docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html), among which are `reader`, per [docs.python.org/3/library/csv.html#csv.reader](https://docs.python.org/3/library/csv.html#csv.reader), and `DictReader`, per [docs.python.org/3/library/csv.html#csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).

- Note that `open` can `raise` a `FileNotFoundError`, per [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).

- Note that the `tabulate` package comes with just one function, per [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). You can install the package with:

```bash
pip install tabulate
```
