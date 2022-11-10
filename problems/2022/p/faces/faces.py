def main():
    mood = input("How are you doing? ")
    convert(mood)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

main()