# def positive_nums(some_num):
#     return [num1 for num1 in some_num if int(num1) >= 0]
# def negative_nums(some_num):
#     return [num2 for num2 in some_num if int(num2) < 0]
# def even_nums(some_num):
#     return [num3 for num3 in some_num if int(num3) % 2 == 0]
# def odd_nums(some_num):
#     return [num4 for num4 in numbers if int(num4) % 2 != 0]
#
#
# numbers = input().split(', ')
# print(f"Positive: {', '.join(positive_nums(numbers))}")
# print(f"Negative: {', '.join(negative_nums(numbers))}")
# print(f"Even: {', '.join(even_nums(numbers))}")
# print(f"Odd: {', '.join(str(odd_nums(numbers)))}")

# positive_numbers = [num1 for num1 in numbers if num1 >= 0]
# negative_numbers = [num2 for num2 in numbers if num2 < 0]
# even_numbers = [num3 for num3 in numbers if num3 % 2 == 0]
# odd_numbers = [num4 for num4 in numbers if num4 % 2 != 0]

# # print(f'Positive: {', '.join(positive_numbers)}')
# print(''.join(positive_numbers))
# print(f'Negative: {negative_numbers}')
# print(f'Even: {even_numbers}')
# print(f'Odd: {odd_numbers}')
# # print(', '.join(str(positive_numbers)))


def positive_numbers(some_numbers):
    return [number for number in some_numbers if int(number) >= 0]


def negative_numbers(some_numbers):
    return [number for number in some_numbers if int(number) < 0]


def odd_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 != 0]


def even_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 == 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")
