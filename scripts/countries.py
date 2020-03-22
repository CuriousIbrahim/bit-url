import requests
from bs4 import BeautifulSoup
import csv
import os

FILE_NAME = 'countries.csv'


if (os.path.isfile(FILE_NAME)):
    os.remove(FILE_NAME)


with open(FILE_NAME, 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['country name', 'country code', 'country iso 1', 'country iso 2'])


r = requests.get('https://countrycode.org/')

soup = BeautifulSoup(r.content, 'lxml')

r.close()


table = soup.find('table')

all_rows = table.find_all('tr')

# the added [1:] is used to ignore the header
for row in all_rows[1:]:
    data = row.find_all('td')

    country_name = data[0].text.strip()
    country_code = data[1].text.strip()

    iso_codes = data[2].text

    iso_codes = iso_codes.split('/')

    iso_code_1 = iso_codes[0].strip()
    iso_code_2 = iso_codes[1].strip()


    with open(FILE_NAME, 'a+') as file:
        writer = csv.writer(file)

        writer.writerow([country_name, country_code, iso_code_1, iso_code_2])

    print(country_name, country_code, iso_code_1, iso_code_2)