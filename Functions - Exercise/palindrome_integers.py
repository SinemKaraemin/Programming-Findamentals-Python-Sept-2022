def palindrome(number):
    return number == number[::-1]


list_of_positive_numbers = input().split(', ')
for number in list_of_positive_numbers:
    print(palindrome(number))
