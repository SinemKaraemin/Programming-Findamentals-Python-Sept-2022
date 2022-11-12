orders = {}

while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split(' ')
    if name not in orders:
        orders[name] = [float(price), int(quantity)]
    else:
        orders[name][0] = float(price)
        orders[name][1] += int(quantity)

for name in orders:
   total_price = orders[name][0] * orders[name][1]
   print(f"{name} -> {total_price:.2f}")
