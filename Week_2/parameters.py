# def performOperation(num1,num2,operation='sum', message ='Default message'):
#     print(message)
#     if operation=='sum':
#         return num1+num2
#     if operation=='multiply':
#         return num1+num2
    
# performOperation(2,3,message='A new message', operation='multiply')

# args?
# default args : have default values ex-- def greet(name, age=18)
# variable-length args: define functions that can accept a variable number of args:

# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all(1, 2, 3, 4,5))  # Output: 10
#  They are collected into a tuple within the function. *args captures all positional arguments passed to the sum_all function and stores them in a tuple named args.


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
# **kwargs captures all keyword arguments passed to the display_info function and stores them in a dictionary named kwargs.