# key = hexNumbers.keys()

# for key in hexNumbers.keys():
#     print(key)
#integer_decimal = 0
# reversed_hex = ''.join(reversed(hexadecimal_user))
print('enter hexadecimal: ')

hexadecimal_user = input().upper() 

hexNumbers = {'0': 0, '1': 1 , '2': 2,'3': 3,'4' : 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'A': 10,'B':11,'C':12,'D':13,'E':14,'F':15}
result = 0
if len(hexadecimal_user) == 3:
    for char in hexadecimal_user:
        if char not in hexNumbers:
            print('invalid')
            break
        else:
            result = result * 16 + hexNumbers[char]
            
    else:
        print(result)

else:
    print('only 3 chaters')

