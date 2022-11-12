a_string = input().split(', ')

sum_list = []
for element in a_string:
    sum_list.append(int(element))

count_of_beggars = int(input())
final_sums = []
starting_index = 0
while starting_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(starting_index, len(sum_list), count_of_beggars):
        sum_of_current_beggar += sum_list[current_index]
    final_sums.append(sum_of_current_beggar)
    starting_index += 1
print(final_sums)
