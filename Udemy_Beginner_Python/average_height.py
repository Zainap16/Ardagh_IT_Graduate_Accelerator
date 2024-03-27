student_heights = input("Ënter heights: ").split()
iCounter = 0
total_sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    iCounter += 1
    total_sum = total_sum + int(student_heights[n]) 
    average = round(total_sum / iCounter, 2)
    

print(f"average: {average}")
print(f"sum of heights: {total_sum}")
print(f"List of students: {student_heights}")


