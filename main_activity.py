'''
5 Enabling Assessment, three (3) Summative Assessment, Final Examination
'''
# Grade  = (ea_avg * 0.3) + (sa_avg * 0.3) + (final_exam * 0.4)

student_name = []
final_grade = []
letter_grade = []

for i in range(5):
    print("\n")
    print(f"[[Student {i+1}]] ")
    student_name.append(input("Enter the Student Name: "))

    # 5 Enabling Assessments
    enabling_asssessment = []
    for x in range(5):    
        enabling_asssessment.append(float(input(f"Enter Enabling Assessment {x+1} grade: ")))
    ea_avg = sum(enabling_asssessment) / len(enabling_asssessment)

    # 3 Summative Assessments
    summative_asssessment = []
    for y in range(3):    
        summative_asssessment.append(float(input(f"Enter Summatieve Assessment {y+1} grade: ")))
    sa_avg = sum(summative_asssessment) / len(summative_asssessment)
    
    # Final Examination
    final_exam = float(input("Enter Final Examination grade: "))

    # Final Grade
    final_grade.append((ea_avg * 0.3) + (sa_avg * 0.3) + (final_exam * 0.4))

    # Letter Grade 
    if final_grade[i] >= 90:
        letter_grade.append('A')
    elif final_grade[i] >= 80:
        letter_grade.append('B')
    elif final_grade[i] >= 70:
        letter_grade.append('C')
    elif final_grade[i] >= 60:
        letter_grade.append('D')
    else:
        letter_grade.append('F')

# Table output (not the cleanest code :<)
print("\n\n\n\n")
print('%-2s%-18s%-18s%-12s' % (" ","Student Name", "Average Grade", "Letter Grade"))
print("____________________________________________________")
for a in range(5):
    print('%-5s%-11s%-8s%-11s%-8s%-12s' % (" ", student_name[a], "|" ,round(final_grade[a], 1), "|", letter_grade[a]))