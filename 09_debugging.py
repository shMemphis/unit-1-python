#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Determine whether the temperature is hot, temperate, or cold. 
temperature = 75

if temperature > 80:
    print("It's hot")
elif temperature > 50:
    print("It's temperate")
elif temperature < 0:
    print("It's cold")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Count how many spaces are in a given string
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Determine if numbers 1 to n are even or odd 
count = 0  
print(count)
print()

num = int(input("Give me a number: "))
for i in range(1, num):
    if i % 2 == 0:
        print(i, "is even.")
    else:
        print(i, "is odd.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculate the factorial of a given number
num = int(input("Enter an integer: "))
if num < 0:
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i   
    print("Factorial of " + str(num) + " is " + str(result))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Ask user to enter the correct password but only give them 3 attempts
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break  
    else:
        print("Incorrect password")

    if attempts >= 3:
        print("Too many attempts")
        break





from datetime import datetime
my_string ="07/22/2000"
my_date = datetime.strptime(my_string, "%m/%d%y")
print(my_date)