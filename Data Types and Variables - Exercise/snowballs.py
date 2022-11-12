number_of_snowballs = int(input())
weight_of_the_snowball = int(input())
needed_time = int(input())
quality = int(input())

for current_snowball in range(number_of_snowballs):
    value = (weight_of_the_snowball / needed_time) ** quality
print(f"{weight_of_the_snowball} : {needed_time} = {int(value)} ({quality})")