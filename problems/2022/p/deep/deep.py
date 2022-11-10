name = input("What is the Answer to the Great Question of Life? ").lower().strip()

match name:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")