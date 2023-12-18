# question 1 read files and count lines

import os

def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = 0
        words = 0
        for line in file:
            lines += 1
            word_count = len(line.split())
            words += word_count
        return lines, words

# Read obama_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('data/obama_speech.txt')
print(f"Obama's speech has {lines} lines and {words} words.")

# Read michelle_obama_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('data/michelle_obama_speech.txt')
print(f"Michelle's speech has {lines} lines and {words} words.")

# Read donald_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('data/donald_speech.txt')
print(f"Trump's speech has {lines} lines and {words} words.")

# Read melina_trump_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('data/melina_trump_speech.txt')
print(f"Melina's speech has {lines} lines and {words} words.")

# question 2 Read countries_data.json data file and find the ten most spoken languages
import json

def find_most_spoken_languages(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    language_counts = {}
    for country in data:
        language = country['language']
        if language not in language_counts:
            language_counts[language] = 0
        language_counts[language] += 1

    most_spoken_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return most_spoken_languages

most_spoken_languages = find_most_spoken_languages('data/countries_data.json')
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

# question 3 Read countries_data.json data file and create a list of the ten most populated countries:
def find_most_populated_countries(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    most_populated_countries = sorted(data, key=lambda x: x['population'], reverse=True)[:10]
    return most_populated_countries

most_populated_countries = find_most_populated_countries('data/countries_data.json')
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

#question 4 Extract all incoming email addresses as a list from the email_exchange_big.txt file:
def extract_email_addresses(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()

                email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
                return email_addresses

email_addresses = extract_email_addresses('data/email_exchange_big.txt')
print(f"{len(email_addresses)} email addresses found: {email_addresses}")

# question 5 Find the most common words in the English language.

# question 6 Use the function, find_most_frequent_words to find:

# question 7 Write a python application that checks similarity between two texts.

# question 8 Find the 10 most repeated words in the romeo_and_juliet.txt:

def find_most_repeated_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    words = re.findall(r'\b\w+\b', content)
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    most_repeated_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return most_repeated_words

most_repeated_words = find_most_repeated_words('data/romeo_and_juliet.txt')
for word, count in most_repeated_words:
    print(f"{word}: {count}")

# question 9 Read the hacker news csv file and find out

import csv

def count_occurrences(file_path, keyword):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        count = sum(1 for row in reader if keyword.lower() in row[1].lower())
    return count

# Count the number of lines containing python or Python
python_count = count_occurrences('data/hacker_news.csv', 'python')
print(f"{python_count} lines contain 'python' or 'Python'.")

# Count the number lines containing JavaScript, javascript or Javascript
javascript_count = count_occurrences('data/hacker_news.csv', 'javascript')
print(f"{javascript_count} lines contain 'JavaScript', 'javascript' or 'Javascript'.")

# Count the number of lines containing Java and not JavaScript
java_count = count_occurrences('data/hacker_news.csv', 'java') - javascript_count
print(f"{java_count} lines contain 'Java' but not 'JavaScript', 'javascript' or 'Javascript'.")