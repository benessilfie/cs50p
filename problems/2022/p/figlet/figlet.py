import sys
from pyfiglet import Figlet
from random import choice

fg = Figlet()
fonts = fg.getFonts()


def main():
    if len(sys.argv) == 1:
        sys.exit(text_to_ascii())
    elif len(sys.argv) == 2 or sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    text_to_ascii(str(sys.argv[2]))


def text_to_ascii(f=choice(fonts)):
    text = input("Input: ")

    fg.setFont(font=f)
    ascii = fg.renderText(text)

    print(ascii)


main()

if "__name__" == "__main__":
    main()
