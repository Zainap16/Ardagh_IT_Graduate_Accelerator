student_scores = input("Enter scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
   
highest_score = 0
   
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(max_nums)

print(highest_score)

# 78 65 89 86 55 91 64 89

