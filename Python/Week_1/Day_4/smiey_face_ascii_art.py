# learn functions
# make a function called encode and a list
# in that list store user string
# value =0
# loop with the same char
# when char != char 
# value change to +1 and loop occurs again

# assuming that user enters 'aaaaabbbcc' == 5a3b2c
myString = input("enter code: ")

# def myEncode():
#     pass
value = 0
iCount = 0
my_encode = [] #list, changeable, square brackets,ordered lists
# puts myString into a list
char_count = {}

for char in myString:
    my_encode.append(char)
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
 
print(char_count)   
  
# set_list = set(my_encode)#set doesnt not contain duplicates
   
# for char2 in set_list:
#     if char2 in my_encode[iCount]:
#         value += 1
#     else: 
#         print(value)   
        
# print(my_encode)
# print(char)
# print(iCount)
# print(set_list)


