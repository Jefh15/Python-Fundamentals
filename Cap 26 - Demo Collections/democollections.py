# Demo Collections

jesus = {}
jesus['first'] = 'Fonseca'
jesus['last'] = 'Hernandez'

aaron = {}
aaron['first'] = 'Fonseca'
aaron['last'] = 'Hernandez'

people = []
people.append(jesus)
people.append(aaron)
# Pass the list
people.append({
    'first': 'Bill',
    'last': 'Gates'
})
# print all lists
print(people)
