"""Welcome to e-gradebook.
You can log in as school, teacher, or student.
When you do log in successfully, in terminal you will see possible options you can make.
There is already a database, but it can be changed through interaction with terminal.
When program starts, students are not graded for any subject they attend, teacher must grade them before any grade data can be shown
Options to be added: jmbg validation, usage of serialization and deserialization (nisam stigla ali bih volela da dodam ako imam mogucnosti)"""
import os
import random
from projekat.exeptions_class import *
from data_load import *
from projekat.txt import *


def main():

    while True:
        option = input("Welcome to e-gradebook! How would you like to register as? (school/teacher/student/exit): ")
        try:
            if option == "school":
                school_id = input("Enter school id: ")
                try:
                    if school_id not in schools_ids:
                        raise SchoolNotInSystemExeption
                    else:
                        for school in schools:
                            if school_id == school.get_school_id():
                                while True:
                                    option_1 = input(f"Welcome, {school.name}.\n"
                                                         f"Options:\n"
                                                         f"a) See school statistics\n"
                                                         f"b) Hire teacher\n"
                                                         f"c) Fire teacher\n"
                                                         f"d) Enroll student in school\n"
                                                         f"e) Withdraw student from school\n"
                                                         f"f) Transfer student to another school\n"
                                                         f"g) Show teachers in employment\n"
                                                         f"h) Show students attending school\n"
                                                         f"i) Show best student in every grade\n"
                                                         f"j) Transfer student to another grade class\n"                                                 
                                                         f"Enter option you would like to continue with (a-j/exit): ")
                                    try:
                                        if option_1 == "a":
                                            school.get_statistics()
                                        elif option_1 == "b":
                                            teacher = Teacher(name=input("Insert name: "), surname=input("Insert surname: "), jmbg=input("Insert jmbg: "), date_of_birth=input("Insert date of birth: "), country_of_birth=input("Insert country of birth: "), city_of_birth=input("Insert city of birth: "), subjects=[], id=school_ck.get_id_for_new_teacher())
                                            subject = input("Insert teacher's subject? (elementary, serbian, english, math, art, music, history, biology, geography, chemistry, physics, physical, technology, computer science): ")
                                            try:
                                                if teacher.get_id() in (school.get_teachers_id() + school.get_elementary_teachers_id()):
                                                    raise TeacherAlreadyInSchoolExeption
                                                else:
                                                    try:
                                                        if subject == "elementary":
                                                            for sub in elementary_grade_subjects:
                                                                teacher.add_subject(subject=sub)
                                                        else:
                                                            if subject not in higher_grade_subjects_names:
                                                                raise OptionExeption
                                                            else:
                                                                for subj in higher_grade_subjects:
                                                                    if subject == subj.name:
                                                                        teacher.add_subject(subject=subj)
                                                        school.hire_teacher(teacher=teacher)
                                                    except OptionExeption as e:
                                                        print(e)
                                            except TeacherAlreadyInSchoolExeption as taise:
                                                print(taise)
                                        elif option_1 == "c":
                                            teacher_id = input("Enter teachers id: ")
                                            try:
                                                if teacher_id not in (school.get_teachers_id() + school.get_elementary_teachers_id()):
                                                    raise TeacherNotInSchoolExeption
                                                else:
                                                    for teacher in school.get_teachers():
                                                        if teacher_id == teacher.get_id():
                                                            school.fire_teacher(teacher=teacher)
                                            except TeacherNotInSchoolExeption as tnise:
                                                print(tnise)
                                        elif option_1 == "d":
                                            student = Student(name=input("Insert name: "), surname=input("Insert surname: "), jmbg=input("Insert jmbg: "), date_of_birth=input("Insert date of birth: "), country_of_birth=input("Insert country of birth: "), city_of_birth=input("Insert city of birth: "), grade="", grade_class="", id=school_ck.get_id_for_new_student())
                                            try:
                                                if student.id in school.get_students_id():
                                                    raise StudentAlreadyInSchoolExeption
                                                else:
                                                    school.add_student_to_school(student=student)
                                                    wanted_grade = input("Enter grade you would like to enroll student in (I-VIII): ")
                                                    try:
                                                        if wanted_grade not in grade_names:
                                                            raise OptionExeption
                                                        else:
                                                            for grade in school.grades:
                                                                if wanted_grade == grade.grade_num:
                                                                    grade.add_student(student=student)
                                                                    grade_class = random.choice(grade.grade_classes)
                                                                    grade_class.add_student(student=student)
                                                    except OptionExeption as e:
                                                        print(e)
                                            except StudentAlreadyInSchoolExeption as saise:
                                                print(saise)
                                        elif option_1 == "e":
                                            student_id = input("Enter students id: ")
                                            try:
                                                if student_id not in school.get_students_id():
                                                    raise StudentNotInSchoolExeption
                                                else:
                                                    for student in school.get_students():
                                                        if student_id == student.get_id():
                                                            school.expel_student_from_school(student=student)
                                            except StudentNotInSchoolExeption as snise:
                                                print(snise)
                                        elif option_1 == "f":
                                            student_id = input("Enter students id: ")
                                            new_school_id = input("To which school you want to transfer student? (enter schools id): ")
                                            try:
                                                if student_id not in school.get_students_id():
                                                    raise StudentNotInSchoolExeption
                                                else:
                                                    try:
                                                        if new_school_id not in schools_ids:
                                                            raise SchoolNotInSystemExeption
                                                        elif new_school_id == school.get_school_id():
                                                            raise TransferStudentExeption
                                                        else:
                                                            for student in school.get_students():
                                                                if student_id == student.id:
                                                                    for transfer_school in schools:
                                                                        if new_school_id == transfer_school.get_school_id():
                                                                            school.transfer_student(student=student, school=transfer_school)
                                                    except SchoolNotInSystemExeption as snise:
                                                        print(snise)
                                                    except TransferStudentExeption as tse:
                                                        print(tse)
                                            except StudentNotInSchoolExeption as snise:
                                                print(snise)
                                        elif option_1 == "g":
                                            for teacher in (school.get_teachers() + school.get_elementary_teachers()):
                                                if len(teacher.subjects) > 1:
                                                    print(f"{teacher.name} {teacher.surname}, elementary teacher")
                                                else:
                                                    print(f"{teacher.name} {teacher.surname}, {teacher.subjects[0].name}")
                                        elif option_1 == "h":
                                            for student in school.get_students():
                                                print(f"{student.name} {student.surname} {student.grade}{student.grade_class}")
                                        elif option_1 == "i":
                                            for grade in school.grades:
                                                print(f"Best student for grade {grade.grade_num} is {grade.get_best_student().name} {grade.get_best_student().surname}")
                                        elif option_1 == "j":
                                            stud_id = input("Enter student id: ")
                                            try:
                                                if stud_id not in school.get_students_id():
                                                    raise StudentNotInSchoolExeption
                                                else:
                                                    for student in school.get_students():
                                                        if stud_id == student.id:
                                                            for grd in school.grades:
                                                                if student in grd.students:
                                                                    grd_class = input("Enter grade class you would like to transfer student in: ")
                                                                    try:
                                                                        if grd_class not in grd.extract_grade_classes():
                                                                            raise OptionExeption
                                                                        elif grd_class == student.grade_class:
                                                                            raise TransferStudentToGradeClassExeption
                                                                        else:
                                                                            for grd_classs in grd.grade_classes:
                                                                                if grd_classs.grade_class_name == grd_class:
                                                                                    for grd_classss in grd.grade_classes:
                                                                                        if student.grade_class == grd_classss.grade_class_name:
                                                                                            grd_classss.transfer_student(student=student, grade_class=grd_classs)
                                                                    except OptionExeption as e:
                                                                        print(e)
                                                                    except TransferStudentToGradeClassExeption as tstgce:
                                                                        print(tstgce)
                                            except StudentNotInSchoolExeption as snise:
                                                print(snise)
                                        elif option_1 == "exit":
                                            break
                                        else:
                                            raise OptionExeption
                                    except OptionExeption as e:
                                        print(e)
                except SchoolNotInSystemExeption as snise:
                    print(snise)
            elif option == "teacher":
                school_id = input("Enter your working schools id:  ")
                teacher_id = input("Enter teacher id: ")
                try:
                    if school_id not in schools_ids:
                        raise SchoolNotInSystemExeption
                    else:
                        for school in schools:
                            if school_id == school.get_school_id():
                                try:
                                    if teacher_id not in (school.get_teachers_id() + school.get_elementary_teachers_id()):
                                        raise TeacherNotInSchoolExeption
                                    else:
                                        for teacher in (school.get_teachers() + school.get_elementary_teachers()):
                                            if teacher_id == teacher.get_id():
                                                while True:
                                                    option_2 = input(f"Welcome, {teacher.name} {teacher.surname}.\n"
                                                                     f"Options:\n"
                                                                     f"a) See grade class status\n"
                                                                     f"b) Add grade\n"
                                                                     f"c) Finalize grades\n"
                                                                     f"d) Add excused/unexcused absence\n"
                                                                     f"e) Show personal info\n"
                                                                     f"Enter option you would like to continue with (a-f/exit): ")
                                                    if option_2 == "a":
                                                        try:
                                                            if school.is_teacher_elder(teacher_id=teacher.get_id()):
                                                                for grade in school.grades:
                                                                    for grade_class in grade.grade_classes:
                                                                        if grade_class.is_teacher_elder_in_grade_class(teacher_id=teacher.get_id()):
                                                                            grade_class.show_grade_class_status()
                                                            else:
                                                                raise TeacherIsNotElderExeption
                                                        except TeacherIsNotElderExeption as tinee:
                                                            print(tinee)
                                                    elif option_2 == "b":
                                                        student_id = input("Enter students id: ")
                                                        try:
                                                            if student_id not in school.get_students_id():
                                                                raise StudentNotInSchoolExeption
                                                            else:
                                                                grade_for_sub = int(input("Enter grade: "))
                                                                try:
                                                                    if 1 <= grade_for_sub <= 5:
                                                                        for student in school.get_students():
                                                                            if student.id == student_id:
                                                                                for grade in school.grades:
                                                                                    if student in grade.students:
                                                                                        for grade_class in grade.grade_classes:
                                                                                            if student in grade_class.extract_students():
                                                                                                if student.grade in ["I", "II", "III", "IV"]:
                                                                                                    try:
                                                                                                        if grade_class.is_teacher_elder_in_grade_class(teacher_id=teacher.get_id()):
                                                                                                            subject = input("Enter subject you want to grade (math, serbian, english, physical, world around us, nature and society, music, art): ")
                                                                                                            try:
                                                                                                                if subject not in school.extract_schools_subjects():
                                                                                                                    raise NoSuchSubjectExeption
                                                                                                                else:
                                                                                                                    try:
                                                                                                                        if subject not in teacher.extract_subject_names():
                                                                                                                            raise IsNotTeachersSubjectExeption
                                                                                                                        else:
                                                                                                                            for sub in teacher.subjects:
                                                                                                                                if str(sub.name) == subject:
                                                                                                                                    student.subjects.get(subject).append(int(grade_for_sub))
                                                                                                                    except IsNotTeachersSubjectExeption as intse:
                                                                                                                        print(intse)
                                                                                                            except NoSuchSubjectExeption as nsse:
                                                                                                                print(nsse)
                                                                                                        else:
                                                                                                            raise TeacherIsNotElderExeption
                                                                                                    except TeacherIsNotElderExeption as tinee:
                                                                                                        print(tinee)
                                                                                                else:
                                                                                                    subject = input("Enter subject you want to grade (math, serbian, english, physical, music, art, history, biology, geography, physics, technology, computer science, chemistry): ")
                                                                                                    try:
                                                                                                        if subject not in school.extract_schools_subjects():
                                                                                                            raise NoSuchSubjectExeption
                                                                                                        else:
                                                                                                            try:
                                                                                                                for sub in teacher.subjects:
                                                                                                                    if sub.name == subject:
                                                                                                                        student.subjects.get(subject).append(int(grade_for_sub))
                                                                                                                else:
                                                                                                                    raise IsNotTeachersSubjectExeption
                                                                                                            except IsNotTeachersSubjectExeption as e:
                                                                                                                print(e)
                                                                                                    except NoSuchSubjectExeption as nsse:
                                                                                                        print(nsse)
                                                                    else:
                                                                        raise GradeOutOfRangeExeption
                                                                except GradeOutOfRangeExeption as e:
                                                                    print(e)
                                                        except StudentNotInSchoolExeption as e:
                                                            print(e)
                                                    elif option_2 == "c":
                                                        student_id = input("Enter students id: ")
                                                        try:
                                                            if student_id not in school.get_students_id():
                                                                raise StudentNotInSchoolExeption
                                                            else:
                                                                for student in school.get_students():
                                                                    if student.id == student_id:
                                                                        for grade in school.grades:
                                                                            if student in grade.students:
                                                                                for grade_class in grade.grade_classes:
                                                                                    if student in grade_class.extract_students:
                                                                                        if student.grade in ["I", "II", "III", "IV"]:
                                                                                            try:
                                                                                                if grade_class.is_teacher_elder_in_grade_class(teacher_id=teacher.get_id()):
                                                                                                    for subject in student.subjects:
                                                                                                        student.get_final_grade_for_subject(subject=subject)
                                                                                                        print(f"Final grade for subject {subject} is {student.get_final_grade_for_subject(subject=subject)}")
                                                                                                else:
                                                                                                    raise TeacherIsNotElderExeption
                                                                                            except TeacherIsNotElderExeption as tinee:
                                                                                                print(tinee)
                                                                                        else:
                                                                                            student.get_final_grade_for_subject(subject=teacher.subjects[0].name)
                                                                                            print(f"Final grade for subject {teacher.subjects[0].name} is {student.get_final_grade_for_subject(subject=teacher.subjects[0].name)}")

                                                        except StudentNotInSchoolExeption as snise:
                                                            print(snise)
                                                    elif option_2 == "d":
                                                        student_id = input("Enter students id: ")
                                                        try:
                                                            if student_id not in school_ck.get_students_id():
                                                                raise StudentNotInSchoolExeption
                                                            else:
                                                                for student in school_ck.get_students():
                                                                    if student.id == student_id:
                                                                        for grade in school_ck.grades:
                                                                            if student in grade.students:
                                                                                for grade_class in grade.grade_classes:
                                                                                    if student in grade_class.extract_students:
                                                                                        try:
                                                                                            if grade_class.is_teacher_elder_in_grade_class(teacher_id=teacher.get_id()):
                                                                                                absence = input("What absence do you want to add (excused/unexcused)?:  ")
                                                                                                try:
                                                                                                    if absence == "excused":
                                                                                                        student.add_excused_absence()
                                                                                                        print(f"You added excused absence to student {student.name} {student.surname}, excused absence current number is {student.excused_absences}")
                                                                                                    elif absence == "unexcused":
                                                                                                        student.add_unexcused_absence()
                                                                                                        print(f"You added unexcused absence to student {student.name} {student.surname}, unexcused absence current number is {student.unexcused_absences}")
                                                                                                    else:
                                                                                                        raise OptionExeption
                                                                                                except OptionExeption as e:
                                                                                                    print(e)
                                                                                            else:
                                                                                                raise TeacherIsNotElderExeption
                                                                                        except TeacherIsNotElderExeption as tinee:
                                                                                            print(tinee)
                                                        except StudentNotInSchoolExeption as snise:
                                                            print(snise)
                                                    elif option_2 == "e":
                                                        print(teacher.show_person_info())
                                                    elif option_2 == "exit":
                                                        break
                                except TeacherNotInSchoolExeption as tnise:
                                    print(tnise)
                except SchoolNotInSystemExeption as snise:
                    print(snise)
            elif option == "student":
                school_id = input("Enter school id: ")
                student_id = input("Enter student id: ")
                try:
                    if school_id not in schools_ids:
                        raise SchoolNotInSystemExeption
                    else:
                        for school in schools:
                            if school.get_school_id() == school_id:
                                try:
                                    if student_id not in school.get_students_id():
                                        raise StudentNotInSchoolExeption
                                    else:
                                        for stud in school.get_students():
                                            if stud.id == student_id:
                                                while True:
                                                    option_3 = input(f"Welcome, {stud.name} {stud.surname}.\n"
                                                                     f"Options:\n"
                                                                     f"a) Show personal info \n"
                                                                     f"b) Show student info\n"
                                                                     f"Enter option you would like to continue with (a-b/exit): ")
                                                    try:
                                                        if option_3 == "a":
                                                            print(stud.show_person_info())
                                                        elif option_3 == "b":
                                                            stud.show_student_info()
                                                        elif option_3 == "exit":
                                                            break
                                                        else:
                                                            raise OptionExeption
                                                    except OptionExeption as e:
                                                        print(e)
                                except StudentNotInSchoolExeption as snise:
                                    print(snise)
                except SchoolNotInSystemExeption as snise:
                    print(snise)
            elif option == "exit":
                print("Thank you for using our e-gradebook!")
                root = os.path.join(os.getcwd(), "DATA_BASE")
                root = create_dir_if_not_exists(root)
                bodyy = ""
                for school in schools:
                    for stud in school.get_students():
                        bodyy += f"{stud.show_person_info()}\n"
                        create_files(root=root, dir=school.name, title="students",
                                     body=bodyy, dir_1="", dir_2="",
                                     dir_3="", dir_4="")
                    bodyy = ""
                    for teach in (school.get_teachers() + school.get_elementary_teachers()):
                        bodyy += f"{teach.show_person_info()}\n"
                        create_files(root=root, dir=school.name, title="teachers",
                                     body=bodyy, dir_1="", dir_2="",
                                     dir_3="", dir_4="")
                    bodyy = ""
                    for grade in school.grades:
                        for grade_class in grade.grade_classes:
                            for sub in grade.subjects:
                                create_files(root=root, dir=school.name,
                                                title=f"{grade.grade_num}_{grade_class.grade_class_num}_{sub.name}",
                                                body=f"{sub.name}: {grade_class.get_average_grade_for_subject(subject=sub.name)}\n",
                                                dir_1="average_grade_for_subjects_per_grade_class", dir_2="",
                                                dir_3="", dir_4="")
                                create_files(root=root, dir=school.name,
                                                title=f"{grade.grade_num}_{sub.name}",
                                                body=f"{sub.name}: {grade.get_average_grade_for_subject(subject=sub.name)}\n",
                                                dir_1="average_grade_for_subjects_per_grade", dir_2="",
                                                dir_3="", dir_4="")
                            for student in grade_class.students:
                                gradess = ""
                                body = ""
                                for subject in student.subjects:
                                    for i in range(len(student.subjects.get(subject))):
                                        gradess += f"{str(student.subjects.get(subject)[i])}, "
                                    body += f"{subject}: {gradess}\n"
                                    gradess = ""
                                body += f"Excused absence: {student.excused_absences}\nUnexcused absence: {student.unexcused_absences}"
                                create_files(root=root, dir=school.name, title="grades", body=body,
                                                dir_1="students",
                                                dir_2=grade.grade_num, dir_3=grade_class.grade_class_num,
                                                dir_4=f"{student.name}_{student.surname}")
                                gradee = ""
                                body = ""
                                for subject in student.subjects:
                                    gradee += f"{student.get_final_grade_for_subject(subject=subject)}"
                                    body += f"{subject}: {gradee}\n"
                                    gradee = ""
                                body += f"Excused absence: {student.excused_absences}\nUnexcused absence: {student.unexcused_absences}\nfinal grade: {student.get_final_grade()}"
                                create_files(root=root, dir=school.name, title="final_grades", body=body,
                                                dir_1="students",
                                                dir_2=grade.grade_num, dir_3=grade_class.grade_class_num,
                                                dir_4=f"{student.name}_{student.surname}")
                break
            else:
                raise OptionExeption
        except OptionExeption as e:
            print(e)


if __name__ == "__main__":

    main()




