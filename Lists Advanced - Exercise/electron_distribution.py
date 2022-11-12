number_of_electrons = int(input())
filled_shells = []
enough_electrons = True
count_of_shell = 1

while enough_electrons:
    number_of_electrons -= 2 * (count_of_shell ** 2)
    filled_shells.append(2 * (count_of_shell ** 2))
    count_of_shell += 1
    if 2 * (count_of_shell ** 2) > number_of_electrons:
        filled_shells.append(number_of_electrons)
        enough_electrons = False
print(filled_shells)

