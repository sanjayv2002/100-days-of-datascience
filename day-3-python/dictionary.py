# Day - 3 Dictionaries

# Creating a Dictionary
empty_dict = {}

person = {
    'first_name':'Sanjay',
    'last_name':'Kumar',
    'age':2341,
    'country':'India',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'JJR street',
        'zipcode':'600073'
        }
    }

# Dictionary Length
print(len(person))

# Accessing Dictionary Items
print(person['first_name']) 
print(person['country'])    
print(person['skills'])    
print(person['skills'][0])  
print(person['address']['street']) 
print(person['city'])    


#ALITER
print(person.get('first_name')) 
print(person.get('country'))    
print(person.get('skills'))
print(person.get('city'))

# Adding Items to a Dictionary
person['job_title'] = 'Student'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
person['skills'][1] = 'Python'

# Checking Keys in a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs from a Dictionary
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married'] 

# Changing Dictionary to a List of Items
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# Deleting a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
