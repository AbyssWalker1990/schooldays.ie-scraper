from dataclasses import dataclass, asdict
import os
from dataclass_csv import DataclassWriter


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


class DataWriter:
    def __init__(self, data=None, file_name="log.txt"):
        self.data = data
        self.file_name = file_name

    def write_to_csv(self):
        if "data" not in os.listdir():
            os.mkdir('data')
        fil = asdict(self.data)
        print(type(fil))
        list_data = [self.data]
        with open(f"data/{self.file_name}", 'a+', encoding='utf8', newline='') as file:
            writer = DataclassWriter(file, list_data, School)
            writer.write(skip_header=True)

    def write_to_log(self, scraped_link):
        with open('data/log.txt', 'a+', encoding='utf-8') as file:
            file.write(scraped_link+"\n")



