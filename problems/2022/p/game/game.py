from random import randint as ri


def main():
    n = get_number()
    number = ri(1, n)
    guess(number)


def get_number() -> int:
    while True:
        try:
            level = int(input("Level: "))

            if level > 0:
                return int(level)
        except:
            pass


def guess(number: int) -> None:
    while True:
        guess = input("Guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess == number:
                print("Just right!")
                break
            elif guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")


if __name__ == "__main__":
    main()
