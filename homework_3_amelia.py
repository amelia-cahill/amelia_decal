#1 Oski Stole Your Power
#Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
#a different way (by writing a function) that can compute x raised to the power
#of y.
#>>> x = 2
#>>> y = 3
#>>> computePower(x, y)
#8

def computePower(x,y):
    result=1
    for i in range(y):
        result=result*x
    return result

print(computePower(2,3))

#2: What Should I Wear?
#You are trying to decide what to wear to the Python DeCal lecture, but you
#are only concerned about the day’s lowest and highest temperatures. Write a
#function that takes in a list as input and returns a tuple with the min and max
#as two values.
#>>> readings = [15, 14, 17, 20, 23, 28, 20]
#>>> temperatureRange(readings)
#(14, 28)

def temperatureRange(readings):
    temperature_list = []
    temperature_list.append(min(readings))
    temperature_list.append(max(readings))
    tuple(temperature_list)
    print(temperature_list)
    return temperature_list

readings = [15, 14, 17, 20, 23, 28, 20]
temperatureRange(readings)

#3: Check if its the Weekend
#All your classes have assigned problem sets due next week, and you want to
#check if it’s the weekend so you have time to work on them. Write a function
#that takes a day of the week (represented as an integer, where 1 = Monday, 2
#= Tuesday, etc) and returns True if its a weekend and False if otherwise.
#>>> day = 6 # Saturday
#>>> isWeekend(day)
#True
#1

def isWeekend(day):
    isWeekend=False
    if day==6 or day==7:
        isWeekend=True
    return isWeekend

day = 6
print(isWeekend(day))

#4 Fuel Efficiency Calculator
#The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
#CA) and they want to pick the best car. Write a function that takes the distance
#traveled (in miles) and the amount of fuel consumed (in gallons) as input and
#returns the fuel efficiency.
#>>> distance = 70 # miles
#>>> fuel = 21.5 # gallons
#>>> fuel_efficiency(distance, fuel)
#3.26

def fuel_efficiency(distance,fuel):
    efficiency=distance/fuel
    return(round(efficiency, 2))

print(fuel_efficiency(70,21.5))

#5 Secret Code
#Write a function that takes an integer as input and moves its last digit to the
#front of the number. You may NOT convert the input to a string. Hint: Try
#modulus (%) and floor division. (\\) to solve this problem.
#>>> n = 12345
#>>> decodeNumbers(n)
#51234

def decodeNumbers(n):
    n_one=n%10
    n_two=n // 10
    temp=n
    while temp>10:
        n_one=n_one*10
        temp = temp/10
    return (n_one + n_two)

print(decodeNumbers(12345))

#6 Min & Max but with Loops!
#Oh no! Oski hacked you computer again... now you have lost the ability to use
#min() and max().
#6.1 For Loops
#Write two functions to manually find the minimum and maximum values in a
#list of numbers with for loops.
#>>> nums = [2024, 98, 131, 2, 3, 72]
#>>> find_min_with_for_loop(nums)
#2
#>>> find_max_with_for_loops(nums)
#2024

def find_min_with_for_loop(nums):
    min=nums[0]
    for i in nums:
        if i<min:
            min=i
    return min

nums = [2024, 98, 131, 2, 3, 72] 

print(find_min_with_for_loop(nums))

def find_max_with_for_loop(nums):
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
    return max

print(find_max_with_for_loop(nums))

#6.2 While Loops
#Write two functions to manually find the minimum and maximum values in a
#list of numbers with while loops.

def find_min_with_while_loop(num):
    temp_list=num.copy()
    min = temp_list[0]
    while len(temp_list)>0:
        i=temp_list[0]
        if i<min:
            min=i
        temp_list.pop(0)
    return min

print(find_min_with_while_loop(nums))

def find_max_with_while_loop(num):
    temp_list=num.copy()
    max = temp_list[0]
    while len(temp_list)>0:
        i=temp_list[0]
        if i>max:
            max=i
        del temp_list[0]
    return max
    
print(find_max_with_while_loop(nums))

#7 Counting Vowels
#Write a function that takes a string as an input and returns the number of vowels
#in the string and the number of consonants in the string as tuple. Don’t forget
#about capital letters! Hint: You can use .isalpha() to check if a character is
#a letter.
#>>> text = "UC Berkeley, founded in 1868!"
#>>> vowel_and_consonant_count(text)
#(4, 11)

def vowel_and_consonant_count(text):
    vowel_count=0
    consonant_count=0
    vowels=["a", "e", "i", "o", "u"]
    text=list(text.lower())
    for i in text:
        if i.isalpha():
            if i in(vowels):
                vowel_count=vowel_count+1
            else:
                consonant_count=consonant_count+1
    return vowel_count, consonant_count

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))

#8 Calculate Digital Root
#Write a function that takes an integer as an input and returns the sum of its
#digits.
#>>> num = 2468
#>>> digital_root(num)
#20

def digital_root(num):
    sum=0
    while num>0:
        sum=sum+num%10
        num=num//10
    return sum

num = 2468
print(digital_root(num))