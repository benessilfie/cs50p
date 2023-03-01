months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if date[0].isdigit():
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
        else:
            month, day, year = date.split()

            if len(day) == 1:
                raise ValueError

            month = months.index(month) + 1
            day = int(day.rstrip(","))

        if not (1 <= month <= 12) or not (1 <= day <= 31):
            continue
    except ValueError:
        continue
    break

print(f"{year}-{month:02}-{day:02}")
