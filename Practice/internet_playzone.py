# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000, 'dog': "flappy"},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000, 'dog': "alex"},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000, 'dog': "Shoko"},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000, 'dog': "milky"},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')

# sort by dog name (Ascending order)
# casefold() method is sort by small chars and then big chars (at start if each string)
employees.sort(key=lambda x: (x.get('dog')).casefold())
print(employees, end='\n\n')
