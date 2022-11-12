def extract_even_numbers(number):
    even_numbers = []
    for num in number:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


sequence_of_numbers = list(map(int, input().split(' ')))
print(extract_even_numbers(sequence_of_numbers))

