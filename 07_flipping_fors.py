
#Exercise 1: Write a program to print each character of a given string using a for loop.
stuff = ('water', "snake", 'dogs', 'chocolate banana')
for x in stuff:
    print(x)
            #using the 'for' loop
#Exercise 2: Write a program to calculate the sum of elements in a list using a for loop.
lst = []
num = int(input('How many numbers: '))
                #asking how many numbers.
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
        #seeks the sum based off input.
print("Sum of elements in given list is :", sum(lst))
                #prints the input.
#Exercise 3: Write a program to print the length of each word in a sentence using a for loop and a list.
def word_lengths(phrase):
    return [f"{word} {len(word)}" for word in phrase.split()]

print(word_lengths("How long are the words in this phrase"))
#Excercise 4: Write a program that creates a dictionary (atleast 4 key:value pairs) and then iterates through a dictionary and prints the result
# Create a dictionary with at least 4 key-value pairs
my_dict = {
    "name": "Selah",
    "age": 40,
    "city": "New York",
    "occupation": "Him."
}

# Iterate through the dictionary and print each key and its value
for key, value in my_dict.items():
    print(f"{key}: {value}")

#In a comment, answer the following, what do you notice about the output of your code? Is it what you expected?
#I dont entirely notice anything signifgant.