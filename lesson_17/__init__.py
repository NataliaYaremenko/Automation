from __future__ import unicode_literals
from os.path import abspath, join, dirname
from random import randint, choice, sample
from datetime import datetime
import csv


def full_path(filename):
    return abspath(join(dirname(__file__), filename))

def get_first_name(gender=None):
    with open(full_path('data.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        filtered_data = [row[0] for row in reader if row and row[0] and (gender is None or row[2].lower() == gender.lower())]
    return choice(filtered_data) if filtered_data else "Unknown"

def get_last_name():
    with open(full_path('data.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        last_names = [row[1] for row in reader if row and row[1]]
    return choice(last_names) if last_names else "Unknown"

def get_country():
    with open(full_path('data.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        countries = [row[3] for row in reader if row and row[3]]
    return choice(countries) if countries else "Unknown"

def get_address():
    with open(full_path('data.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        addresses = [row[6] for row in reader if row and row[6]]
    return choice(addresses) if addresses else "Unknown"

def get_email(person):
    return f"{person.first_name.lower()}.{person.last_name.lower()}@example.com"

def get_birthdate():
    return datetime.strftime(datetime.strptime(f"{randint(1970, 2005)}-{randint(1,12):02d}-{randint(1,28):02d}", "%Y-%m-%d"), "%d %b, %Y")

def random_password(length=8):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(sample(chars, length))

def get_hobbies():
    with open(full_path('data.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        hobbies = [row[4] for row in reader if row and row[4]]
    return sample(hobbies, min(3, len(hobbies))) if hobbies else ["Unknown"]

class Person:
    def __init__(self, gender=None):
        self.first_name = get_first_name(gender)
        self.last_name = get_last_name()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.birthdate = get_birthdate()
        self.phone = f"+1-{randint(100,999)}-{randint(100,999)}-{randint(1000,9999)}"
        self.email = get_email(self)
        self.gender = gender if gender else "male" if self.first_name.endswith("n") else "female"
        self.country = get_country()
        self.paswd = random_password()
        self.hobbies = get_hobbies()
        self.address = get_address()
        self.customAttr = {}

    def set_attr(self, attr_name, value=None):
        if attr_name.isalnum() and attr_name[0].isalpha():
            self.customAttr[attr_name] = value
            print(f"Attribute '{attr_name}' added.")
        else:
            raise ValueError("Attribute name must start with a letter and contain only alphanumeric characters.")

    def get_attr(self, attr_name):
        if attr_name in self.customAttr:
            return self.customAttr[attr_name]
        raise AttributeError(f"Attribute '{attr_name}' does not exist.")

    def get_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "password": self.paswd,
            "country": self.country,
            "hobbies": self.hobbies,
            "address": self.address,
            "custom_attributes": self.customAttr,
        }


if __name__ == "__main__":
    person = Person()
    print(person.get_details())
