string = input()

for idx in range(len(string)):
    if string[idx] == ':':
        print(f':{string[idx + 1]}')
