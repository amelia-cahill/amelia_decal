#1 Prime Clusters
#You have obtained a dataset of star temperatures from different stellar clusters.
#For your research, you are interested only in clusters where at least one star’s
#temperature is a prime number. Given a 2D NumPy array, write a function to
#find the rows where at least one value is a prime number. For example:
#>>> arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
#>>> containsPrimes(arr)
#array([[2, 3, 5],
#[11, 13, 17],
#[7, 10, 13]])

import numpy as np
import math

def containsPrimes(arr):
    contains_primes=False
    for row in arr:
        for number in row:
            if number <= 1:
                contains_primes=True
                print("hi")
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    contains_primes = False
                else:
                    contains_primes = True
        if contains_primes:
            print(row)

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
containsPrimes(arr)

#2.1
#Start by writing a function that creates a 8x8 square matrix with only zeros.
#>>> checkerboard()
#array([[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0]] )

def checkerboard():
    array = np.zeros((8, 8))
    return array

print(checkerboard())

#2.2
#For only the odd rows, make an alternating pattern of ones and zeroes.
#>>> checkerboard()
#array([[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 0, 0, 0, 0, 0, 0, 0]] )

def checkerboard():
    array = np.zeros((8, 8))  
    for row in range(1, len(array), 2):  
        for j in range(len(array[row])):  
            if j % 2 == 0:  
                array[row, j] = 1
    return array

print(checkerboard())

#2.3
#Finish the checkerboard with the even rows.
#>>> checkerboard()
#array([[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1]] )

def checkerboard():
    array = np.zeros((8, 8), dtype=int) 
    for row in range(len(array)): 
        for j in range(len(array[row])):  
            if (row + j) % 2 == 0: 
                array[row, j] = 1
    return array

print(checkerboard())

#2.4
#Re-write your function such that the checkerboard begins with a 0 instead.
#>>> reverse_checkerboard()
#array([[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0],
#[0, 1, 0, 1, 0, 1, 0, 1],
#[1, 0, 1, 0, 1, 0, 1, 0]] )

def reverse_checkerboard():
    array = np.zeros((8, 8), dtype=int)  # Create an 8x8 array of zeros
    for row in range(len(array)):  # Iterate over all rows
        for j in range(len(array[row])):  
            if (row + j) % 2 == 1:  # Shift pattern to start with 0
                array[row, j] = 1
    return array

print(reverse_checkerboard())

#3 The Expanding Universe
#You have now become fascinated with how dark energy is making galaxies ac-
#celerate away from us. Write a function that takes in a string and a number,
#and returns the string with the specified number of spaces inserted between each
#letter, simulating the expansion of space! For example:
#>>> universe = np.array([‘galaxy’, ’clusters’])
#>>> expansion(universe, 1)
#array([‘g a l a x y’, ‘c l u s t e r s’])
#>>> expansion(universe, 2)
#array([‘g a l a x y’, ‘c l u s t e r s’])

def expansion(arr, num):
    return_arr = []
    for word in arr:
        expanded_word = ""  
        for i in range(len(word)): 
            expanded_word += word[i] 
            if i != len(word) - 1: 
                for _ in range(num):
                    expanded_word += " "
        return_arr.append(expanded_word) 
    return return_arr

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 2))\

#4 Second-Dimmest Star
#While analyzing a dataset of star luminosities, you need to identify the second-
#dimmest star in each cluster. Write a function that takes a 2D NumPy array
#and returns an array containing only the second-smallest value in each column.
#For example:
#>>> np.random.seed(123)
#>>> stars = np.random.randint(500, 2000, (5, 5))
#array([[1123, 1456, 1789, 1324, 1876],
#[1567, 1987, 1678, 1405, 1589],
#[1345, 1654, 1523, 1109, 1923],
#[1298, 1890, 1367, 1784, 1432],
#[1823, 1756, 1489, 1672, 1550]])
#>>> secondDimmest(stars)
#array([1298, 1654, 1489, 1324, 1550])

def secondDimmest(stars):
    second_smallest = np.zeros(stars.shape[1], dtype=int)
    for col in range(stars.shape[1]):  
        smallest = float('inf')
        second = float('inf')
        for row in range(stars.shape[0]):  
            value = stars[row, col]
            if value < smallest:  
                second = smallest  
                smallest = value 
            elif smallest < value < second: 
                second = value 
        second_smallest[col] = second 
    return second_smallest

np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))
