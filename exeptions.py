class Exeption(Exception):
    def __init__(self, message):
        super().__init__(message)


class StudentAlreadyInSchoolExeption(Exeption):
    def __init__(self):
        super().__init__("We already have that student in school.")


class StudentNotInSchoolExeption(Exeption):
    def __init__(self):
        super().__init__("We don't have that student at our school.")


class TeacherAlreadyInSchoolExeption(Exeption):
    def __init__(self):
        super().__init__("We already have that teacher in school.")


class TeacherNotInSchoolExeption(Exeption):
    def __init__(self):
        super().__init__("We don't have that teacher at our school.")


class OptionExeption(Exception):
    def __init__(self):
        super().__init__("We don't have that option.")


class SchoolNotInSystemExeption(Exception):
    def __init__(self):
        super().__init__("We don't have that school in our database.")


class TeacherIsNotElderExeption(Exception):
    def __init__(self):
        super().__init__("Teacher is not grade class elder.")


class IsNotTeachersSubjectExeption(Exception):
    def __init__(self):
        super().__init__("This is not your subject, you can't grade it.")


class GradeOutOfRangeExeption(Exception):
    def __init__(self):
        super().__init__("Grade must be in range 1-5.")


class NoSuchSubjectExeption(Exception):
    def __init__(self):
        super().__init__("There's no such subjcet.")


class TransferStudentExeption(Exception):
    def __init__(self):
        super().__init__("Student can't be transfered to the same school.")


class TransferStudentToGradeClassExeption(Exception):
    def __init__(self):
        super().__init__("Student can't be transfered to the same grade class.")