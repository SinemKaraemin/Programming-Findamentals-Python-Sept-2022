string = input().split('\\')
second_string = string[-1].split('.')
print(f'File name: {second_string[0]}')
print(f'File extension: {second_string[1]}')
