string = input()
last_letter = ''
final_text = ''

for character in string:
    if character != last_letter:
        final_text += character
        last_letter = character
print(final_text)
