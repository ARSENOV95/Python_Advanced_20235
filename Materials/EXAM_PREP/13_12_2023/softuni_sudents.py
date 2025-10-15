def softuni_students(*cridentials,**courses):
    courses_students = []
    invalid_courses = []
    result = ''

    for id,sturdent in cridentials:
        if id in courses.keys():
           courses_students.append((sturdent,courses[id])) 
        else:
            invalid_courses.append(sturdent)

    for name,course in sorted(courses_students,key = lambda x: x[0]):
        result += f"*** A student with the username {name} has successfully finished the course {course}!\n"

    if invalid_courses:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_courses))}"
    return result



print(softuni_students(('id_1', 'Kaloyan9905'),id_1='Python Web Framework',))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(softuni_students(('id_7', 'Silvester1'),('id_32', 'Katq21'),('id_7', 'The programmer'),id_76='Spring Fundamentals',id_7='Spring Advanced',))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(softuni_students(('id_22', 'Programmingkitten'),('id_11', 'MitkoTheDark'),('id_321', 'Bobosa253'),('id_08', 'KrasimirAtanasov'),('id_32', 'DaniBG'),id_321='HTML & CSS',id_22='Machine Learning',id_08='JS Advanced',))