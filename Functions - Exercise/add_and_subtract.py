def sum_numbers(number1, number2):
    return number1 + number2
def subtract(sum_of_number1_and_2, number3):
    return sum_of_number1_and_2 - number3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result_of_sum = sum_numbers(num_1, num_2)
result_of_subtract = result_of_sum - num_3
print(result_of_subtract)
