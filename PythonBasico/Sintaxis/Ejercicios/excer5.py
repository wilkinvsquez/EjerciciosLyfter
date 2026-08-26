grade_count = 1
current_grade = 0
approved_grades_quantity = 0
disapproved_grades_quantity = 0
approved_grades_avg = 0
disapproved_grades_avg = 0
total_grades_avg = 0

grades_total = input("Please enter the total number of grades to be evaluated: ")
while grade_count <= int(grades_total):
    current_grade = float(input(f"Please enter grade {grade_count}: "))
    if current_grade < 70:
        disapproved_grades_quantity += 1
        disapproved_grades_avg += current_grade
    else:
        approved_grades_quantity += 1
        approved_grades_avg += current_grade

    total_grades_avg = total_grades_avg + (current_grade / int(grades_total))
    grade_count += 1


if disapproved_grades_quantity > 0:
    disapproved_grades_avg = disapproved_grades_avg / disapproved_grades_quantity

if approved_grades_quantity > 0:
    approved_grades_avg = approved_grades_avg / approved_grades_quantity


print(f"\nThe student has approved : {approved_grades_quantity} grades.")
if approved_grades_quantity > 0:
    print(f"The average of approved grades is: {approved_grades_avg}")
else:
    print("There are no approved grades in this category.")

print(f"\nThe student has disapproved : {disapproved_grades_quantity} grades.")
if disapproved_grades_quantity > 0:
    print(f"The average of disapproved grades is: {disapproved_grades_avg}")
else:
    print("There are no disapproved grades in this category.")

print(f"\nThe average of all grades is: {total_grades_avg}")