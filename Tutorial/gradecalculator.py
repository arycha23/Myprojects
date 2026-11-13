grade:int = []

while(True):
    grade_entered = input("Enter grade: ")

    if (grade_entered == "done"):
        break
    elif (grade_entered.isdigit()):
        grade.append(float(grade_entered))

average_grade = sum(grade) / len(grade)
print(average_grade)