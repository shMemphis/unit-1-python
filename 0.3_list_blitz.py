#Task 1: Create a list Create a list with 4 elements and print it.
chocolate = ["white","dark","milk","caramel"]
#Explanation: None needed
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Task 2: Add Element to a List Add an element to the end of the list. Print the updated  list.
chocolate.append("cacao")
print(chocolate)
#Explanation: I used append to add "cacao" to my list, then printed it.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 3: Remove Element from a List Remove a specific element from the list. Print the updated list.
del chocolate[4]
print(chocolate)
#Explanation:using the "del" i was able to remove the last item in my list.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 4: Modify Element in a List. Modify an element at a specific index with a new value. Print the updated list.
chocolate[2] = "aerated"
print(chocolate)
#Explanation:I used the "[]" to specifically modify my list.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 5: Append Multiple Elements to a List. Append multiple elements to the end of the list. Print the updated list.
chocolate.append("milk")
chocolate.append("raw")
print(chocolate)
#Explanation:I used the append to add more items to the list.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 6: Delete Element at a Specific Index. Delete an element at a specific index. Print the updated list.
del chocolate[4]
print(chocolate)
#Explanation:I used the "[]" to specifically remove the 5th item in my list.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 7: Subsetting lists Create a new variable equal to the first 2 items of your list Then print out the new variable
frosting = ["white","dark","strawberry","chocolate"]
print(frosting)
#Explanation:I made a new variable with the first 2 items in the list being the same.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Task 8: Extend a List Extend the list with the elements of another list. Print the updated list.
sweetstuff = chocolate + frosting
print(sweetstuff)
#Explanation: I made a new variable with both of my priors combined.