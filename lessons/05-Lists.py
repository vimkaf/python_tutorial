"""
List
- It is denoted by []
- It is iterable
"""

shoppingList = ['Jam', 'Nutella', 'Kellogs', 'Mayonnaise', 'Salt', 'Sugar','Sugar']

print(shoppingList)

#print the first item in a list
print( shoppingList[0] )

#get the last item in a list
print ( shoppingList[-1] )

#get items from the 2:4
print ( shoppingList[2:4] )


#add item to a list
shoppingList.append('Butter')

print(shoppingList)

#add a new list to an existing list
bolaShoppingList = ['Lipstick', 'Pad']

#shoppingList.append(bolaShoppingList)

print(shoppingList + bolaShoppingList)
print( shoppingList.extend(bolaShoppingList) )

print(shoppingList)

#replace an item from a list
shoppingList[0] = "Crackers"
print(shoppingList)

shoppingList[1:3] = ["Nothing"]
print(shoppingList)

#insert item to a list
grades = ['A', 'B' , 'D' , 'E', 'F']
grades.insert(2, 'C')

#remove an item from a list
# print( shoppingList.pop() )
print( shoppingList.pop(0) )

print(shoppingList)

shoppingList.remove("Salt")
print(shoppingList)

#count the number of items in a list
print( len(shoppingList) )

#get the number of occurence an item appears in a list
print( shoppingList.count('Sugar') )

#copy by reference - the two lists refer to the same object of the first list
newShoppingList = shoppingList

shoppingList.append('Garri')
newShoppingList.append("Rice")

print(newShoppingList)
print(shoppingList)

#shallow copy - creates a new copy of a list
newShoppingList = shoppingList.copy()
newShoppingList.append('XMAS Chicken')
print(newShoppingList)
print(shoppingList)


#clear a list
# shoppingList.clear()
# shoppingList = []

#sorts a list
print("Before sort: ", shoppingList)
shoppingList.sort()

print("After sort: " ,shoppingList)

print("Before reverse sort: ", shoppingList)

shoppingList.sort(reverse=True)

print("After reverse sort: " ,shoppingList)

#reverse a list 
shoppingList.reverse()







