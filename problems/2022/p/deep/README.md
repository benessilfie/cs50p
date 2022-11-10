# Problem Set 1: Deep Thought

>“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable. <br>
>“You’re really not going to like it,” observed Deep Thought.<br>
>“Tell us!”<br>
>“All right,” said Deep Thought. “The Answer to the Great Question…”<br>
>“Yes…!”<br>
>“Of Life, the Universe and Everything…” said Deep Thought.<br>
>“Yes…!”<br>
>“Is…” said Deep Thought, and paused.<br>
>“Yes…!”<br>
>“Is…”<br>
>“Yes…!!!…?”<br>
>“Forty-two,” said Deep Thought, with infinite majesty and calm.”<br>
>
>_— The Hitchhiker’s Guide to the Galaxy, Douglas Adams_

In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output `No`.

## Hints

- No need to convert the user’s input to an `int` if you check for equality with `"42"`, a `str`, rather than `42`, an `int`!
- It’s okay if your output or the user’s wraps onto multiple lines.
