import typing as t
from subjects import *
from person import *


class Teacher(Person):
    def __init__(self, name: str, surname: str, jmbg: str, date_of_birth: str, country_of_birth: str,
                 city_of_birth: str, subjects: t.List[Subject], id: str):
        super().__init__(name, surname, jmbg, date_of_birth, country_of_birth, city_of_birth)
        self.subjects = subjects
        self.id = id

    def get_id(self):
        """
        It returns the id of the object
        :return: The id of the object.
        """
        return self.id

    def show_person_info(self):
        """
        It returns a string containing the name, surname, JMBG, date of birth, city of birth and country of birth of the
        person
        :return: a string with the name, surname, jmbg, date of birth, city of birth and country of birth.
        """
        return f"{self.name} {self.surname}\n{self.get_jmbg()}\n{self.get_date_of_birth()}\n{self.get_city_of_birth()}, {self.get_country_of_birth()}"

    def add_subject(self, subject: Subject):
        """
        Add a subject to the list of subjects.

        :param subject: Subject - The subject to add to the list of subjects
        :type subject: Subject
        """
        self.subjects.append(subject)

    def extract_subject_names(self):
        """
        It takes a list of subjects and returns a list of the names of those subjects
        :return: A list of the names of the subjects in the class.
        """
        lst = []
        for sub in self.subjects:
            lst.append(sub.name)
        return lst


