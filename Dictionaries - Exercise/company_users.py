company = {}

while True:
    command = input()
    if command == 'End':
        break
    company_name, employees_id = command.split(' -> ')
    if company_name not in company:
        company[company_name] = []
    if employees_id not in company[company_name]:
        company[company_name].append(employees_id)

ordered_info = sorted(company.items())
for company_name, users in ordered_info:
    print(f"{company_name}")
    for id in users:
        print(f'-- {id}')