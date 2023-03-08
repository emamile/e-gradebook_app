class Exception(Exception):
    def __init__(self, message):
        super().__init__(message)


class StudentAlreadyInSchoolException(Exception):
    def __init__(self):
        super().__init__("We already have that student in school.")


class StudentNotInSchoolException(Exception):
    def __init__(self):
        super().__init__("We don't have that student at our school.")


class TeacherAlreadyInSchoolException(Exception):
    def __init__(self):
        super().__init__("We already have that teacher in school.")


class TeacherNotInSchoolException(Exception):
    def __init__(self):
        super().__init__("We don't have that teacher at our school.")


class OptionException(Exception):
    def __init__(self):
        super().__init__("We don't have that option.")


class SchoolNotInSystemException(Exception):
    def __init__(self):
        super().__init__("We don't have that school in our database.")


class TeacherIsNotElderException(Exception):
    def __init__(self):
        super().__init__("Teacher is not grade class elder.")


class IsNotTeachersSubjectException(Exception):
    def __init__(self):
        super().__init__("This is not your subject, you can't grade it.")


class GradeOutOfRangeException(Exception):
    def __init__(self):
        super().__init__("Grade must be in range 1-5.")


class NoSuchSubjectException(Exception):
    def __init__(self):
        super().__init__("There's no such subjcet.")


class TransferStudentException(Exception):
    def __init__(self):
        super().__init__("Student can't be transfered to the same school.")


class TransferStudentToGradeClassException(Exception):
    def __init__(self):
        super().__init__("Student can't be transfered to the same grade class.")