some_text = input()
strength = 0
new_text = ''

for index in range(len(some_text)):
    if strength > 0 and some_text[index] != '>':
        strength -= 1
    elif some_text[index] == '>':
        new_text += some_text[index]
        strength += int(some_text[index + 1])
    else:
        new_text += some_text[index]
print(new_text)
