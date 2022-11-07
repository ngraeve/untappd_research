
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
import csv

header = ['Beer', 'Brewery', 'Style', 'YourRating', 'GlobalRating', 'FirstCheckIn', 'RecentCheckIn']

with open('./data/Jarod2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    with open('./data/Jarod.html', 'rb') as html:
        soup = BeautifulSoup(html)

    # mydivs = soup.find_all("a", {"data-href": ":firstCheckin"})
    # for div in mydivs:
    #     print(div.get_text())

    # mydivs = soup.find_all("div", {"class": "beer-details"})

    mydivs = soup.find_all('div', {'class': 'beer-item'})

    for div in mydivs:
        first = div.find('a', {'data-href':':firstCheckin'}).get_text()
        recent = div.find('a', {'data-href':':recentCheckin'}).get_text()
        ratings = div.find_all('p', {'class': None})
        try:
            personal_rating = ratings[0].get_text()[ratings[0].get_text().find('(')+1:len(ratings[0].get_text()) - 1]
        except IndexError: 
            personal_rating = None
        
        try:
            global_rating = ratings[1].get_text()[ratings[1].get_text().find('(')+1:len(ratings[1].get_text()) - 1]
        except IndexError: 
            global_rating = None

        writer.writerow([
            div.find('p', {'class': 'name'}).get_text(),
            div.find('p', {'class': 'brewery'}).get_text(),
            div.find('p', {'class': 'style'}).get_text(),
            personal_rating,
            global_rating,
            first,
            recent
            ])
        
