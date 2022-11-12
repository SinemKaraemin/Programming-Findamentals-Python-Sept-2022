def total_price(product_type, quantity_of_the_product):
    if product_type == 'coffee':
        return quantity_of_the_product * 1.50
    elif product_type == 'coke':
        return quantity_of_the_product * 1.40
    elif product_type == 'water':
        return quantity_of_the_product * 1.00
    elif product_type == 'snacks':
        return quantity_of_the_product * 2.00


product = input()
quantity = int(input())
print(f'{total_price(product, quantity):.2f}')
