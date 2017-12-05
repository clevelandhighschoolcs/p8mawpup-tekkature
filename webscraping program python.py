# coding: utf-8
# import libraries
import time
import urllib2
from bs4 import BeautifulSoup

def main():
  while True:
    quote_page = 'https://tekka332510898.wordpress.com/'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'entry-title'})
    name = name_box.text
    print name
    price_box = soup.find('div', attrs={'class':'entry-content'})
    price = price_box.text
    print price  
    time.sleep(20)
  
if __name__ == "__main__":
  main()