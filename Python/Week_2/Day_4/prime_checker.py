# def prime_check(n):
#     calc = n % 2
#     if n == 2:
#         print(f"{n} is a prime number")
#     elif calc != 0: 
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} NOT a prime number")

def prime_check(n):
    for i in range(2, n+1):
        if (i%2) != 0:
            print(f"{i} is a prime ")
        else:
            print(f"{i} NOT a prime number")
    
           

n = int(input("Enter a number: "))
prime_check(n)