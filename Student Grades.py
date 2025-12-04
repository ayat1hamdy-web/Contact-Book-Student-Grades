# Task 2: Student Grades


# 1. إنشاء قائمة الطلاب
students = [
    {"name": "Ali", "grades": [85, 90, 88]},
    {"name": "Laila", "grades": [78, 82, 80]},
    {"name": "Omar", "grades": [92, 88, 94]}
]

# 2. حساب المتوسط وعرض النتائج
print("\nStudent Averages:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    
    # حساب المتوسط
    average = sum(grades) / len(grades)
    
    print(f"{name} - Average Grade: {average:.2f}")
