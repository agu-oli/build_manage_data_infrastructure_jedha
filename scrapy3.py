import os
import logging
import scrapy
import time
from scrapy.crawler import CrawlerProcess

class BookingSpider(scrapy.Spider):
    name = 'booking'
    start_urls = ['https://www.booking.com']

    cities = [
        "Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris", 
        "Amiens", "Lille", "Strasbourg", "Chateau du Haut Koenigsbourg", "Colmar", 
        "Eguisheim", "Besancon", "Dijon", "Annecy", "Grenoble", "Lyon", "Gorges du Verdon", 
        "Bormes les Mimosas", "Cassis", "Marseille", "Aix en Provence", "Avignon", "Uzes", 
        "Nîmes", "Aigues Mortes", "Les Saintes-Maries-de-la-Mer", "Collioure", "Carcassonne", 
        "Ariege", "Toulouse", "Montauban", "Biarritz", "Bayonne", "La Rochelle"
    ]
    
    def start_requests(self):
        for city in self.cities:
            search_url = f'https://www.booking.com/searchresults.fr.html?ss={city}'
            yield scrapy.Request(
                url=search_url,
                callback=self.after_search,
                cb_kwargs={'city': city}
            )

    def after_search(self, response, city):
        hotels = response.xpath('//*[@data-testid="property-card"]')

        for hotel in hotels:
            hotel_name = hotel.xpath('.//div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]/text()').get()
            url = hotel.xpath('.//a/@href').get()

            try:
                note = hotel.xpath('.//div[2]/div/div/a/span/div/div[1]/text()').get()
            except KeyError:
                note = None

            # Construct the full URL for the hotel detail page
            hotel_url = response.urljoin(url)
            
            yield scrapy.Request(
                url=hotel_url,
                callback=self.parse_hotel_details,
                cb_kwargs={'city': city, 'hotel_name': hotel_name, 'note': note}
            )

    def parse_hotel_details(self, response, city, hotel_name, note):
        # Scrape latitude, longitude and description
    
        lat_lon = response.xpath('//*[@id="hotel_address"]').attrib['data-atlas-latlng']

        # Scrape description
        description = response.xpath('//*[@id="basiclayout"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/p[1]/text()').get()

        yield {
            'city': city,
            'hotel': hotel_name,
            'url': response.url,
            'note': note,
            'coordinates': lat_lon,
            'description': description
        }

filename = 'booking5.json'

# Ensure the directory exists
if not os.path.exists('booking_scraping'):
    os.makedirs('booking_scraping')

# Remove the file if it already exists
file_path = os.path.join('booking_scraping', filename)
if os.path.exists(file_path):
    os.remove(file_path)

process = CrawlerProcess(settings={
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    'FEEDS': {
        file_path: {'format': 'json'},
    }
})

process.crawl(BookingSpider)
process.start()
