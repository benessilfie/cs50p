import sys
from csv import reader as rdr
from tabulate import tabulate as tab


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

menu = []

try:
    with open(sys.argv[1]) as file:
        reader = rdr(file)

        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")


print(tab(menu, headers="firstrow", tablefmt="grid"))
