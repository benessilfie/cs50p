menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0

while True:
    try:
        order = input("Item: ").title()

        if order in menu:
            total_cost += menu[order]
            print(f"Total Cost: ${total_cost:.2f}")
    except (EOFError):
        print()
        break
