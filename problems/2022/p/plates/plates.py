def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0:2].isalpha() == False:
        return False

    if s.startswith("0"):
        return False

    for char in s[:-1]:
        if char in [".", " ", ",", "!", "?"]:
            return False
        elif char == "0":
            return False

    return True


main()
