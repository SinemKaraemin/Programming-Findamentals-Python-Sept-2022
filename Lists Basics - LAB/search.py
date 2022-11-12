number = int(input())
word = input()
lst = []
lst_with_the_given_word = []

for _ in range(number):
    strings = input()
    lst.append(strings)
    if word in strings:
        lst_with_the_given_word.append(strings)
print(lst)
print(lst_with_the_given_word)