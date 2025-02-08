print(type(0.1))

x=7 #global variables
y=2
print(x+y)
print(type(x))

my_list = [1,2,3,4]
print(type(my_list))

my_dictionary= {'cookies': ['oreo','chocolate chip'], 'cake': ['red velvet', 'chocolate']}

print(type(my_dictionary))

print(5%2)

def pwr(x,y):
    '''this function raises the first input to the power of the second input'''
    x=2 #local variables, cant be called outside
    y=4
    exp=x ** y
    return exp

print(pwr(x,y))

def mult(a,b):
    m=a*b
    return m

print(mult(x,y))