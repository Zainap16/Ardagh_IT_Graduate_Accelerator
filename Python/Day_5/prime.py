def allPrimesUpTo(num):#2,3,5,7
    i =1
    for i in range(2,num+1):
        square = i**0.5
        prime = square % 2
        if prime == 0:
            print('Is a prime: '+ str(square))
            # print(num)
        else:
            print('Is NOT prime: '+ str(square))    
        
allPrimesUpTo(10)