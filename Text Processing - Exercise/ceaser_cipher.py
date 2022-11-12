text = input()
final_text = ''

for char in text:
    new_symbol = chr(ord(char) + 3)
    final_text += new_symbol
print(final_text)
