import typing as t
import random

from exeptions import *
from grade import Grade
from student import Student
from teacher import Teacher


class School:
    def __init__(self, name: str, teachers: t.List[Teacher], students: t.List[Student], id: str):
        self.name = name
        self.__students = students
        self.__teachers = teachers
        self.__elementary_teachers = []
        for teacher in self.__teachers:
            if len(teacher.subjects) > 1:
                self.__elementary_teachers.append(teacher)
                self.__teachers.remove(teacher)
        self.id = id
        self.grades = []

    def is_teacher_elder(self, teacher_id: str):
        """
        It checks if the teacher with the given id is the class elder of any of the classes in the school

        :param teacher_id: The id of the teacher
        :type teacher_id: str
        :return: A boolean value.
        """
        for grade in self.grades:
            for grade_class in grade.grade_classes:
                if grade_class.class_elder is not None:
                    if grade_class.class_elder.id == teacher_id:
                        return True

    def get_statistics(self):
        """
        It prints the number of students in the school, and then prints the percentage of students in each grade
        """
        num_of_students = len(self.__students)
        print(f"Number of students: {num_of_students}\n")
        for grade in self.grades:
            print(f"grade {grade.grade_num}: {round((len(grade.students) / num_of_students) * 100, 2)}%")

    def add_grade(self, grade: Grade):
        """
        This function adds a grade to the list of grades.

        :param grade: Grade
        :type grade: Grade
        """
        self.grades.append(grade)

    def get_school_id(self):
        """
        It returns the id of the school
        :return: The id of the school.
        """
        return self.id

    def get_students(self):
        """
        The function get_students() returns the value of the private variable __students
        :return: The list of students
        """
        return self.__students

    def get_students_jmbg(self):
        """
        It returns a list of jmbg's of all students in the class
        :return: List of students' jmbg
        """
        lst = []
        for stud in self.get_students():
            lst.append(stud.get_jmbg())
        return lst

    def get_students_id(self):
        """
        It returns a list of the ids of all the students in the class
        :return: A list of student ids
        """
        lst = []
        for student in self.get_students():
            lst.append(student.id)
        return lst

    def get_teachers(self):
        """
        It returns the value of the private variable __teachers
        :return: The list of teachers
        """
        return self.__teachers

    def get_teachers_jmbg(self):
        """
        It returns a list of jmbg's of all teachers in the school
        :return: List of jmbg's of all teachers
        """
        lst = []
        for teacher in self.get_teachers():
            lst.append(teacher.get_jmbg())
        return lst

    def get_teachers_id(self):
        """
        It returns a list of the ids of all the teachers of a given course
        :return: A list of the ids of the teachers of the course.
        """
        lst = []
        for teacher in self.get_teachers():
            lst.append(teacher.id)
        return lst

    def get_elementary_teachers(self):
        """
        This function returns the list of elementary teachers
        :return: The elementary teachers.
        """
        return self.__elementary_teachers

    def get_elementary_teachers_jmbg(self):
        """
        It returns a list of jmbg's of all elementary teachers
        :return: List of jmbg of elementary teachers
        """
        lst = []
        for elem_teach in self.get_elementary_teachers():
            lst.append(elem_teach.get_jmbg())
        return lst

    def get_elementary_teachers_id(self):
        """
        It returns a list of the ids of all the elementary teachers in the school
        :return: A list of the ids of the teachers in the elementary school.
        """
        lst = []
        for teacher in self.get_elementary_teachers():
            lst.append(teacher.id)
        return lst

    def add_student_to_school(self, student: Student):
        """
        It adds a student to a school, but if the student is already in the school, it raises an exception

        :param student: Student - the student that we want to add to the school
        :type student: Student
        """
        try:
            if student.get_jmbg() in self.get_students_jmbg():
                raise StudentAlreadyInSchoolExeption
            else:
                self.get_students().append(student)
        except StudentAlreadyInSchoolExeption as e:
            print(e)

    def expel_student_from_school(self, student: Student):
        """
        It removes a student from the school if the student is in the school

        :param student: Student - the student that will be expelled from the school
        :type student: Student
        """
        try:
            if student.get_jmbg() not in self.get_students_jmbg():
                raise StudentNotInSchoolExeption
            else:
                self.get_students().remove(student)
        except StudentNotInSchoolExeption as e:
            print(e)

    def hire_teacher(self, teacher: Teacher):
        """
        It adds a teacher to the school, but if the teacher is already in the school, it raises an exception

        :param teacher: Teacher
        :type teacher: Teacher
        """
        try:
            if teacher.get_jmbg() in self.get_elementary_teachers_jmbg() or teacher.get_jmbg() in self.get_teachers_jmbg():
                raise TeacherAlreadyInSchoolExeption
            else:
                if len(teacher.subjects) > 1:
                    self.get_elementary_teachers().append(teacher)
                else:
                    self.get_teachers().append(teacher)
        except TeacherAlreadyInSchoolExeption as e:
            print(e)

    def fire_teacher(self, teacher: Teacher):
        """
        The function fire_teacher() takes a teacher object as an argument and removes it from the list of teachers in the
        school

        :param teacher: Teacher - the teacher to be fired
        :type teacher: Teacher
        """
        try:
            if teacher.get_id() not in self.get_elementary_teachers_id() and teacher.get_id() not in self.get_teachers_id():
                raise TeacherNotInSchoolExeption
            else:
                if len(teacher.subjects) > 1:
                    self.get_elementary_teachers().remove(teacher)
                else:
                    self.get_teachers().remove(teacher)
        except TeacherNotInSchoolExeption as e:
            print(e)

    def transfer_student(self, student: Student, school: "School"):
        """
        "This function takes in a student and a school, and transfers the student from the current school to the new
        school."

        The function is called transfer_student, and it takes in two parameters: student and school. The student parameter
        is a Student object, and the school parameter is a School object

        :param student: Student - This is the student that you want to transfer
        :type student: Student
        :param school: School
        :type school: "School"
        """
        self.expel_student_from_school(student=student)
        school.add_student_to_school(student=student)

    def get_id_for_new_teacher(self):
        """
        It takes a list of teacher ids and returns the next available id
        :return: The new id for a teacher.
        """
        lst = []
        for id in self.get_teachers_id():
            lst.append(int(id))
        for id in self.get_elementary_teachers_id():
            lst.append(int(id))
        new_id = str(max(lst) + 1)
        return new_id

    def get_id_for_new_student(self):
        """
        It takes a list of student IDs, converts them to integers, finds the maximum value, adds 1 to it, and returns the
        result as a string.
        :return: the id of the new student.
        """
        lst = []
        for id in self.get_students_id():
            lst.append(int(id))
        new_id = str(max(lst) + 1)
        return new_id

    def extract_schools_subjects(self):
        """
        It returns a list of all the subjects taught by all the teachers in the school
        :return: A list of all the subjects taught by all the teachers in the school.
        """
        lst = []
        for teacher in (self.get_teachers() + self.get_elementary_teachers()):
            for subject in teacher.subjects:
                lst.append(subject.name)
        return lst

    def assign_grade_class_elders(self):
        """
        For each grade in the school, if the grade is in the elementary grades, then for each grade class in the grade,
        assign a random elementary teacher to be the class elder. If the grade is in the middle school grades, then for each
        grade class in the grade, assign a random middle school teacher to be the class elder
        """
        if self.get_teachers() + self.get_elementary_teachers():
            for grade in self.grades:
                if grade.grade_num in ["I", "II", "III", "IV"]:
                    for grade_class in grade.grade_classes:
                        grade_class.class_elder = random.choice(self.get_elementary_teachers())
                elif grade.grade_num in ["V", "VI", "VII", "VIII"]:
                    for grade_class in grade.grade_classes:
                        grade_class.class_elder = random.choice(self.get_teachers())
                else:
                    pass



