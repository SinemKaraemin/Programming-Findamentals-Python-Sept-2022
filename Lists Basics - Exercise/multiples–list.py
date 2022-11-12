factor = int(input())
count = int(input())
length_of_count = []

for multiplier in range(1, count+1):
    length_of_count.append(factor * multiplier)
print(length_of_count)