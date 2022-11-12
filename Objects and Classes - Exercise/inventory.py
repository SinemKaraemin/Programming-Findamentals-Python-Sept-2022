class Inventory:
    __capacity = 0
    items = []

    def __init__(self, capacity: int):
        Inventory.__capacity = capacity

    def add_item(self, item: str):
        if len(Inventory.items) < Inventory.__capacity:
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        left_capacity = Inventory.__capacity - len(Inventory.items)
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
