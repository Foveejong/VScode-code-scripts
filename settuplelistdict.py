#tuple -> immutable, ordered, duplicates
#list -> mutable, ordered, duplicates
#set -> mutable, unordered, no duplicates

courses = ['math', 'art', 'compsci', 'history']
courselist = '-'.join(courses)
listedcourse = courselist.split('-')
courses.append('english')
poppedcourse = courses.pop()
courses.insert(0, 'german')

#sets used to check if an element is inside the FASTEST
coursesset = {'math', 'art', 'compsci', 'history'}
"""print('math' in coursesset)"""

#remove duplicates
cs_courses = {'math', 'art', 'compsci', 'history', 'history', 'history'}
"""print(len(cs_courses)) """#returns 4 instead of 6

#set functions
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
"""print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))"""

#dictionaries
student = {'name': 'John', 'age': 25, 'courses': ['math', 'compsci']}
phone = student.get('phone', None)

#change <1 value at the same time
"""student.update({'name': 'Jane', 'phone': '555-555'})
print(phone)
print(student)"""

#ways to remove a key/value
"""del student['age']
age = student.pop('age')"""

stu_keys = student.keys()
stu_values = student.values()
stu_keysandvalues = student.items()
for k, v in student.items():
    print(k, v)
