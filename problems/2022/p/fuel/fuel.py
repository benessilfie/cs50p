def get_fuel_percentage(x, y):
    percentage = (x / y) * 100
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


while True:
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)

        if x > y or y == 0:
            raise ValueError

        print(get_fuel_percentage(x, y))
        break
    except (ValueError, ZeroDivisionError):
        pass
