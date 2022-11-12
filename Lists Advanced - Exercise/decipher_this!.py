secret_message = input().split()

reveal = []

for word in secret_message:
    num_as_string = ''
    current_word = []
    for symbol in word:
        if symbol.isdigit():
            num_as_string += symbol
        else:
            current_word.append(symbol)
    num_as_digit = int(num_as_string)
    current_word.insert(0, chr(num_as_digit))
    if len(current_word) > 2:
        current_word[1], current_word[-1] = current_word[-1], current_word[1]
    reveal.append(''.join(current_word))
print(*reveal)
