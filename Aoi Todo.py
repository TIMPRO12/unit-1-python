print ('To-do List!')
print ('')
print ('')
todo_list = []
with open('todo.txt') as file:
    contents = file.read()

while 1:
    print('What would you like to do?')
    print("")
    print('1. Add a Todo')
    print('2. View Task')
    print('3. Snap Away a Todo')
    print('4. Burn It All!')
    print("")
    print('Enter one of one of the numbers above.')
    pick = int(input(""))
    print("")

    num = 1
    if pick == 2:
        for thing in todo_list:     
            print(f"{num}){thing}")
            num += 1
        print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
    elif pick == 1:
        print('What Would you like to add?')
        add = input("")
        todo_list.append(add)
        print("")
        print(f"Added {add} To Your Todo List.")
        print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
    elif pick == 3:
        print('What Would You Like To Remove?')
        remove = input("")
        todo_list.remove(remove)
        print(f"Snapped {remove} From Your Todo List.")
        print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
    elif pick == 4:
        todo_list = []
        print('Your Todo list Is Burned')
    else:
        print('Nuh Uh.')
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

        with open('todo.txt', "r+") as file:
            contents = file.readlines()
        print(contents)
