import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from data_extractor import DataExtractor

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60"
}


@dataclass(slots=True)
class School:
    """Contains all info about school"""
    work_link: str = None
    name: str = None
    phone: str = None
    roll_number: str = None
    address: str = None
    email: str = None
    website: str = None
    principal: str = None
    enrolment: str = None
    ethos: str = None
    fees: str = None


class CitiesScraper:
    def __init__(self, url: str, cities: list):
        self.url = url
        self.cities = cities

    def get_cities_links(self):
        result_links = []
        req_src = requests.get(self.url, headers=headers).content
        soup_cities_page = BeautifulSoup(req_src, "html.parser")
        for city in self.cities:
            links_raw_data = soup_cities_page.find('div', {'class': city}).find_all('a')
            links = [i['href'] for i in links_raw_data]
            result_links.extend(links)
        return result_links

    def fix_links(self, links: list):
        """Fixing not properly cutted links for cities"""
        links = ["http://www.schooldays.ie" + i if "http" not in i else i for i in links]
        print("LEN BEFORE", len(links))
        links = list(set(links))
        print("LEN AFTER", len(links))
        return links

    def extract_school_links(self, cities_list: list):
        """Forming list of school list for city on each iteration and start to scrape"""
        for city in cities_list:
            city_req = requests.get(city, headers=headers)
            city_soup = BeautifulSoup(city_req.content, 'html.parser')
            school_links = [i['href'] for i in city_soup.find('div', id='block_main').find_all('a')]
            school_links = ["https://www.schooldays.ie" + i for i in school_links]
            print(city, "----- ", school_links)
            self.extract_data(school_links)

    def extract_data(self, school_list: list):
        for item in school_list:
            src = requests.get(item, headers=headers).content
            soup = BeautifulSoup(src, 'html.parser')

            extractor = DataExtractor(soup)

            work_link = item
            name = extractor.get_name()
            phone = extractor.get_phone()
            roll_number = extractor.get_roll_number()
            address = extractor.get_address()
            email = extractor.get_email()
            website = ""
            principal = ""
            enrolment = ""
            ethos = ""
            fees = ""

            print(work_link)
            print(name)
            print(phone)
            print(roll_number)
            print(address)
            print(email)
            print("-*-"*30)

    def is_not_scraped(self, school_link):
        """Check if school is already scraped"""
        with open('log.txt') as f:
            scraped_school = f.readlines()
        if school_link in scraped_school:
            return True
        else:
            return False

# def get_cities_list():
#     start_url = "https://www.schooldays.ie/articles/primary-Schools-in-Ireland-by-County"
#     start_req = requests.get(start_url, headers=headers)
#     start_req_src = start_req.content
#     start_req_soup = BeautifulSoup(start_req_src, "html.parser")
#     city_links = start_req_soup.find('div', {'class': 'sdschoollist'}).find_all('a')
#     city_links = [i['href'] for i in city_links]
#
#     # Add munster links
#     munster_city_soup = start_req_soup.find('div', {'class': 'panelMun'}).find_all('a')
#     munster_list = [i['href'] for i in munster_city_soup]
#     munster_list = list(set(munster_list))
#     munster_list.sort()
#     print("MUSTER: ", len(munster_list))
#     print(munster_list)
#     city_links.extend(munster_list)
#
#     # Add CONNAUGHT links
#     connaught_city_soup = start_req_soup.find('div', {'class': 'panelCon'}).find_all('a')
#     connaught_list = [i['href'] for i in connaught_city_soup]
#     print("Connaught: ", len(connaught_list))
#     city_links.extend(connaught_list)
#
#     # Add ulster
#     ulster_city_soup = start_req_soup.find('div', {'class': 'panelUls'}).find_all('a')
#     ulster_list = [i['href'] for i in ulster_city_soup]
#     print("ULSTER: ", len(ulster_list))
#     city_links.extend(munster_list)
#
#     city_links.sort()
#     city_links = list(set(city_links))
#     city_links = ["http://www.schooldays.ie" + i if "http" not in i else i for i in city_links]
#     for i in city_links:
#         print(i)
#     print(len(city_links))
#
#     return city_links
