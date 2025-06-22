num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print(f"\n--- Enter details for Student {i+1} ---")
    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")
    marks1 = float(input("Enter marks of English: "))
    marks2 = float(input("Enter marks of Urdu: "))
    marks3 = float(input("Enter marks of Math: "))
    total = marks1 + marks2 + marks3
    percentage = (total / 300) * 100
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Roll No: {roll_no}")
    print(f"Total Marks: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
