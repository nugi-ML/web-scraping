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

data = []

print("Sedang scraping website")
if response.status_code == 200:
    for country in info_country:
        country_name = country.find('h3').text.strip()
        country_population = country.find('span', class_='country-population').text.strip()
        country_area = country.find('span', class_='country-area').text.strip()
        data.append({
            'name' : country_name,
            'population' : country_population,
            'area' : country_area
        })
else:
    print("Gagal scraping halaman")

print("Berhasil scraping halaman")

with open('countries.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Country Name', 'Population', 'Area'])  # Menulis header CSV
    
    for item in data:
        writer.writerow([item['name'], item['population'], item['area']])  # Menulis data negara ke CSV