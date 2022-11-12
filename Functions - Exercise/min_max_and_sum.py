def min_and_max_value(number):
    print(min(number))
    print(max(number))

def sum_of_all_numbers(num):
    return sum(num)


sequence_of_numbers = list(map(int, input().split(' ')))
result_of_sum = sum_of_all_numbers(sequence_of_numbers)
print(f"The minimum number is {min(sequence_of_numbers)}")
print(f"The maximum number is {max(sequence_of_numbers)}")
print(f"The sum number is: {result_of_sum}")

