"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
list_of_mods = ["Half_grip", "Side_grip", "Laser_sight", "Buckshot"]
print (list_of_mods)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
list_of_mods.append ("supressor")
#this allows me to add to the list
print (list_of_mods)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
list_of_mods.remove("Buckshot")
#this removes buckshot from the list
print(list_of_mods)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
list_of_mods[3] = "Flash muzzle"
#changes the third one on the lis to flash muzzle
print(list_of_mods)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
list_of_mods.append ("Extended barrel")
#you can only add one at a time so you have to put them in their on line of code
list_of_mods.append ("Armor pericing arounds")
list_of_mods.append ("Tracking rounds")
#added 3 new elements
print (list_of_mods)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del list_of_mods[5]
#this gets ride on the item on the index of 5
print(list_of_mods)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
list2 = list_of_mods [0:2]
print(list2)


"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""