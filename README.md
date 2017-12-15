#this is a repository I, Nathan Reilly, made to submit my webscraping code please view setup_tutorial.txt to see how.

#TO VIEW MY FLOWCHART SEE: MY FLOWCHART.png in repository 

#to setup my web scraping code
first you need to install notepad++
secondly install python version 2.7.14 (https://www.python.org/downloads/)
then setup your cmd to run virtual environments using pip (look this up or use the assignment:http://moodle.clevelandhighschool.org/mod/assign/view.php?id=4132)
once you have a virtual environment running in your cmd and notepad++ up with an new document,
copy and paste the following code into your document:

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

make sure to save the file with the name of ur choice but change the file type to a .py file
your almost done!
now all u gotta do is type in the cmd: python (insert file name).py 
it should collect data about the text located at the cite: https://tekka332510898.wordpress.com/
it will search for the data every 20 seconds.
this code can be reused for any website with only a few changes:

here's an example of what I mean:

# coding: utf-8
# import libraries
import time
import urllib2
from bs4 import BeautifulSoup

def main():
  while True:
    quote_page = 'Your url here'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('what the section is (use inspect)', attrs={'class': 'what the class is (use inspect)'})
    name = name_box.text
    print name
    price_box = soup.find('what the section is (use inspect)', attrs={'class':'what the class is (use inspect)'})
    price = price_box.text
    print price  
    time.sleep(number of seconds between checks)
  
if __name__ == "__main__":
  main()


