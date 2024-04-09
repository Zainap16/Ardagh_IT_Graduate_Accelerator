# myList = [1,2,3,4,5]
# [2*item for item in myList]

myList2 = list(range(100))
filtredList = [items for items in myList2 if items % 10 == 0]

print(filtredList)


#  select the items whose remainder after division by 10 is less than 3. This means we will get a list containing the numbers that end in 0, 1, or 2. Pretty neat, huh?
filtredList = [items for items in myList2 if items % 10 < 3]
print(filtredList)