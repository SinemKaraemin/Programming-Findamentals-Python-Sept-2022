operator = input()
number_1 = int(input())
number_2 = int(input())

def solve(operator,number_1,number_2):
    if operator == 'subtract':
        return number_1 - number_2
    elif operator == 'divide':
        return number_1 / number_2
    elif operator == 'add':
        return number_1 + number_2
    elif operator == 'multiply':
        return number_1 * number_2
print(int(solve(operator,number_1,number_2)))
