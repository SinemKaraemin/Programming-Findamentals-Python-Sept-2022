def group_of_10s(numbers):
    nums_to_10 = []
    for num in numbers:
        if num <=10 and num > 0:
            nums_to_10.append(num)
    return nums_to_10

def group_of_20s(numbers):
    nums_to_20 = []
    for num in numbers:
        if num <=20 and num >= 11:
            nums_to_20.append(num)
    return nums_to_20

def group_of_30s(numbers):
    nums_to_30 = []
    for num in numbers:
        if num <=30 and num >= 21:
            nums_to_30.append(num)
    return nums_to_30

def group_of_40s(numbers):
    nums_to_40 = []
    for num in numbers:
        if num <=40 and num >= 31:
            nums_to_40.append(num)
    return nums_to_40

def group_of_50s(numbers):
    nums_to_50 = []
    for num in numbers:
        if num <=50 and num >= 41:
            nums_to_50.append(num)
    return nums_to_50



sequence_of_numbers = list(map(int, input().split(', ')))
print(f'Group of 10\'s: {group_of_10s(sequence_of_numbers)}')
print(f'Group of 20\'s: {group_of_20s(sequence_of_numbers)}')
print(f'Group of 30\'s: {group_of_30s(sequence_of_numbers)}')
print(f'Group of 40\'s: {group_of_40s(sequence_of_numbers)}')
print(f'Group of 50\'s: {group_of_50s(sequence_of_numbers)}')
