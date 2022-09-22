command=input()
num_of_coffees=0

while command!='END':
    if command.lower()=='coding' \
        or command.lower()=='dog' \
        or command.lower()=='cat' \
        or command.lower()=='movie':
        if command.islower():
            num_of_coffees+=1
        else:
            num_of_coffees+=2
    command=input()
if num_of_coffees>5:
    print("You need extra sleep")
else:
    print(num_of_coffees)