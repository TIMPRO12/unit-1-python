"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
password = "deepwoken"
entpass = input("put in password").lower()
#input for the password
if entpass == password:
    print("correct")
else:
    print("wrong password")


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
words = input("put some words in ;3")
words = words.strip()
#clears the whitespaces
if bool(words) == True:
    print("valid")
else:
    print ("invalid")



"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
pet1 = 'cat'
new_pet = pet1.replace('cat','dog')
#swaps cat for dog
print (new_pet)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
age = input("what is your age?")
print(age)
name = input("what is your name?")
print(name)



"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
float1 = (12.3)
float2 = (45.6)
answer = float1 / float2 

quotent = "f{float1} / {float2} = {answer:.1f}"

print(quotent)