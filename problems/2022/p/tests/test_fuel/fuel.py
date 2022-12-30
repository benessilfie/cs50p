def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)


def convert(fraction) -> int:
    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            z = (x / y)

            if z <= 1:
                percentage = int(z * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
