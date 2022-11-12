number = int(input())
positive_lst = []
negative_lst = []
counter = 0
sum_of_negatives = 0

for _ in range(number):
    current_number = int(input())
    if current_number >= 0:
        positive_lst.append(current_number)
        counter += 1
    else:
        negative_lst.append(current_number)
        sum_of_negatives += current_number
print(positive_lst)
print(negative_lst)
print(f'Count of positives: {counter}')
print(f'Sum of negatives: {sum_of_negatives}')