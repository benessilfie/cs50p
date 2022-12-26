import emoji

input = input("Input: ")
print("Output: ", end="")
print(emoji.emojize(input, language="alias"))
