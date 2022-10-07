import requests
from bs4 import BeautifulSoup
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60"
}

class CitiesScraper():
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
        links = ["http://www.schooldays.ie" + i if "http" not in i else i for i in links]
        print("LEN BEFORE", len(links))
        links = list(set(links))
        print("LEN AFTER", len(links))
        return links    # list

    # def extract_data(self, cities_list: list):










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
