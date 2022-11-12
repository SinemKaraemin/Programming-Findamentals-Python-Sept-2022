first_String, second_string = input().split()
total_sum = 0

if len(first_String) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_String[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_String)):
        total_sum += ord(first_String[index])
elif len(second_string) > len(first_String):
    for index in range(len(first_String)):
        total_sum += ord(first_String[index]) * ord(second_string[index])
    for index in range(len(first_String), len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(len(second_string)):
        total_sum += ord(first_String[index]) * ord(second_string[index])
print(total_sum)
