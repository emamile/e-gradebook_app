from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):
    def __init__(self, name: str, surname: str, jmbg: str, date_of_birth: str, country_of_birth: str, city_of_birth: str):
        self.name = name
        self.surname = surname
        self.__jmbg = jmbg
        self.__date_of_birth = date_of_birth
        self.__country_of_birth = country_of_birth
        self.__city_of_birth = city_of_birth
        self.__age = datetime.today().year - int(date_of_birth.split(".")[2])
        self.place_of_birth = f"{city_of_birth}, {country_of_birth}"

    def get_age(self):
        """
        The function get_age() returns the value of the private variable __age
        :return: The age of the person.
        """
        return self.__age

    def get_jmbg(self):
        """
        The function get_jmbg() returns the value of the private attribute __jmbg
        :return: The value of the private attribute jmbg.
        """
        return self.__jmbg

    def get_date_of_birth(self):
        """
        The function get_date_of_birth() returns the value of the private variable __date_of_birth
        :return: The date of birth of the person.
        """
        return self.__date_of_birth

    def get_country_of_birth(self):
        """
        This function returns the country of birth of the person
        :return: The country of birth.
        """
        return self.__country_of_birth

    def get_city_of_birth(self):
        """
        The function get_city_of_birth() returns the value of the private variable __city_of_birth
        :return: The city of birth.
        """
        return self.__city_of_birth

    @abstractmethod
    def show_person_info(self):
        """
        It prints the person's name and age.
        """
        pass

