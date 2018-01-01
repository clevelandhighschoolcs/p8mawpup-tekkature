# coding: utf-8
# import libraries
import time
import urllib2
from bs4 import BeautifulSoup
from twilio.rest import Client

url = 'https://tekka332510898.wordpress.com/'
account_sid = '(ur account sid here)'
auth_token = '(ur auth token here)'
twilio_phone_number = '+1(ur twilio number here)'
my_phone_number = '+1(ur number here)'

def main():
  while True:
    client = Client(account_sid, auth_token)
    client.messages.create(
   body="
    quote_page = 'https://tekka332510898.wordpress.com/'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'entry-title'})
    name = name_box.text
    print name
    price_box = soup.find('div', attrs={'class':'entry-content'})
    price = price_box.text
    print price  
    time.sleep(20)",
        to=my_phone_number,
        from_=twilio_phone_number
    )

    time.sleep(20)
  
if __name__ == "__main__":
  main()
