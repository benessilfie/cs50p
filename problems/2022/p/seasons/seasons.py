from datetime import date
import sys
import inflect

flect = inflect.engine()


def main():
    birthday = input("Enter your birthday (yyyy-mm-dd): ")
    year, month, day = check_date_format(birthday)
    birthday = date(int(year), int(month), int(day))

    today = date.today()
    days = (today - birthday).days
    minutes = days * 24 * 60

    minutes_in_english = flect.number_to_words(minutes, andword="")
    print(f"{minutes_in_english.capitalize()} minutes")


def check_date_format(birthday):
    try:
        year, month, day = birthday.split("-")
        date(int(year), int(month), int(day))
        return year, month, day
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
