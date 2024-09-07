students_count = int(input())

students = {}

for _ in range(students_count):
    student_name, grade = tuple(input().split())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(grade))

for key, value in students.items():
    average_grade = sum(students[key]) / len(students[key])

    print(f"{key} -> {' '.join(f'{i:.2f}' for i in value)} (avg: {average_grade:.2f})")