number_of_lines = int(input())
command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'

numbers = []

for _ in range(number_of_lines):
    current_num = int(input())
    numbers.append(current_num)
command = input()
filtered_nums = []

for number in numbers:
    filtered_passes = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_negative and number < 0) or
        (command == command_positive and number >= 0)
    )
    if filtered_passes:
        filtered_nums.append(number)
print(filtered_nums)