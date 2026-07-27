from bs4 import BeautifulSoup
import requests
import urllib3
import csv

# Menyembunyikan peringatan/warning terkait SSL yang dimatikan
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, 'lxml')
info_country = soup.find_all('div', class_='col-md-4 country')

with open('countries.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Country Name', 'Population', 'Area'])  # Menulis header CSV
    
    for country in info_country:
        country_name = country.find('h3').text.strip()
        country_population = country.find('span', class_='country-population').text.strip()
        country_area = country.find('span', class_='country-area').text.strip()
        writer.writerow([country_name, country_population, country_area])  # Menulis data negara ke CSV