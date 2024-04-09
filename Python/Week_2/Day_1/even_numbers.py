x = int(input("Enter range: "))

total = 0
if x == 100:
    for even in range(2, x + 1, 2):
        
        total += even
        # print(even)
else:
    for even in range(1, x + 1):
        total += even
         
         
       
    

print(f"even: {total}")
