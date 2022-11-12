food = input().split(' ')

# for word in food:
#     if len(word) % 2 == 0:
#         print(word)

new_food_list = [word for word in food if len(word) % 2 == 0]
print(''.join(new_food_list))