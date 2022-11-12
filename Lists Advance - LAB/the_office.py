employees_happiness = input().split(' ')
factor = int(input())
employees_happiness = list(map(lambda x: int(x) * factor, employees_happiness)

filtration = list(filter(lambda x: x >= (sum(employees_happiness) / len(employees_happiness)), ))

if len(filtration) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtration)}/{len(employees_happiness)}. Employees are happy!")

else:
    print(f"Score: {len(filtration)}/{len(employees_happiness)}. Employees are not happy!")


