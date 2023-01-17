import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        if link := re.search(r"(?:http(?:s)*:\/\/(?:www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9_-]+)", s):
            return f"https://youtu.be/{link.group(1)}"


if __name__ == "__main__":
    main()
