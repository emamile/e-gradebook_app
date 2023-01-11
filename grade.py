import typing as t

from projekat.grade_class_class import GradeClass
from projekat.student_class import Student
from projekat.subjects_class import Subject


class Grade:
    def __init__(self, grade_num: str, subjects: t.List[Subject], students: t.List[Student]):
        self.grade_num = grade_num
        self.students = students
        self.subjects = subjects
        self.grade_classes = []

    def add_grade_class(self, grade_class: GradeClass):
        """
        This function adds a grade class to the list of grade classes.

        :param grade_class: The grade class to add to the list of grade classes
        :type grade_class: GradeClass
        """
        self.grade_classes.append(grade_class)

    def extract_grade_classes(self):
        """
        It takes a list of grade classes and returns a list of the names of those grade classes
        :return: A list of the grade_class_name attribute of each grade_class object in the grade_classes list.
        """
        lst = []
        for grd_class in self.grade_classes:
            lst.append(grd_class.grade_class_name)
        return lst

    def assign_subjects_to_students(self):
        """
        For each student in the school, add a dictionary entry for each subject in the school, with the key being the
        subject name and the value being an empty list.
        """
        for student in self.students:
            for subject in self.subjects:
                student.subjects.update({subject.name: []})

    def assign_subjects_to_one_student(self, student: Student):
        """
        It takes a student and assigns them all the subjects in the school

        :param student: Student - this is the student that we want to assign subjects to
        :type student: Student
        """
        for subject in self.subjects:
            student.subjects.update({subject: []})

    def add_subject(self, subject: Subject):
        """
        Add a subject to the list of subjects.

        :param subject: Subject - The subject to add to the list of subjects
        :type subject: Subject
        """
        self.subjects.append(subject)

    def extract_subjects(self):
        """
        It returns the list of subjects for a given student
        :return: The subjects are being returned.
        """
        return self.subjects

    def add_student(self, student: Student):
        """
        Add a student to the list of students.

        :param student: Student - This is the student object that we want to add to the list of students
        :type student: Student
        """
        self.students.append(student)

    def remove_student(self, student: Student):
        """
        Remove a student from the list of students.

        :param student: Student - This is the student object that we want to remove from the list
        :type student: Student
        """
        self.students.remove(student)

    def get_best_student(self):
        """
        It loops through all the students in the class, and returns the student with the highest final grade
        :return: The student with the highest final grade.
        """
        wanted_student = self.students[0]
        for student in self.students[1:]:
            if student.get_final_grade() > wanted_student.get_final_grade():
                wanted_student = student
        return wanted_student

    def get_average_grade_for_subject(self, subject: str):
        """
        It takes a subject as a parameter, and returns the average grade for that subject

        :param subject: str
        :type subject: str
        :return: The average grade for a given subject.
        """
        try:
            count = 0
            sum = 0
            for student in self.students:
                for i in range(len(student.subjects.get(subject))):
                    sum += student.get_subjects_dict().get(subject)[i]
                    count += 1
            return round(sum / count, 2)
        except ZeroDivisionError:
            pass


