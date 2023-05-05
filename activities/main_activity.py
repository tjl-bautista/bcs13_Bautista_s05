def calculate_grade (ea_avg, sa_avg, final_exam):
    return (ea_avg * 0.3) + (sa_avg * 0.3) + (final_exam * 0.4)

def calculate_letter (final_grade):
    if final_grade[i] >= 90:
        return 'A'
    elif final_grade[i] >= 80:
        return 'B'
    elif final_grade[i] >= 70:
        return 'C'
    elif final_grade[i] >= 60:
        return 'D'
    else:
        return 'F'
    
student_name = []
final_grade = []
letter_grade = []

for i in range(5):
    print(f"\n[[Student {i+1}]] ")
    student_name.append(input("Enter the Student Name: "))

    # 5 Enabling Assessments
    ea = []
    for x in range(5):    
        ea.append(float(input(f"Enter Enabling Assessment {x+1} grade: ")))
    ea_avg = sum(ea) / len(ea)
    
    # 3 Summative Assessments
    sa = []
    for y in range(3):    
        sa.append(float(input(f"Enter Summative Assessment {y+1} grade: ")))
    sa_avg = sum(sa) / len(sa)
    
    # Final Examination
    final_exam = float(input("Enter Final Examination grade: "))

    # Final Grade and Letter Grade
    final_grade.append(calculate_grade(ea_avg, sa_avg, final_exam))
    letter_grade.append(calculate_letter(final_grade))

# Table output (not the cleanest code :<)
print("\n\n\n\n")
print('%-2s%-18s%-18s%-12s' % (" ","Student Name", "Average Grade", "Letter Grade"))
print("____________________________________________________")
for a in range(5):
    print('%-5s%-11s%-8s%-11s%-8s%-12s' % (" ", student_name[a], "|" ,round(final_grade[a], 1), "|", letter_grade[a])) 