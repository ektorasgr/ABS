#returns a dictionary with addeditems added to the player's inventory

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(str(addedItems[i]), 0)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1

    return inventory


#display the inventory. a function from inventory.py
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + inventory.get(k,0)
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
