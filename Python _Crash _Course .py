#8-1
def display_message(title):
    message = "One of my favorite books is " + title + "."
    print(message)


#8-2
    def favorite_book(title):
    message = f"One of my favorite books is {title}."
    print(message)

#8-3
    def make_shirt(size, message):
    shirt_info = f"I have a {size} shirt with the message '{message}' printed on it."
    print(shirt_info)

#8-4
    def make_shirt(size='large', message='I love Python'):
    shirt = {
        'size': size,
        'message': message,
    }
    return shirt
# to create the shirts
shirt1 = make_shirt() # Large shirt with default message
shirt2 = make_shirt('medium') # Medium shirt with default message
shirt3 = make_shirt(size='small', message='Hello World') # Small shirt with custom message


#8-5
def describe_city(city, country="United States"):
    sentence = f"{city} is in {country}."
    print(sentence)

#To call the function and describe the cities
 describe_city("New York")
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")

#8-6
def city_country(city, country):
    return f"{city}, {country}"

#To call the functions 
city1 = city_country("New York", "United States")
city2 = city_country("Reykjavik", "Iceland")
city3 = city_country("gusau", "Nigeria")

#8-7
def make_album(artist, album, num_songs=None):
    album_info = {"Artist": artist, "Album": album}
    if num_songs is not None:
        album_info["Number of Songs"] = num_songs
    return album_info

#8-8
    def make_album(artist, album, num_songs=None):
    album_info = {"Artist": artist, "Album": album}
    if num_songs is not None:
        album_info["Number of Songs"] = num_songs
    return album_info

albums = []
while True:
    artist = input("Enter the artist's name (or 'quit' to quit): ")
    if artist.lower() == "quit":
        break

    album = input("Enter the album's title: ")
    num_songs = input("Enter the number of songs on the album (or 'skip' to skip): ")
    if num_songs.lower() != "skip":
        num_songs = int(num_songs)

    new_album = make_album(artist, album, num_songs)
    albums.append(new_album)
    print(f"Added album: {new_album}")


#8-9
messages = [
    "Hello, world!",
    "Goodbye, world!",
    "Have a great day!",
]
#8-10
def send_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    return sent_messages


#functions to print the messages
sent_messages = send_messages(messages)

print("Original messages list:")
print(messages)

print("Sent messages list:")
print(sent_messages)    

#8-11
copied_messages = messages.copy()
sent_messages = send_messages(copied_messages)

print("Original messages list:")
print(messages)

print("Sent messages list:")
print(sent_messages)      

#8-12
def make_sandwich(*items):
    sandwich = ", ".join(items)
    print(f"Ordering a sandwich with {sandwich}.")

make_sandwich("cheese", "lettuce", "tomato")
make_sandwich("ham", "cheese", "bread", "mustard")
make_sandwich("chicken", "bacon", "lettuce", "tomato", "mayo")

#8-13
def build_profile(first_name, last_name, **key_value_pairs):
    profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    for key, value in key_value_pairs.items():
        profile[key] = value
    return profile

user_profile = build_profile("John", "Doe", occupation="Software Engineer", city="New York")
print(user_profile)
#8-14
def make_car(manufacturer, model, **optional_info):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in optional_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)