# Web Scraper
### By: Nathan Reilly
This was made for my IB Computer Science Course

![Flowchart](https://github.com/clevelandhighschoolcs/p8mawpup-tekkature/blob/master/images/my%20flowchart.PNG)

# To setup my web scraping code you will need

- [ ] install notepad++ (if not already installed)
- [ ] install [python version 2.7.14](https://www.python.org/downloads/) (if not already installed)
- [ ] setup your virtual enviroment
- [ ] Download the code

Once you have a virtual environment ready move the [pythonwebscraper.py](https://github.com/clevelandhighschoolcs/p8mawpup-tekkature/blob/master/pythonwebscraper.py) into it. Make sure to install the BeautifulSoup liberary in your virtual enviroment.

```CMD
  pip install bs4
```

# Modifying
The program by default is checking [my blog](https://tekka332510898.wordpress.com/) for change but you can change that by opening the web scraper in notepad++ and changing the url in this line

```Python
  quote_page = 'https://tekka332510898.wordpress.com/'
```

It will automatically check the website for change every 20 seconds to change how often it checks change the number here

```Python
  time.sleep(20)
```

# Running the code
Now all you gotta do is type in the virtual enviroment:

```CMD
  python pythonwebscraper.py 
```
