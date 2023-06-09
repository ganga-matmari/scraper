import csv
import requests
from bs4 import BeautifulSoup


url = "https://etenders.gov.in/eprocure/app?page=FrontEndTendersByOrganisation&service=page"

response = requests.get(url)

page_contents  = response.text

soup = BeautifulSoup(page_contents, 'html.parser')

filename = 'sc_data.csv'

csv_writer = csv.writer(open(filename, 'w',))


# run a for loop
for tr in soup.find_all('tr'):
    data = []

    for td in tr.find_all('td'):
        data.append(td.text)

    if data:
        print("Inserting headers: {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
        
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    
    if data:
        print("Inserting table data: {}".format(','.join(data)))
        csv_writer.writerow(data)







