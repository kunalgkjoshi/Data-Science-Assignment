students = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8', 'student9',
            'student10']
marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]


def display_dash_board(students, marks):
    temp = []
    temp = marks.copy()
    temp.sort(reverse=True)
    top_5_students = temp[:5]
    temp.sort()
    least_5_students = temp[:5]
    students_within_25_and_75 = []
    for mark in marks:
        if mark > 25 and mark < 75:
            students_within_25_and_75.append(mark)

    return top_5_students, least_5_students, students_within_25_and_75


top_5_students, least_5_students, students_within_25_and_75 = display_dash_board(students, marks)

print("a.")
for ele in top_5_students:
    print(students[marks.index(ele)], ele)

print("b.")
for ele in least_5_students:
    print(students[marks.index(ele)], ele)

print("c.")
students_within_25_and_75.sort()
for ele in students_within_25_and_75:
    print(students[marks.index(ele)], ele)