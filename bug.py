def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

#Example Usage:
print(function_with_uncommon_error(10, 2)) # Output 5.0
print(function_with_uncommon_error(10, 0)) # Output Error: Division by zero, None
print(function_with_uncommon_error(10, "a")) # Output Error: Unsupported operand type(s) for /, None

#Uncommon Error: FloatingPointError
import math

def function_with_floating_point_error(x):
    try:
        result = math.log(x)
        return result
    except ValueError:
        print("Error: math domain error")
        return None

print(function_with_floating_point_error(-1)) # Output Error: math domain error, None
print(function_with_floating_point_error(0)) # Output Error: math domain error, None

#Another uncommon error: RecursionError
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n-1) + n

print(recursive_function(1000)) #Output: RecursionError

#Uncommon error due to improper use of libraries.
import numpy as np

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])

#Correct way of multiplication
result = np.multiply(array_a,array_b)
print(result) #Output [ 4 10 18]

#Incorrect way
#result = array_a*array_b
#print(result) #Output [ 4 10 18]