<h2>About project</h2>

<p>This is a simple scraper for getting data about primary schools in Ireland</p>

<h2>How to start?</h2>

1. <p>First of all you can use requirements.txt for installing all libraries</p> 
- <p>Or install it manually:</p>

```
pip install bs4

pip install dataclass_csv

pip install requests
```
2. <p>Run main.py</p>
3. <p>Press n in terminal as answer for question about log file</p>
4. <p>Extracting of data has begun, info about scraped item will be printing in console</p>
5. <p>All data will be saved in data/school-data.csv</p>

<h2>How it works?</h2>
1. <p>Creating CitiesScraper object with url info and list of classes for scraping links of all cities</p>
2. <p>Starting method reset_log, that asks about reset log file or resume scraping using existing one?</p>
3. <p>Method get_cities_list getting all urls of cities</p>
4. <p>Starting fix_links method to check and remove issues in urls</p>
5. <p>List of cities_links is given to extract_school_links that one by one doing requests for all links and forming new lists of school links, where all needed info</p>
6. <p>On each iteration extract_school_links is forming a new list of school links and give it to extract_data method</p>
7. <p>extract_data is checking if one of these links is already scraped using is_not_scraped method, that also handles with checking if data folder and log file created and fix all problems with it</p>
8. <p>If link is not scraped already - doing request to page and creating BeautifulSoup object. Then creating object of DataExtractor class and give bs4 object to him</p>
9. <p>Inside DataExtractor class we have various methods to scrape data</p>
10. <p>After collecting data from one of school we are creating an object of School dataclass</p>
11. <p>Also printing in console info about what we scraped for monitoring in real-time</p>
12. <p>For writing data in csv and log file we are creating object of DataWriter class and give to it our School object and name of file we want to create or add info to existing one</p>
13. <p>The same thing we are doing with log file, using DataClass object with no arguments and method to writing links in log.txt</p>

<p>Any moment we can stop scraping and resume it using log.txt for avoid to follow already scraped links</p>

