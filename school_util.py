import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from data_extractor import DataExtractor
from data_writer import DataWriter, School
import os


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60"
}


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
            if not self.is_not_scraped(item):
                src = requests.get(item, headers=headers).content
                soup = BeautifulSoup(src, 'html.parser')

                extractor = DataExtractor(soup)

                work_link = item
                name = extractor.get_name()
                phone = extractor.get_phone()
                roll_number = extractor.get_roll_number()
                address = extractor.get_address()
                email = extractor.get_email()
                website = extractor.get_website()
                principal = extractor.get_principal()
                enrolment = extractor.get_enrollment()
                ethos = extractor.get_echos()
                fees = extractor.get_fees()

                """Create class with info"""
                school_object = School(work_link=work_link, name=name, phone=phone, roll_number=roll_number,
                                       address=address, email=email, website=website, principal=principal,
                                       enrolment=enrolment, ethos=ethos, fees=fees)

                print("Work link: ", school_object.work_link)
                print("Name: ", school_object.name)
                print("Phone: ", school_object.phone)
                print("Roll number: ", school_object.roll_number)
                print("Address: ", school_object.address)
                print("Email: ", school_object.email)
                print("Website: ", school_object.website)
                print("Principal: ", school_object.principal)
                print("Enrolment: ", school_object.enrolment)
                print("Ethos: ", school_object.ethos)
                print("Fees: ", school_object.fees)
                print("-*-"*30)
            else:
                print("ALREADY SCRAPED: ", item)

            """Writing data to csv and links to log file"""
            csv_writer = DataWriter(school_object, 'school-data.csv')
            csv_writer.write_to_csv()
            log_writer = DataWriter()
            log_writer.write_to_log(school_object.work_link)


    def is_not_scraped(self, school_link):
        if "data" not in os.listdir():
            os.mkdir('data')

        """Check if school is already scraped"""
        try:
            with open('data/log.txt', 'r') as f:
                scraped_school = f.readlines()
        except FileNotFoundError:
            with open('data/log.txt', 'w') as f:
                print("LOG FILE CREATED")
                scraped_school = []
        if school_link in scraped_school:
            return True
        else:
            return False

    def reset_log(self):
        answer = input('Do you need to reset your LOG file? Y/N')
        if answer.lower() == 'y':
            try:
                os.remove("data/log.txt")
                print("LOG file REMOVED!!!")
            except:
                print('EXCEPTION')
            else:
                print("There is no LOG file. Don't worry. It will be created")
        else:
            print("Resume to scrape using info from LOG file")
