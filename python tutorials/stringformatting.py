person = {'name': 'John', 'age': 23}
# l = ['John', 23]
# sentence = f"my name is {person['name']} and I am {person['age']} years old"
# sentence = "my name is {0} and I am {1} years old".format(person['name'], person['age'])
# sentence = "my name is {0[0]} and I am {0[1]} years old".format(l)
# print(sentence)

# tag = 'h1'
# text = 'This is a headline'
# sentence = f'<{tag}>{text}</{tag}>'
# sentence = '<{0}>{1}</{0}>'.format(tag, text)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# p1 = Person("John", "23")
# sentence = f"my name is {p1.name} and I am {p1.age} years old"
# sentence = "my name is {name} and I am {age} years old".format(name="Jack", age=33)

# sentence = "my name is {name} and I am {age} years old".format(**person) -> unpacking dictionary (line 1)

for i in range(1, 11):
    # sentence = "The value is {:01}".format(i)
    sentence = f"The value is {i:02}" #colon means FORMATTING, 02 means 2 digits, if first digit empty (eg 1,2,3) fill with 0 -> 0 padding
    # print(sentence)
    
# k = 3.12345
# sent = f'k is {k:.2f}'
# print(sent)

# sent = f'1MB = {1000**2:,.2f}' # ->comma separated values AND 2 decimals
# print(sent)

import datetime
# my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
# sent = f'{my_date:%B %d, %Y}'

date = datetime.datetime(2023, 9, 24)
sent = f"{date: %B %d, %Y} fell on a {date:%A} and was the {date:%j} day of the year"
print(sent)