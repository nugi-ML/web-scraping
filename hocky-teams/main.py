from bs4 import BeautifulSoup
import requests
import urllib3
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = []

for page in range(1,26):
    print(f"Sedang scraping halaman {page}")
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={page}"
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        teams = soup.find_all('tr', class_='team')
        for team in teams:
            name = team.find('td', class_='name').text.strip()
            win = team.find('td', class_='wins').text.strip()
            lose = team.find('td', class_='losses').text.strip()
            data.append({
                'Team Name' : name,
                'Wins' : win,
                'Losses' : lose
            })

    else:
        print(f"Gagal mengakses halaman {page}")

with open("teams_hocky.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Name', 'Wins', 'Losses'])
    
    for item in data:
        writer.writerow([item['Team Name'], item['Wins'], item['Losses']])

print("Data berhasil disimpan dengan nama teams_hocky.csv")