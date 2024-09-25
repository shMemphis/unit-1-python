#Exercise 1: Write a program to print numbers from 1 to 10 using a for loop.
for number in range(1, 11):
    print(number)
                # Print numbers from 1 to 10 using a for loop

#Exercise 2: Write a program to count by 10s from 900 to 1000

for number in range(900, 1001, 10):
    print(number)
                # Count by base 10's from 900 to 1000
#Exercise 3: Write a program that counts form 1-100 by 9
for number in range(1, 101, 9):
    print(number)
                # I count from 1 to 100 by 9s
#Exercise 4: Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
# make a variable to hold the sum
total_sum = 0

# find the sum of numbers from 1 to 10 using a for loop
for number in range(1, 11):
    total_sum += number  # Add the current number to the total sum
print("The sum of numbers from 1 to 10 is:", total_sum)
# Print

#Excercise 5: Uncomment the following code and run it. Then answer the following: What is the ouput of the code?

#Explain the iterative process that this code executes to get that output
rows = 5
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
#This process creates a christmas tree or ramp pattern of asterisks.