from random import randint as rand


def main():
    level = get_level()
    score = game(level)

    print(f"Your score is {score}")


def get_level() -> int:
    while True:
        try:
            level = int(input("Enter level: "))

            if level in [1, 2, 3]:
                break
        except:
            pass

    return level


def generate_integer(level) -> tuple:
    if level == 1:
        x = rand(0, 9)
        y = rand(0, 9)
    elif level == 2:
        x = rand(10, 99)
        y = rand(10, 99)
    else:
        x = rand(100, 999)
        y = rand(100, 999)

    return x, y


def generate_round(x, y) -> bool:
    tries = 1
    sum = x + y

    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == sum:
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")

    print(f"{x} + {y} = {sum}")
    return False


def game(level) -> int:
    round = 1
    score = 0

    while round <= 10:
        x, y = generate_integer(level)
        if generate_round(x, y):
            score += 1
        round += 1

    return score


if __name__ == "__main__":
    main()
