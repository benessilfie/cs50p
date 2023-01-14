import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    elif not sys.argv[1].endswith(sys.argv[2][sys.argv[2].rfind("."):]):
        sys.exit("Input and output have different extensions")

    image = sys.argv[1]
    after = sys.argv[2]

    convert_image(image, after)


def convert_image(image: str, after: str) -> None:
    try:
        before = Image.open(image)
    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    muppet = ImageOps.fit(before, size)
    muppet.paste(shirt, shirt)
    muppet.save(after)


if __name__ == "__main__":
    main()
