products_and_quantities = input().split()
bakery = {}

for i in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[i]
    value = products_and_quantities[i + 1]
    bakery[key] = int(value)

products_to_search_for = input().split()
for product in products_to_search_for:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
