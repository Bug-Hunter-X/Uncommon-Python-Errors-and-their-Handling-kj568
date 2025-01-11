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

#Solution for FloatingPointError
import math

def function_with_floating_point_error(x):
    try:
        if x <= 0:
            print("Error: Input must be positive")
            return None
        result = math.log(x)
        return result
    except ValueError:
        print("Error: math domain error")
        return None

print(function_with_floating_point_error(1))
print(function_with_floating_point_error(-1)) #Output:Error message
print(function_with_floating_point_error(0)) #Output:Error message

#Solution for RecursionError using iteration:
def iterative_function(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
print(iterative_function(1000))

#Solution for improper library use
import numpy as np

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])

#Correct way of multiplication
result = np.multiply(array_a,array_b)
print(result) #Output [ 4 10 18]