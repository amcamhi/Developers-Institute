
text = " "
for col in range(3):
    for row in matrix:
        char = row[col]
        if type(char) is str and char.isalnum():
            text += char
        else:
            text += " "

finaltext = " "
