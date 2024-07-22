import requests
from bs4 import BeautifulSoup
import csv
import click

@click.command()
@click.argument('ticker')
def main(ticker):
    """ This script fetches stock data for the given ticker and saves it to a CSV file. """
    url = f"https://fr.finance.yahoo.com/quote/{ticker}/key-statistics/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    page_content = fetch_page(url, headers)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        table_titles = ["Mesures d’évaluation", "Exercice fiscal", "Rentabilité", "Efficacité de la gestion", "Bilan", "Compte de résultat", "État du flux de trésorerie", "Historique du prix des actions", "Statistiques des actions", "Dividendes et divisions"]
        extracted_data = extract_data(soup, table_titles)
        save_to_csv(extracted_data, f"{ticker.lower()}_finance_data.csv")

def fetch_page(url, headers):
    """ Fetch the content of a webpage given its URL and request headers. """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def extract_data(soup, titles):
    """ Extract specified data from the BeautifulSoup object based on titles. """
    data = []
    for title in titles:
        title_tag = soup.find('span', string=title)
        if title_tag:
            table = title_tag.find_parent('div').find_next('table')
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) > 1:
                        key = cells[0].text.strip()
                        value = cells[1].text.strip()
                        data.append((title, key, value))
            else:
                print(f"Table not found under title '{title}'.")
        else:
            print(f"Title '{title}' not found.")
    return data

def save_to_csv(data, filename):
    """ Save extracted data to a CSV file. """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tableau', 'Indicateur', 'Valeur'])
        for item in data:
            writer.writerow(item)
    print(f"The data was saved in {filename}.")

if __name__ == '__main__':
    main()
