import requests
import urllib3
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = []

for year in range(2010,2016):
    print(f"Sedang scraping halaman tahun {year}")
    url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={year}"
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        films = response.json()
        for film in films:
            title = film.get('title')
            year = film.get('year')
            awards = film.get('awards')
            nominations = film.get('nominations')
            best_picture = film.get('best_picture', False)
            data.append({
                'Film Title': title,
                'Year': year,
                'Awards': awards,
                'Nominations': nominations,
                'Best Picture': best_picture
            })
    else:
        print("Gagal scraping halaman")

fieldnames = ['Film Title', 'Year', 'Awards', 'Nominations', 'Best Picture']

with open("oscar-winning-films.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data berhasil disimpan pada file oscar-winning-films.csv")