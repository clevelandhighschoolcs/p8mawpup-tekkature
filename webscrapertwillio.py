# coding: utf-8
# import libraries
import time
import urllib2
from bs4 import BeautifulSoup
from twilio.rest import Client

url = 'https://tekka332510898.wordpress.com/'
account_sid = raw_input('Your account SID: ')
auth_token  = raw_input('Your authentication token: ')
twilio_phone_number = input('Your twilio number: ')
my_phone_number = input('Your phone number: ')
# I stole these ideas from Colin but I thought they were cool

quote_page = 'https://tekka332510898.wordpress.com/'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

def main():
    while True:
    
    name_box = soup.find('h1', attrs={'class': 'entry-title'})
    name = name_box.text
    print name
    price_box = soup.find('div', attrs={'class':'entry-content'})
    price = price_box.text
    print price  
    client = Client(account_sid, auth_token)
    client.messages.create(
        body="Title :" + name + ", Content: " + price,
        to=my_phone_number,
        from_=twilio_phone_number
    )

    time.sleep(20)
  
if __name__ == "__main__":
  main()
