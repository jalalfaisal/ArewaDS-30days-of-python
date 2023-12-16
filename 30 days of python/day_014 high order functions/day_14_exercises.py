
#Level_0ne
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#question_1
#"map" means converting a series of inputs to an equal length series of outputs and Filter is a built-in function in Python. The filter function can be applied to an iterable such as a list or a dictionary and create a new iterator. while "reduce" means converting a series of inputs into a smaller number of outputs.They each take a function and a list of elements, and then return the result of applying the function to each element in the list. 
#question_2
#A higher-order function is a function that either takes a function as an argument or returns a function and Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.while a decorator really is simply a function that takes another function as an argument.
#question_3
#Call function for map:map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.).
#E.g sum_up=map(sum_arr,[1,2,3])
# print(list(sum_up))
#question_4
for i in countries:
    print(i)
#question_5
for i in names:
    print(i)
#question_6
for i in numbers:
    print(i)
#Level_two
#question_1
def upper(countries):
    return countries.upper()
    capitalize_countries=map(upper,countries)
    print(list(capitalize_countries))
#question_2
def square(numbers):
    return numbers**2
    squares_of_numbers=map(square,numbers)
    print(list(squares_of_numbers))
#question_3
def upper(names):
    return name.upper()
    capitalize_names=map(upper,names)
    print(list(capitalize_names))
#question_4
def land(countries):
    if 'land' in countries:
        return True
        return False
        print(list(filter(land,countries)))
#question_5
def six(countries):
    if len(countries)==6:
        return True 
        return False
        print(list(filter(six,countries)))
#question_6
def six_and_more(countries):
    if len(countries)>=6:
        return True 
        return False
        print(list(filter(six_and_more,countries)))
#question_7
def E(countries):
    if countries[0]=='E':
        return True 
        return False
        print(list(filter(E,countries)))
#question_9
def to_string(string):
    return str(string)
def get_string_lists(arr):
    return list(to_string,arr)
    print(get_string_lists(nunbers))
#question_10
numbers_string=[]
def add_two_numbers(x,y):
    return int(x)+int(y)
    total=reduce(add_two_numbers,numbers_string)
    print(total)
#question_11
def concatenate_countries(first_countries_list,second_countries_list):
    return f"{first_countries_list},{second_countries_list}"
    complete_list=reduce(concatenate_countries,countries)
    print(f"{complete_list} are north European countries.")
#question_12
def countries_dictionary(countries):
    dictionary={}
    for country in countries:
        if country[0] in dictionary:
            dictionary[country[0]]+=1
        else:
            dictionary[country[0]]=1
            return dictionary
            print(countries_dictionary(all_countries))
#question_13
def get_first_ten_countries(list):
    return list[:10]
    print(get_first_ten_countries(all_countries))
#question_14
def get_last_ten_countries(last):
    return list[-10:]
    print(get_last_ten_countries(all_countries))      #Level_three
def name(data):
    arr=[]
    for i in data:
        arr.append(i['name'])
        arr.sort()
        return arr
        print(name(data))
def capital(data):
   arr=[]
   for i in data:
       arr.append(i['capital'])
       arr.sort()
       return arr
       print(capital(data))
def population(data):
   arr=[]
   for i in data:
       arr.apend(i['population'])
       arr.sort()
       return arr
       print(population(data))
   