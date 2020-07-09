
matrix = [
    [7, " ", 3],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"]
]
text = " "
invalid_char_count = 0


def is_valid(char):
    return type(char) is str and char.isalnum()


for col in range(3):
    for row in matrix:
        char = row[col]

        if is_valid(char):
            if invalid_char_count > 1:
                invalid_char_count = 0
                text += " "
            text += char
        else:
            invalid_char_count += 1

print(text)
