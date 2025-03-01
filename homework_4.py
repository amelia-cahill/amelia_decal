#1 Debugging
#As you work through this problem set, whenever you encounter an error, please
#include a comment explaining what the error was and how you later resolved it.
#You can add these explanations at any relevant place in the file. Example:
#>>> print("Hello, World!")
#>>> """
#>>> I encountered the following eror: "SyntaxError: unterminated
#>>> string literal (detected at line 1) when I wrote
#>>> print("Hello, World!)". So I added the missing " at the end
#>>> and the code printed it successfully.
#>>> """

#2.1 Making a List Variable
#Create a variable (name it anything you want, but make it descriptive!) that
#is assigned to a list with numbers 0 through 20. You should not write each
#number manually.
#>>> whateverNameYouWant = # Your code here
#>>> print(whateverNameYouWant)
#[0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list

list_of_1_through_20 = []
for i in range(21):
    list_of_1_through_20.append(i)
print(list_of_1_through_20)

"""
Line 23 I encourentered the error: line 23, in <module>
    list_of_1_through_20+=1
TypeError: 'int' object is not iterable
This was because I forgot to use append instead of adding.
"""

#2.2 Working with List Elements
#Write a function that will take in your list from Part 2.1 and square each element
#in the list. Assign the result to a new variable.
#>>> whateverNameYouWant = # Your code from Part 2.1
#>>>
#>>> def squareList():
#>>> # Your code here
#>>>
#>>> anotherNameYouWant = squareList(list)
#>>> print(anotherNameYouWant)
#[0, 1, 4, ..., 400]

def squareList(list):
    list_1_through_20_squared = []
    for i in list:
        i=i*i
        list_1_through_20_squared.append(i)
    return list_1_through_20_squared

squared_list = squareList(list_of_1_through_20)
print(squared_list)

"""
For this function I first got the error "squared_list = squareList(list_of_1_through_20)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: squareList() takes 0 positional arguments but 1 was given"
This was because I forgot to allow the function to take in a list, so it read squareList()
"""

#2.3 Slicing
#Write a function that takes in your new list from Part 2.2 and returns the first
#15 elements of the list using slicing.
#>>> anotherNameYouWant = squareList(list)
#>>> first_fifteen_elements(anotherNameYouWant)
#[0, 1, 4, ..., 196]

def first_fifteen_elements(squared_list):
    sliced_first_fifteen_list = squared_list[0:15]
    return sliced_first_fifteen_list

first_fifteen = first_fifteen_elements(squared_list)
print(first_fifteen)

#2.4 Striding
#Write a function that takes in your list from Part 2.2 and returns every 5th
#element from the list using striding.
#>>> anotherNameYouWant = squareList(list)
#>>> every_fifth_element(anotherNameYouWant)
#[16, 81, 196, 361]

def every_fifth_element(squared_list):
    print(squared_list)
    striding_list = squared_list[4::5]
    return striding_list

every_fifth_element = every_fifth_element(squared_list)
print(every_fifth_element)

#2.5 Slicing & Striding
#Write a function that takes your list from Part 2.2, slices the last 3 elements of
#the list, and then returns every 3rd element from that list in reverse order.
#>>> anotherNameYouWant = squareList(list)
#>>> fancy_function(anotherNameYouWant)
#[400, 289, 196, 121, 64, 25, 4]

def every_third_in_reverse(squared_list):
    every_third=squared_list[2::3]
    every_third.reverse()
    return every_third

print(every_third_in_reverse(squared_list))

#3 2D lists
#3.1 Creating a 5x5 2D List
#Write a function that uses nested for loops to create a 5x5 2D list where the
#numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
#able.
#>>> matrix = create_2d_list()
#>>> print(matrix)
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
#[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

def create_2d_list():
    num=0
    matrix=[]
    for i in range (5):
        temp_matrix=[]
        for i in range(5):
            num+=1
            temp_matrix.append(num)
        matrix.append(temp_matrix)
    return matrix

two_d_list=create_2d_list()
print(two_d_list)

#3.2 Replacing 2D List with Multiples of 3
#With the 2D list you created in Part 3.1, write a function that will replace all
#multiples of 3 with the character “?”.
#>>> matrix = create_2d_list()
#>>> modified_2d_list(matrix)
#[[1, 2, ‘?’, 4, 5],
#[‘?’, 7, 8, ‘?’, 10],
#[11, ‘?’, 13, 14, ‘?’],
#[16, 17, ‘?’, 19, 20],
#[‘?’, 22, 23, ‘?’, 25]]

def modified_2d_list(matrix):
    for i in matrix:
        for j in range(len(i)):
            if i[j]%3==0:
                i[j]='?'
    return matrix

modified_list=modified_2d_list(two_d_list)
print(modified_list)

#3.3 Summing None-’ ?’ Elements
#Assign the result of your function from Part 3.2 to a variable. Write a function
#that will iterate through the new 2D list variable and return the sum of all the
#elements that are not “?”. Hint: Try using “!=”.
#>>> matrix = create_2d_list()
#>>> new_matrix = modified_2d_list(matrix)
#>>> sum_non_question_elements(new_matrix)
#217

def sum_not_question_elements(matrix):
    sum=0
    for j in matrix:
        #print(j)
        for i in j:
            #print(i)
            if i != "?":
                sum+=i
    return sum

print(sum_not_question_elements(modified_list))

'''
For this problem I got the error "Traceback (most recent call last):
  File "/Users/ameliacahill/python_decal/amelia_decal/homework_4.py", line 169, in <module>
    print(sum_not_question_elements(modified_list))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ameliacahill/python_decal/amelia_decal/homework_4.py", line 165, in sum_not_question_elements
    if matrix[i] != "?":
       ~~~~~~^^^
TypeError: list indices must be integers or slices, not str"
This error occured because "i" in the function above is already an element within one list of the 2d list, its not the index of an element.
'''