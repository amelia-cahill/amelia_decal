#1. You have been plopped into this directory system. What command will
#tell you what your working directory is?
#The command that will tell me what my working directory is is "pwd".

#2. The command tells you ∼/python decal/judy decal. What command
#with list all the files in your current working directory?
#The command that will list all the files in my current working directory is "ls"

#3. Brianna just sent out an announcement that there was a typo on homework.py.
#So you need to pull the updates. What commands will let you move to
##the correct repository and pull the latest changes?
#I would need to enter "cd .." then "cd brianna_repo" then "git fetch origin"

#. How would you move this new homework.py to your personal repository
#homework directory?
#I would enter "mv ∼/python decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework"

#5. You want to see the contents of the homework.py in your terminal from
#your personal repository. What command(s) will let you do this?
#"cd ..", "cd judy_decal", "cd homework", "open homework.py"

#6. You want to edit the contents of the homework.py in your terminal from
#your personal repository. What command will let you do this?
#"nano homework.py"

#7. You have finished the homework. What commands will allow you to save
#the changes and push from your local repository to your remote repository?
#"git add homework.py"
#"git commit -m "adding homework""
#"git push origin main"

#8. Oh no! Git gave you the following error. What commands should you call
#to resolve this error and push your homework properly? What does the
#error mean? (i.e. what did ”Judy” do wrong?)
#! [rejected] main -> main (fetch first)
#error: failed to push some refs to ’https://github.com
#/judy/judy_decal.git’
#hint: Updates were rejected because the remote contains
#work that you do
#hint: not have locally. This is usually caused by another
#repository pushing
#hint: to the same ref. You may want to first integrate
#the remote changes
#hint: (e.g., ’git pull ...’) before pushing again.
#hint: See the ’Note about fast-forwards’ in ’git push
#--help’ for details.

#The issue is that the remote repository does not match Judy's local one and it needs to be updated before changes can be pushed.
#Update with "git fetch origin"
#"git merge origin"
#Then push again "git push origin main"

#9. What absolute path will allow you to move to Recents/?
#cd /home/user/Recents

#2.1 Data Types
#Write a function that takes any input and returns a string indicating its data
#type.
#>>> checkDataType(3.14)
#‘float’
#>>> checkDataType(True)
#‘bool’
def checkDataType(data):
    print(type(data))
    return type(data)

checkDataType(3.14)
checkDataType(True)

#2.2 Conditionals
#Write a function that takes an integer as input and returns ’Even’ if the integer
#is even, and ’Odd’ otherwise.
#>>> evenOrOdd(7)
#’Odd’
#>>> evenOrOdd(10)
#’Even’

def evenOrOdd(num):
    if num%2==0:
        return("Even")
    else:
        return("Odd")
    
print(evenOrOdd(7))
print(evenOrOdd(10))

#3 Loops
#Write a function that takes a list of integers and returns their sum using a loop
#(do NOT use the built-in sum() function).
#>>> numbers = [1, 2, 3, 4, 5]
#>>> sumWithLoop(numbers)
#15
def sumWithLoop(list):
    sum=0
    for i in list:
        sum+=i
    return sum
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

#4 HW4 Review: Lists
#4.1 Lists
#Write a function that takes a list and returns a new list with each element
#duplicated.
#>>> duplicateList([‘a’, ‘b’, ‘c’])
#[‘a’, ‘a’, ‘b’, ‘b’, ‘c’, ‘c’]

def duplicateList(list):
    new_list=[]
    for i in list:
        for j in range(2):
            new_list.append(i)
    return new_list

print(duplicateList(['a', 'b', 'c']))

#4.2 Debugging
#There’s an error in the following function that’s supposed to return the square
#of a number. Find and correct it:
#def square(num)
#return num * num

'''The error is there is no colon after the definition statement.'''
def square(num):
    return num*num

print(square(3))