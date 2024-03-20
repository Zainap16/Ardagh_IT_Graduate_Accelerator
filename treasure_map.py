line1=["⬜","⬜","⬜"]
line2=["⬜","⬜","⬜"]
line3=["⬜","⬜","⬜"]

map = [line1,line2,line3]
print("Hidng your treasure! X marks the spot.")
position = input() # where do you want to put your treasure?

# B[columns]1[rows] [1][1]
column_entered = position[0].lower() 

#  A B C


abc = ["a","b","c"]
letter_index = abc.index(column_entered)
number_index = int(position[1]) - 1
# if row_entered == '1':
#     global row
#     row = 0
# elif row_entered == '2':
#     row = 1
# elif row_entered == '3':
#     row = 2
    
map[letter_index][number_index] = 'X'   

print(f"{line1}\n{line2}\n{line3}")







