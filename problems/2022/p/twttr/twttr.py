def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word) -> str:
    shorten = ""

    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            shorten += ""
        else:
            shorten += char

    return shorten


if __name__ == "__main__":
    main()
