# lambda functions
'''
Lambda functions, also known as anonymous functions, are small, inline functions that are defined using the lambda keyword in Python. They are used for simple, one-line operations where defining a full function using def would be overly verbose. Lambda functions can take any number of arguments but can only have a single expression.

'''

# Regular Expression
# def square(x):
#     return x * x

# print(square(5))

# square_lambda = lambda x:x*x
# print(square_lambda(5))
# practice exercise

'''

random package -->> between 0 & 1 [float_num] 


'''

# def getWithRetry(dataFunc):
#     time.sleep(1)
#     if getData50() != '50%':
#         getData50()

import random
import time

servicesAreUp = True

float_num = random.uniform(0,1)

def getData50():
    if servicesAreUp and float_num < 0.5:
        return '50%'
    else:
        None
    
def getData25():
    if servicesAreUp and float_num < 0.25:
        return '25%'
    else:
        None

def getData10():
    if servicesAreUp and float_num < 0.1:
        return '10%'
    else:
        None

# if not 50, then retry until 50%

def getWithRetry(dataFunc):
    time.sleep(1)
    i = 0
    for i in range(5):
        value = getData50()
        if value == '50%':
            return '50%_retry'
        else:
            return None




print(getData50())
print(getWithRetry(getData50()))

