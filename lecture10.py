productInventory = {
    'apple': 10,
    'banana': 20,
    'grape': 5,
    'orange': 15
}

# ACCESSING ITEMS IN A DICTIONARY
# quantityOfGrape = productInventory['grape']
# print(quantityOfGrape)

# quantityOfApples = productInventory.get('mango', 'not found')
# print(quantityOfApples)

# for fruit, num_of_fruit in productInventory.items():
#     print(f"Fruit: {fruit} Amount: {num_of_fruit}")

# fruits = productInventory.keys()
# for item in fruits:
#     print(item)

# amount = productInventory.values()
# print(amount)

# productInventory['mango'] = 42
# productInventory['cherry'] = 7
new_stock = {'mango': 23, 'cherry': 41, 'strawberry': 33}
productInventory.update(new_stock)
productInventory['apple'] = 20
productInventory['banana'] = 12
productInventory['cherry'] = 69
del productInventory['mango']
removed_item = productInventory.pop('apple')
removed_item2 = productInventory.popitem()
print(productInventory)
print(removed_item)
print(removed_item2)
