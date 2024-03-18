import math
# def allPrimesUpTo(num):#2,3,5,7
#     i =1
#     for i in range(2,num+1):
#         square = i**0.5
#         prime = square % 2
#         if prime == 0:
#             print('Is a prime: '+ str(square))
#             # print(num)
#         else:
#             print('Is NOT prime: '+ str(square))    
        
# allPrimesUpTo(10)

def allPrimesUpTo(num):#2,3,5,7
    i =1
    for i in range(2,num+1):
        number = math.sqrt(i)
        prime = number % 2
        if prime == 0:
            print('is NOT a prime: '+str(i))
            
            # print(num)
        else:
            print('Is a prime: '+ str(i))  
            
        
allPrimesUpTo(10)

# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def allPrimesUpTo(num):
#     for i in range(2, num + 1):
#         if is_prime(i):
#             print('Is a prime:', i)
#         else:
#             print('is NOT a prime:', i)

# allPrimesUpTo(10)
