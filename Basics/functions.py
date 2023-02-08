# define a basic function
def func1():
    print("I\'m function 1")

func1()
print(func1()) #runs fuction and prints return value of a function
print(func1) #prints value of function object

#function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

#function that returns a value
def cube(x):
    return x*x*x

func2(10,20)
print(func2(30,40))

print("cube root is ", cube(3))

# function with default value for argement
def power(num, x =1):
    result = 1
    for i in range(x):  # runs loop for ith time
        result = result * num
    return result

print(power(2)) # prints value with default value of x
print(power(2,3)) #prints value after changing default value by 3

#as long as you pass value of args by specifying name in python
# order of args in function call doesn't matter
print(power(x=3,num=2)) 

def multi_add(*args):  # *character allows multiple values to pass to a function at a time
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,19))