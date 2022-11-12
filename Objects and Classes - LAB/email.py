from email_class import Email

emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    sender, receiver, content = command.split(' ')
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(', ')]

for email in emails:
    print(email.get_info())
