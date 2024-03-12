# 5! -->> 5 * 4 * 3  2 * 1 = 120
print('enter factorial number: ')
factorial_num = int(input())
if factorial_num >= 0: 
    counter = 0
    answer = 1
    while counter != factorial_num:
        counter += 1
        answer = answer * counter
        

    print('factorial of '+str(factorial_num)+' is '+str(answer))
else:
    print('Number must be more than 0 or 0')

    

