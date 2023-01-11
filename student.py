from projekat.person_class import *


class Student(Person):
    def __init__(self, name: str, surname: str, jmbg: str, date_of_birth: str, country_of_birth: str,
                 city_of_birth: str, grade: str, grade_class: str, id: str):
        super().__init__(name, surname, jmbg, date_of_birth, country_of_birth, city_of_birth)
        self.grade = grade
        self.grade_class = grade_class
        self.id = id
        self.subjects = {}
        self.excused_absences = 0
        self.unexcused_absences = 0

    def show_person_info(self):
        """
        It returns a string containing the name, surname, JMBG, date of birth, city of birth and country of birth of the
        person
        :return: a string with the name, surname, jmbg, date of birth, city of birth and country of birth.
        """
        return f"{self.name} {self.surname}\n{self.get_jmbg()}\n{self.get_date_of_birth()}\n{self.get_city_of_birth()}, {self.get_country_of_birth()}"

    def show_student_info(self):
        """
        It prints the student's name, surname, grade and grade class, then it prints the subjects and their grades, and
        finally it prints the number of excused and unexcused absences
        """
        print(f"{self.name} {self.surname} {self.grade}{self.grade_class}")
        grades = ""
        for subject in self.subjects:
            for i in range(len(self.subjects.get(subject))):
                grades += f"{str(self.subjects.get(subject)[i])}, "
            print(f"{subject}: {grades}")
            grades = ""
        print(f"Excused absence: {self.excused_absences}\nUnexcused absence: {self.unexcused_absences}")

    def add_subject_grade(self, subject: str, grade: int):
        """
        `add_subject_grade` adds a grade to a subject

        :param subject: The name of the subject
        :type subject: str
        :param grade: int
        :type grade: int
        """
        self.subjects.get(subject).append(grade)

    def get_final_grade_for_subject(self, subject: str):
        """
        It returns the average of all the grades for a given subject

        :param subject: str - the name of the subject
        :type subject: str
        :return: The average grade for a given subject.
        """
        try:
            count = 0
            sum = 0
            for grade in self.subjects.get(subject):
                sum += grade
                count += 1
            return round(sum / count)
        except ZeroDivisionError:
            pass

    def get_final_grade(self):
        """
        It returns the average of all the final grades for a student
        :return: The average of all the final grades for the subjects.
        """
        try:
            count = 0
            sum = 0
            for subject in self.subjects:
                if self.get_final_grade_for_subject(subject=subject) is not None:
                    sum += int(self.get_final_grade_for_subject(subject=subject))
                    count += 1
            return round(sum / count)
        except ZeroDivisionError:
            pass

    def show_grade_for_subject(self, subject: str):
        """
        This function takes in a string and prints the value of the key in the dictionary that matches the string

        :param subject: str
        :type subject: str
        """
        print(self.subjects[subject])

    def get_subjects(self):
        """
        It returns a list of all the subjects in the database
        :return: A list of the subjects in the class.
        """
        lst = []
        for subject in self.subjects:
            lst.append(subject)
        return lst

    def get_subjects_dict(self):
        """
        It returns a dictionary of subjects
        :return: The subjects dictionary is being returned.
        """
        return self.subjects

    def add_excused_absence(self):
        """
        This function adds one to the number of excused absences for a student
        """
        self.excused_absences += 1

    def add_unexcused_absence(self):
        """
        This function adds one to the number of unexcused absences for a student.
        """
        self.unexcused_absences += 1

