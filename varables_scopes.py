# local - within an functions
# global - outside function
def my_function():
    x = 10  # Local variable
    print("Inside function:", x)

my_function()
# Output: Inside function: 10

# Trying to access x outside the function will result in an error
# print("Outside function:", x)  # This will raise a NameError
# Local Scope:

# Variables defined inside a function have a local scope.
# They can only be accessed within the function in which they are defined.
# Local variables are created when the function is called and destroyed when the function exits.
# They do not exist outside of the function's scope.


# Global Scope:

# Variables defined outside of any function or in the global scope have global scope.
# They can be accessed from anywhere in the code, including inside functions.
# Global variables persist throughout the program's execution
y = 20  # Global variable

def my_function():
    print("Inside function:", y)

my_function()
# Output: Inside function: 20

print("Outside function:", y)
# Output: Outside function: 20
# to motify a global variable,use the keyword global

z = 30  # Global variable

def modify_global():
    global z
    z += 5
    print("Inside function:", z)

modify_global()
# Output: Inside function: 35

print("Outside function:", z)
# Output: Outside function: 35
# __code__ --> access btyecode info, inspection code objection, 
# dynamic code analysis
def my_function(x):
    y = x + 1
    return y

code_object = my_function.__code__

print("Number of arguments:", code_object.co_argcount)
print("Variable names:", code_object.co_varnames)
print("Bytecode:", code_object.co_code)
