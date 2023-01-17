import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if check_format := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([AaPp][Mm]) to (([0-9][0-2]*):*([0-5][0-9])*) ([AaPp][Mm])$", s):
        formats = check_format.groups()
        if int(formats[1]) > 12 or int(formats[5]) > 12:
            raise ValueError()
        first_hour = convert_to_24h(formats[1], formats[2], formats[3])
        second_hour = convert_to_24h(formats[5], formats[6], formats[7])
        return f"{first_hour} to {second_hour}"
    else:
        raise ValueError()


def convert_to_24h(hour, minute, meridiem):
    if meridiem == "AM":
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    elif meridiem == "PM":
        if int(hour) == 12:
            new_hour = int(hour)
        else:
            new_hour = int(hour) + 12

    if minute == None:
        new_minute = ":00"
        time = f"{new_hour:02}{new_minute}"
    else:
        time = f"{new_hour:02}:{minute}"

    return time


if __name__ == "__main__":
    main()
