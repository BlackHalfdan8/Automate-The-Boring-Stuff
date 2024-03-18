def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")
        total_items += quantity
    print("Total number of items: " + str(total_items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Example inventory
player_inventory = {'gold coin': 42, 'rope': 1}

# Example loot
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Add loot to inventory
player_inventory = addToInventory(player_inventory, dragon_loot)

# Display inventory
displayInventory(player_inventory)
