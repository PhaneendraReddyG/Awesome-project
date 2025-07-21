marks_math = int(input("Enter the Math marks:"))
marks_science = int(input("Enter the science marks:"))
marks_english = int(input("Enter the english marks:"))

total_marks = marks_science+marks_english+marks_math

average = total_marks // 3
grade = ""
percentage = (total_marks/300)*100

if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <=90: 
    grade = "B"
elif percentage > 70 and percentage <= 80:
    grade = "C"

else:
    grade = "PASS"
print(f"Total marks:{total_marks},\nAverage_marks:{average},\nGrade={grade},\nPercent:{percentage}")