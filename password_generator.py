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

char_random = random.sample(alphabet, nr_letters)
  

symbols_random = random.sample(symbols, nr_letters)


num_random = random.sample(numbers, nr_letters)


addition_random =(char_random+ symbols_random+num_random)
extreme_random =random.shuffle(addition_random)
extreme_random_str = ''.join(extreme_random)
print(extreme_random_str)
    
