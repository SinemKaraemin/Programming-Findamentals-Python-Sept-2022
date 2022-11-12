list_of_numbers = list(map(int, input().split(' ')))
count_of_numbers_to_remove = int(input())

for element in range(count_of_numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
print(*list_of_numbers, sep=', ')
