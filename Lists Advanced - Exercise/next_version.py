version_of_software = [int(number) for number in input().split('.')]
version_of_software[-1] += 1

for index in range(len(version_of_software) - 1, -1, -1):
    if version_of_software[index] > 9:
        version_of_software[index] = 0
        if index - 1 >= 0:
            version_of_software[index - 1] += 1
print('.'.join(str(number) for number in version_of_software))

