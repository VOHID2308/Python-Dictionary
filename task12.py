inventory = {"olma": 10, "banan": 5}
product = input("Mahsulot nomini kiriting: ")

if product not in inventory:
    inventory[product] = 0

print(inventory)
