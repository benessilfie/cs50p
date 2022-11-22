# Problem Set 2: Just setting up my twttr

[just setting up my twttr](https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E20%7Ctwgr%5Ebcdec7b5181bd2fa8f00acfc164f57c44275a125%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Fcs50.harvard.edu%2Fpython%2F2022%2Fpsets%2F2%2Ftwttr%2F)

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called _twttr_. In a file called `twttr.py`, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

## Hints

- Recall that a `str` comes with quite a few methods, per the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- Much like a `list`, a `str` is "iterable", which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:

```python
    for c in s:
        print(c, end="")
```
