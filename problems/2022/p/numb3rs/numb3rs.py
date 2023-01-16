import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split(".")

        for number in numbers:
            if int(number) > 255 or int(number) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
