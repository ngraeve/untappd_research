
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
import csv

header = ['Beer', 'Brewery', 'Style', 'YourRating', 'GlobalRating']

with open('C:\\Users\\Pinball\\Documents\\Jarod.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    with open('C:\\Users\\Pinball\\Documents\\Jarod.html', 'rb') as html:
        soup = BeautifulSoup(html)

    mydivs = soup.find_all("div", {"class": "beer-details"})


    for div in mydivs:
        #print(f"Beer - {div.find('p', {'class': 'name'}).get_text()}")
        #print(f"Brewery - {div.find('p', {'class': 'brewery'}).get_text()}")
        #print(f"Style - {div.find('p', {'class': 'style'}).get_text()}")
        #rating = div.find('p', {'class': None}).get_text()
        
        ratings = div.find_all('p', {'class': None})
        #print(f"Your rating - {ratings[0].get_text()[ratings[0].get_text().find('(')+1:len(ratings[0].get_text()) - 1]}")
        #print(f"Global rating - {ratings[1].get_text()[ratings[1].get_text().find('(')+1:len(ratings[1].get_text()) - 1]}")

        if len(ratings) == 2:
            writer.writerow([
                div.find('p', {'class': 'name'}).get_text(),
                div.find('p', {'class': 'brewery'}).get_text(),
                div.find('p', {'class': 'style'}).get_text(),
                ratings[0].get_text()[ratings[0].get_text().find('(')+1:len(ratings[0].get_text()) - 1],
                ratings[1].get_text()[ratings[1].get_text().find('(')+1:len(ratings[1].get_text()) - 1]
                ])
        
        else:
            writer.writerow([
                div.find('p', {'class': 'name'}).get_text(),
                div.find('p', {'class': 'brewery'}).get_text(),
                div.find('p', {'class': 'style'}).get_text(),
                None,
                ratings[0].get_text()[ratings[0].get_text().find('(')+1:len(ratings[0].get_text()) - 1]
                ])
