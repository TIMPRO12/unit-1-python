text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ": #there was no space in between the quotion
       count += 1

print(count)


print('++++++++++++++++++++++++')

print("give me a number")
n = int(input())

for num in range(1, n):
    if num % 2 < 0:
        print(num, "is odd.")
    else:
        print(num, "is even.")

print('++++++++++++++++++++++++')

num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + num + "is" + result)

print('++++++++++++++++++++++++')

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == "incorrect_password":
        print("Correct password!")
    else:
        print("Incorrect password")

    if attempts > 3:
        print("Too many attempts")
        break
