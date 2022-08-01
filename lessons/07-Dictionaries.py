"""
Dictionaries
- A dictionary is a collection of key-value pairs.
- A key is a unique identifier for a value.
- A value can be any Python object.
- A dictionary is mutable.
- A dictionary is unordered.
- It is denoted by {}
"""
person = ['John',32,'New York',['Python','C++']]
person = {  
    'name' : 'John',
    'age' : 32,
    'location' : 'New York',
    'favorites' : ['Python', 'C++', 'Java'],
    'preferences' : ('Python'),
}

print(person)

print(person['name'])

person['height'] = 100

print(person)

#number of items in the dictionary
print(len(person))

#remove a key-value pair
del person['age']

#change the name of this person
person['name'] = 'Jane'

print( person.items() )

print( person.get('name') )

person.pop('name')
print(person)

person.popitem()
print(person)

person.update({'name':'John','isMarried':False})
print(person)

# person.clear()

print( person.keys() )
print( person.values() )

newPerson = person.copy()

print(newPerson)

person.update({'age': 50})

print(person)
