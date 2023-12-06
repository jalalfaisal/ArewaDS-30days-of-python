#Create an empty dictionary called dog
dog ={}
#Add name, color, breed, legs, age to the dog dictionary
dog ={ 'name': 'winter_dog', 'color': 'white', 'legs': 4, 'age': '8 month'

}
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dictionary = {
    "first_name": "Faisal",
    "last_name": "Muhammad Mustapha",
    "gender": "Male",
    "age": 27,
    "marital_status": "single",
    "skills": ["python", "R", ],
    "country": "Nigeria",
    "city": "Kaura Namoda",
    "address": "Hayin Mahe",
}
#Get the length of the student dictionary
print(len(student_dictionary))
#Get the value of skills and check the data type, it should be a list
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
#Modify the skills values by adding one or two skills
student_dictionary["skills"].append("sword_fighting")
#Get the dictionary keys as a list
list_keys = (list(student_dictionary.keys()))
#Get the dictionary values as a list
values = (list(student_dictionary.values()))
#Change the dictionary to a list of tuples using items() method
print(student_dictionary.items())
#Delete one of the items in the dictionary
student_dictionary.pop("age")
#Delete one of the dictionaries

del dog 