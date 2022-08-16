teachers = [
    {"id": 5, "full_name": "jack&jones"},
    {"id": 6, "full_name": "jack&jones"},
]

students = [{"id": 4, "full_name": "jonse","cources": [{"id": 6, "title": "math", "unit": 3}]}]
courses = [{"id": 6, "title": "math", "unit": 3, "teachers": [{"id": 5, "full_name": "jack&jones"}]}]
for item in [{"id": 9, "title": "ytj", "unit": 2}, {"id": 12, "title": "gfg", "unit": 3},
             {"id": 14, "title": "ass", "unit": 3}]:
    courses.append(item)
print(courses)


# for item in [{"id": 10, "full_name": "zare"}, {"id": 7, "fu
# ll_name": "pezu"}, {"id": 8, "full_name": "larens"}]:
#     teachers.append(item)
#
# courses.append([{"id": 7, "title": "literachur", "unit": 4, "teachers": [{"id": 7, "full_name": "jackson"}]}])

def add_student(student, course_ids):
    student["courses"] = list(filter(lambda x: x["id"] in course_ids, courses))
    print(student)


# def add_course(course, teacher_ids):
#     result_teachers = []
#     for teacher in teachers:
#         if teacher["id"] in teacher_ids:
#             result_teachers.append(teacher)
#
#     course["teachers"] = list(filter(lambda x: x["id"] in teacher_ids, teachers))
#     print(course)
#
#     print()
#     pass

def main():
    add_student({"id": 4, "full_name": "jonse", "courses": []}, [9, 12, 14])

if __name__ == '__main__':
    main()
