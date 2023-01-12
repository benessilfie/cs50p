import sys
from csv import DictReader, DictWriter


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Could not read invalid_file.csv")

    csv_file = sys.argv[1]
    file_name = sys.argv[2]
    clean_csv_file = clean_csv(csv_file)

    write_csv(clean_csv_file, file_name)


def clean_csv(csv_file: str) -> list[dict[str, str]]:
    students = []

    try:
        with open(csv_file) as file:
            reader = DictReader(file)

            for row in reader:
                last_name, first_name = row["name"].split(",")
                house = row["house"]
                students.append(
                    {"first": first_name.lstrip(), "last": last_name, "house": house})

            return students
    except FileNotFoundError:
        sys.exit("File does not exist")


def write_csv(clean_csv: list[dict[str, str]], file_name: str) -> None:

    with open(file_name, "w") as file:
        writer = DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()
        for row in clean_csv:
            writer.writerow(row)


if __name__ == "__main__":
    main()
