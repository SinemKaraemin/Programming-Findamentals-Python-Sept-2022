string = input()
digits = []
letters = []
other_characters = []

for character in string:
    if character.isdigit():
        digits.append(character)
    elif character.isalpha():
        letters.append(character)
    else:
        other_characters.append(character)

print(''.join(digits))
print(''.join(letters))
print(''.join(other_characters))
