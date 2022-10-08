import requests
from bs4 import BeautifulSoup
import re
from school_util import CitiesScraper
import csv

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60"
}
url5 = "https://www.schooldays.ie/school/cahir-b-n-s-rollnumber-18716T"

url = "https://www.schooldays.ie/articles/primary-Schools-in-Ireland-by-County"
cities_selectors = ['sdschoollist', 'panelMun', 'panelCon', 'panelUls']
scraper = CitiesScraper(url, cities_selectors)
cities_list_dirty = scraper.get_cities_links()
cities_list = scraper.fix_links(cities_list_dirty)
scraper.extract_school_links(cities_list)


# cities_list = get_cities_list()






# for i in cities_list:
#     city_req = requests.get(i, headers=headers)
#     city_src = city_req.content
#     city_soup = BeautifulSoup(city_src, 'html.parser')
#     school_links = city_soup.find('div', id='block_main').find_all('a')
#     school_links = [i['href'] for i in school_links]
#     school_links = ["https://www.schooldays.ie" + i for i in school_links]
#     for school in school_links:
#
#
#         with open('log.txt') as f:
#             scraped_school = f.readlines()
#         if school in scraped_school:
#             print(f"{school} IS SCRAPED!!!")
#             continue
#         else:
#
#             req = requests.get(school, headers=headers)
#             src = req.content
#             soup_all_data = BeautifulSoup(src, 'html.parser')
#             school_data = soup_all_data.find('div', id="area1")
#             detailed_data = school_data.find('p')
#
#             name = school_data.find('h1').text
#             phone = school_data.find('a').text
#             data_list = school_data.text.split("\n")
#
#             email = None
#             website = None
#             email_data = None
#
#             # GET email and website from links
#             all_links = school_data.find_all('a')
#             for i in all_links:
#                 # if re.search("^[\w.]+@([\w-]+\.)+[\w-]{2,4}$", i.text):
#
#                 if "http" in i['href']:
#                     website = i['href']
#
#             detailed_data = [i.text.strip().replace("\n", "") for i in detailed_data]
#             detailed_data = [i for i in detailed_data if len(i) > 2 and i != "CLOSED"]
#             address = detailed_data[2]
#             if address == "Primary" or address == "School":
#                 address = detailed_data[1]
#
#             print("Detailed Data: ", detailed_data)
#             print("Links: ", all_links)
#
#             for i in detailed_data:
#                 if re.search("^[A-Z0-9]{6}$", i):
#                     roll_number = i
#                 if "@" in i:
#                     email_data = i
#             try:
#                 principal = detailed_data[detailed_data.index("Principal:") + 1]
#             except:
#                 principal = None
#
#             try:
#                 enrolment = detailed_data[detailed_data.index("Enrolment:") + 1]
#             except:
#                 enrolment = None
#
#             try:
#                 ethos = detailed_data[detailed_data.index("Ethos:") + 1]
#             except:
#                 ethos = None
#
#             try:
#                 fees = detailed_data[detailed_data.index("Fees:") + 1]
#             except:
#                 fees = None
#
#             print("-" * 30)
#             print("WORKING LINK: ", school)
#             print("NAME: ", name)
#             print("PHONE: ", phone)
#             print("ROLL NUMBER: ", roll_number)
#             print("ADDRESS: ", address)
#             print("email: ", email_data)
#             print("WEBSITE: ", website)
#             print("PRINCIPAL: ", principal)
#             print("ENROLMENT", enrolment)
#             print("ETHOS: ", ethos)
#             print("FEES: ", fees)
#
#             for_write = [name, phone, address, roll_number, email_data, website, principal, enrolment, ethos, fees]
#             try:
#                 with open('result.csv', 'a+', encoding='utf-8', newline='') as file:
#                     writer = csv.writer(file)
#                     writer.writerow(for_write)
#             except:
#                 with open('error.txt', 'a+') as f:
#                     print(f"Error on page: {school}\n")
#
#             with open('log.txt', 'a+', encoding='utf-8') as file:
#                 file.write(school+"\n")


# ['', "St. Laurence O'toole's C.B.S. ", 'Phone:  01 8363490  ', ' Seville Place, Dublin 1   ,Dublin City D01A439', '   ', 'Primary School \xa0\xa0 Roll number: 17110B e: info@larriers.ie w: www.larriers.ie', ' Principal: Mark Candon ', 'Enrolment: Boys: 65    (2021/22) ', 'Ethos: Catholic, Parish: Seville Place  \xa0  ', 'Fees:', '']
# ['', 'St Frances Clinic Sp Sc ', 'Phone:  CLOSED  ', ' Temple Street Hospital   Dublin 1  ,Dublin City 1', '  ', 'Primary School \xa0\xa0 Roll number: 19217G     ', ' Principal: CLOSED ', 'Enrolment: Boys: 6    (2021/22) ', 'Ethos: Catholic, Parish: Sean Mcdermott Street  \xa0  ', 'Fees:', '']
# ['', 'Scoil Chaoimhin ', 'Phone:  01 8788594  ', ' Sraid Mhaoilbhride Baile Atha Cliath 1   ,Dublin City D01YT29', '   ', 'Primary School \xa0\xa0 Roll number: 19831B e: scoilchaoimhin@ymail.com w: gaelscoilchaoimhin.ie', " Principal: Ciaran O'Fearraigh ", 'Enrolment: Boys: 30 Girls: 25    (2021/22) ', 'Ethos: Catholic, Parish: Pro-Cathedral  \xa0  ', 'Fees:', '']