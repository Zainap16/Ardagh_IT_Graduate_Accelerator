# number of letters 
# symbols
# number ?
# randam of the above
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to PyPassowrd Generator!")
nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_num = int(input("How many numbers? "))

for letter in alphabet:
    char = random.randint(alphabet)
    
print(char)
    
