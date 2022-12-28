import inflect

flec = inflect.engine()

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

print(f"Adieu, adieu, to {flec.join(names)}")
