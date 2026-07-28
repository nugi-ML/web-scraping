import requests
import csv

BASE_URL = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={}'

def scrape_year(year):
    url = BASE_URL.format(year)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        films = response.json()
        
        if not films:
            print(f"Tidak ada data untuk tahun {year}")
            return []
        
        data = []
        
        for film in films:
            data.append({
                'Film Title' : film.get('title'),
                'Year' : film.get('year'),
                'Awards' : film.get('awards'),
                'Nominations' : film.get('nominations'),
                'Best Picture' : film.get('best_picture', False)
            })
        
        print(f"Tahun {year}: {len(data)} film berhasil diambil")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil data {year}")
        print(f"Error {e}")
        return []
    except ValueError:
        print(f"Data JSON tahun {year} tidak valid")
        return []

def save_to_csv(data, filename):
    fieldnames = ['Film Title', 'Year', 'Awards', 'Nominations', 'Best Picture']
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Data berhasil disimpan ke '{filename}'")
    
    except IOError as e:
        print(f"Gagal menyimpan file CSV")
        print(f"Error: {e}")

def main():
    all_data = []
    
    for year in range(2010,2016):
        print(f"Sedang scraping data tahun {year} ...")
        yearly_data = scrape_year(year)
        all_data.extend(yearly_data)
        
        if all_data:
            save_to_csv(all_data, "oscar-winning-films.csv")
            print(f"Total film yang disimpan: {len(all_data)}")
        else:
            print(f"Tidak ada data yang berhasil disimpan")

if __name__ == "__main__":
    main()