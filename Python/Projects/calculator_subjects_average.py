subjects = {}
# print("enter student name: ") input()
student_name = "Ziah" 
is_True = True
iCounter = 0
while is_True:
    
    key_subjects = input("Enter subject obtained: ")
    value_marks = int(input("Enter marks obtained(out of a 100): "))
    
    iCounter += 1
    
    subjects[key_subjects] = value_marks
    user_choice = input("press q-quit and a-add: ") 
    if user_choice.lower() == "q":
        is_True = False
        average = sum(subjects.values()) / iCounter
    else:
        continue
    
    #add a way for each subject to  
print(f"Dictionary: {subjects}")
print(f"Average: {average}")    


