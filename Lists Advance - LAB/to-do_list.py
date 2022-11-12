to_do_list = []

while True:
    command = input()
    if command == 'End':
        break

    split_command = command.split('-')
    priority = int(split_command[0])
    current_command = split_command[1]

    to_do_list.append([priority, current_command])

    sorted_tasks = []
    for task_data in sorted(to_do_list):
        sorted_tasks.append(task_data[1])
print(sorted_tasks)

