name = input("camelCase: ")
snake_case = ""

for char in name:
    if char.isupper():
        snake_case += f"_{char.lower()}"
    else:
        snake_case += char

print(snake_case)
