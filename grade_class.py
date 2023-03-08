from student import Student


class GradeClass:
    def __init__(self, grade: str, grade_class_num: str):
        self.grade = grade
        self.grade_class_num = grade_class_num
        self.class_elder = None
        self.students = []

    def show_grade_class_status(self):
        """
        It prints the name and surname of each student in the class, along with the subjects they are taking
        """
        for student in self.students:
            print(f"{student.name} {student.surname}: {student.subjects}")

    def show_elder(self):
        """
        It returns the class_elder of the class.
        :return: The class_elder attribute of the class.
        """
        return f"{self.class_elder.name} {self.class_elder.surname}"

    def is_teacher_elder_in_grade_class(self, teacher_id: str):
        """
        It checks if the teacher is the class elder.

        :param teacher_id: The teacher's ID
        :type teacher_id: str
        :return: True or False
        """
        if self.class_elder.id == teacher_id:
            return True

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

    def transfer_student(self, student: Student, grade_class: "GradeClass"):
        """
        > This function removes a student from a grade class and adds them to another grade class.

        :param student: Student - The student to be transferred
        :type student: Student
        :param grade_class: The grade class that the student is being transferred to
        :type grade_class: "GradeClass"
        """
        self.remove_student(student=student)
        grade_class.add_student(student=student)

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
        It returns the average grade for a given subject

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

    def extract_students(self):
        """
        It returns the list of students in the class
        :return: The students list is being returned.
        """
        return self.students
