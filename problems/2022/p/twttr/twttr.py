tweet = input("Input: ")

print(f"Output: ", end="")

for char in tweet:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        print("", end="")
    else:
        print(char, end="")

print("")
