## Define a function named *exponentiate* 
## Takes two integers as arguments.
## Returns the value of the first integer raised to the power of the second integer.

def exponentiate(val1, val2):
    return val1 ** val2

## Define a function named *raise_to_fourth_power
def raise_to_fourth_power(val1):
    val1**4
    return exponentiate(val1, 4)
    

# Create a variable called *square and cube*. The value assigned to this variable should be a lambda
square = lambda x: exponentiate(x, 2)
print(square(2))
cube = lambda x: exponentiate(x, 3)
print(cube(3))
print(raise_to_fourth_power(2))