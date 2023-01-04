# Problem Set 7: Response Validation

When creating a [Google Form](https://www.google.com/forms/about/) that prompts users for a short answer (or paragraph), it’s possible to enable [response validation](https://support.google.com/docs/answer/3378864) and require that the user’s input match a [regular expression](https://support.google.com/a/answer/1371415). For instance, you could require that a user input an email address with a regex like [this one](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address):

```regex
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
```

Or you could more easily use Google’s built-in support for validating an email address, per the screenshot below, much like you could use a library in your own code:

![Image](https://cs50.harvard.edu/python/2022/psets/7/response/form.png)

In a file called `response.py`, using either [validator-collection](https://pypi.org/project/validator-collection/) or [validators](https://github.com/kvesteri/validators) from PyPI, implement a program that prompts the user for an email address via `input` and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. You may not use `re`. And do not validate whether the email address’s domain name actually exists.

## Hints

- Note that you can install validator-collection with:

```shell
pip install validator-collection
```

Click **Homepage** to find your way to the library’s documentation.

- Recall that regular expressions support quite a few special characters, per [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).

- Note that you can install validators with:

```shell
pip install validators
```

Click **Homepage** to find your way to the library’s documentation.
