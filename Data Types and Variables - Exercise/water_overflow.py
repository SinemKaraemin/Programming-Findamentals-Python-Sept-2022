number_of_lines = int(input())
tank_capacity = 255
sum = 0

for current_liters in range(number_of_lines):
    liters_of_water = int(input())

    if tank_capacity-liters_of_water<0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    sum += liters_of_water

print(sum)
