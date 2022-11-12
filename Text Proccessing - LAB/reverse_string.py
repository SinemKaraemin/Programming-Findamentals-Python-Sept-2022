text = input()

while True:
    if text == 'end':
        break
    reversed_word = text[::-1]
    print(f"{text} = {reversed_word}")
    text = input()
