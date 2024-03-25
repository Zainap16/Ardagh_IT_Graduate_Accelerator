# a number divisble by 3, Fizz
# a number divisble by 5, Buzz
# number disible by both 3 & 5, FizzBuzz
devisible_by_5=0
devisible_by_2 =0
for num in range(1,51):
    devisible_by_5 = num % 5
    devisible_by_2 = num % 3
    
    if devisible_by_5 == 0:
        print("Buzz")
    elif devisible_by_2 == 0:
        print("Fizz")
    elif (devisible_by_5 == 0 and devisible_by_2 == 0):
        print("FizzBuzz")
    else:
        print(num)





