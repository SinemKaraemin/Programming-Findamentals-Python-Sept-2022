def is_palindrome(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()
all_palindromes = [word for word in words if is_palindrome(word)]
number_of_palindromes = all_palindromes.count(palindrome)


print(all_palindromes)
print(f"Found palindrome {number_of_palindromes} times")
