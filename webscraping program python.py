# coding: utf-8
# import libraries
import time
import urllib2
from bs4 import BeautifulSoup

from twilio.rest import Client
from datetime import datetime

account_sid = 'XXX'
auth_token = 'XXX'
twilio_phone_number = 'XXX'
my_phone_number = 'XXX'

client = Client(account_sid, auth_token)
 
def main ():

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

    #Text your the information.
		body = name + ', ' + price + ', ' + str(datetime.now())
		client . messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
  
if __name__ == "__main__":
  main()
