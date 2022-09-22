string = input()
string = string.lower()
total=0

for word in ['water','sand','fish','sun']:
    number_of_occurences = string.count(word)
    total+=number_of_occurences
print(total)