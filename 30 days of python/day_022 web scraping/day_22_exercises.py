# question 1
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extracting table headers
headers = [th.text.strip() for th in soup.find_all('th')]

# Extracting table data
data = []
for row in soup.find_all('tr')[1:]:
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

# Combining headers and data
table = [dict(zip(headers, row)) for row in data]

# Converting to json and saving
with open('table.json', 'w') as f:
    json.dump(table, f)

# question 2
    import pandas as pd

url = 'https://archive.ics.uci.edu/ml/datasets.php'
table = pd.read_html(url)[0]
table.to_json('table.json', orient='records')
# question 3
import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extracting table headers
headers = [th.text.strip() for th in soup.find_all('th')]

# Extracting table data
data = []
for row in soup.find_all('tr')[1:]:
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

# Combining headers and data
table = [dict(zip(headers, row)) for row in data]

# Converting to json and saving
with open('presidents.json', 'w') as f:
    json.dump(table, f)