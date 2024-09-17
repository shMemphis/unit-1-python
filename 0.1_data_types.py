#~~~~
#~~~~~~~
#~~~~~~~~~~
#TASK 1:Create a float variable, and then convert it to an integer Print both the original variable and the converted integer.
#~~~
#I turned my float to integer into its own variable.
fltoint = 22.2
integer_a = int(22.2)
print(integer_a)


#TASK 2:Write code that takes a number as input and prints whether it's positive, negative, or zero using if-elif-else statements.
#~~~~
#I made both the number and boolean its own variable, then I used the if else statement to determine and print whether or not the number is positive.
num1 = 3
boolnum = bool(num1)
print(boolnum)
if boolnum >= 1:
    print('its a positive number!')
else:
    print('Its negative...')


#TASK 3:Write code that takes two numbers as input (an integer and a float), performs addition, subtraction, multiplication, and division, and prints the results.
#~~~
#I labeled both the integer and float then coded the math.
dig1 = int(14)
dig2 = float(17.8)
print(dig1 + dig2)
print(dig1 - dig2)
print(dig1 * dig2)
print(dig1 / dig2)


#TASK 4:Create a dictionary with keys as fruit names and values as their respective quantities. Then print out the quantity of one of the fruits.
#~~~
#I made a dictionary then printed one of the fruits in my dictionary.
fruits = { 'Apples' : 3,
    'Oranges' : 5,
    'Grapes' : 10}
print(fruits)



#TASK 5:Create a string variable with that is a list of numbers and convert that string into a tuple.Then print out the both the original string and tuple.
#~~~
#I started by creating 2 variables one being the list converted into a tuple. Then I printed it
digis = "12345678"
tupis = tuple(digis)
print(digis)
print(tupis)