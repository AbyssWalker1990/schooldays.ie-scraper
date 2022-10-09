from bs4 import BeautifulSoup
import re


class DataExtractor:
    def __init__(self, soup_obj):
        self.soup_obj = soup_obj
        self.school_data = self.soup_obj.find('div', id="area1")
        self.all_links = self.school_data.find_all('a')
        self.detailed_data = self.school_data.find('p')
        self.detailed_data = [i.text.strip().replace("\n", "") for i in self.detailed_data]
        self.detailed_data = [i for i in self.detailed_data if len(i) > 2 and i != "CLOSED"]

    def get_name(self):
        try:
            name = self.school_data.find('h1').text
        except:
            name = 'None'
        return name

    def get_phone(self):
        try:
            phone = self.school_data.find('a').text
        except:
            phone = 'None'
        return phone

    def get_roll_number(self):
        roll_number = 'None'
        for i in self.detailed_data:
            if re.search("^[A-Z0-9]{6}$", i):
                roll_number = i
        return roll_number

    def get_address(self):
        address = self.detailed_data[2]
        if address == "Primary" or address == "School":
            address = self.detailed_data[1]
        return address

    def get_email(self):
        email = 'None'
        for i in self.detailed_data:
            if "@" in i:
                email = i
        return email

    def get_website(self):
        website = 'None'
        for i in self.all_links:
            if "http" in i['href']:
                website = i['href']
        return website

    def get_principal(self):
        principal = 'None'
        try:
            principal = self.detailed_data[self.detailed_data.index("Principal:") + 1]
        except Exception as e:
            print("Error: ", Exception)
        return principal

    def get_enrollment(self):
        enrolment = 'None'
        try:
            enrolment = self.detailed_data[self.detailed_data.index("Enrolment:") + 1]
        except Exception as e:
            print("Error: ", Exception)
            enrolment = 'None'
        return enrolment

    def get_echos(self):
        ethos = 'None'
        try:
            ethos = self.detailed_data[self.detailed_data.index("Ethos:") + 1]
        except:
            ethos = 'None'
        return ethos


    def get_fees(self):
        fees = 'None'
        try:
            fees = self.detailed_data[self.detailed_data.index("Fees:") + 1]
        except:
            fees = 'None'
        return fees