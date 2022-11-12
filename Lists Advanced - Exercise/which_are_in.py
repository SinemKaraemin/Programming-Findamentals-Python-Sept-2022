text1 = input().split(', ')
text2 = input().split(', ')
lst = []

for word in text1:
    for word2 in text2:
        if word in word2:
            lst.append(word)
            break
print(lst)
