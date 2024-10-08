print ('Contact Book!')
print ('')
print ('')
Conbook = dict()
while 1:
    print('What would you like to do?')
    print("")
    print('1. Add a Number')
    print('2. View Numbers')
    print('3. Snap Away a Number')
    print('4. Burn It All!')
    print("")
    print('Enter one of one of the numbers above.')
    pick = int(input(""))
    print("")

    num = 1
    if pick == 2:
        for thing in Conbook:
            print()
            print("")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
    elif pick == 1:
        print('What Would you like to add?')
        add = input("")