def collect_characters(first, second):
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters

character1 = input()
character2 = input()
result = collect_characters(character1, character2)
print(*result)
