lines = ['Alex: 30', 'Emma: 28', 'John: 25', 'Sarah: 22']

people = {}

for line in lines:
    parts = line.split(': ')
    people[parts[0]] = parts[1]

print(people.values())

