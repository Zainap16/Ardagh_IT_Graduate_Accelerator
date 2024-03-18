print('enter factorial number: ')
factorial_num = int(input())

num_1=0
num_2=0
sum=0
while num_1 != factorial_num:

    num_1 += 1
    num_2 += 1
    multi_ans = num_2 * num_1
    sum = sum + multi_ans
    
   
    print(str(num_2) +' * ' +str(num_1) + ' = '+ str(multi_ans))


print('Total: '+ str(sum))