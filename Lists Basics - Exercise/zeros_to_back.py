a_string = input().split(', ')
if '0' in a_string:
    a_string.append(a_string.pop(a_string.index(0)))
print(list(a_string))
