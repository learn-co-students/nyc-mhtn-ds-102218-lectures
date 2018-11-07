import requests
from bs4 import BeautifulSoup
import re
from listing import Listing

class ListingBuilder:
    def run(self):
        cl = CraigsListScraper()
        listings = []
        for listing_html in cl.listings_html():
            parser = ListingParser(listing_html)
            listing = Listing(parser.title(), parser.housing(), parser.neighborhood(), parser.price())
            listings.append(listing)
        return listings

class CraigsListScraper:
    def webpage_html(self, url = 'https://newyork.craigslist.org/search/brk/aap'):
        craigslist_request = requests.get(url)
        self.craigslist_html = craigslist_request.text
        return self.craigslist_html

    def listings_html(self, craigslist_html = None):
        craigslist_html = craigslist_html or self.craigslist_html
        craigslist_soup = BeautifulSoup(craigslist_html)
        listings =  craigslist_soup.findAll('li', {'class':"result-row"})
        self.listings = listings
        return self.listings

class ListingParser:
    def __init__(self, listing_html):
        self.listing_html = listing_html

    def neighborhood(self):
        return self.parse(self.listing_html, 'hood')

    def title(self):
        return self.parse(self.listing_html, 'title')

    def housing(self):
        return self.parse(self.listing_html, 'housing').strip()

    def price(self, listings = None):
        price = self.parse(self.listing_html, 'price')
        return int(price[1:])

    def parse(self, criteria):
        result = self.listing_html.find(class_=re.compile(r'.*%s' % criteria)})
        return result.text
