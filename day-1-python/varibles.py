# Day 1 - variables

# variables

first_name = 'Sanjay'
last_name = 'Kumar'
country = 'India'
city = 'Chennai'
age = 324234
is_married = True
skills = ['Python','Html', 'CSS','JS']
personal_info = {
        'firstname':'Sanjay',
        'lastname':'Kumar',
        'country':'India',
        'city':'Chennai'
        }

# Printing the values
print('First name: ',first_name)
print('First name length: ',len(first_name))
print('Last name: ',last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', personal_info)

# Declaring multiple variables in one line


first_name, last_name, country, age, is_married = 'Sanjay', 'Kumar', 'India', 23430, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
