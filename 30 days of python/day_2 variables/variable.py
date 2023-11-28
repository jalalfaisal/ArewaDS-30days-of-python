
# Variables in Python

first_name = 'rahma'
last_name = 'lyse'
country = 'kazakhstan'
city = 'bukhara'
age = 19
year = 2019
is_married = True
is_true = True
skills = [ 'React', 'Python']
personal_info = {
    'firstname':'rahma', 
    'lastname':'lyse', 
    'country':'kazakhstan',
    'city':'bukhara'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('year:' , year)
print('Married: ', is_married)
print('True: ', is_true)
print('Skills: ', skills)
print('Person information: ', personal_info)

# Declaring multiple variables in one linE

first_name, last_name, country, age, is_married = 'rahma', 'lyse', 'kazakhstan', 19, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('year:' , year)
print('Married: ', is_married)
print('True: ', is_true)
print('Skills: ', skills)
print('Person information: ', personal_info)