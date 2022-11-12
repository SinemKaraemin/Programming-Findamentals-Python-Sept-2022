def sorted_list(number):
    ascending_order = []
    for num in number:
        ascending_order.append(num)
        ascending_order.sort()
    return ascending_order


sequence_of_numbers = list(map(int, input().split(' ')))
print(sorted_list(sequence_of_numbers))
