import random
from faker import Faker
from connect_db import session
from model import Student, Teacher, Group, Subject, Grade

fake = Faker('uk_UA')


def add_groups():
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        group = Group(group_name=group_name)
        session.add(group)
    session.commit()


def add_students():
    for _ in range(1, 31):
        student = Student(
            fullname=fake.name(),
            student_phone=fake.phone_number(),
            student_email=fake.email()
        )
        session.add(student)
    session.commit()


def add_teachers():
    for _ in range(1, 4):
        teacher = Teacher(
            teacher_name=fake.name(),
            teacher_phone=fake.phone_number(),
            teacher_email=fake.phone_number()
        )
        session.add(teacher)
    session.commit()

# def add_groups():
#     for _ in range(1,4):
#         group = Group(
#         group_name = fake.name(),
#         id=fake.random_element(elements=range(1, 4))
#      )
#         session.add(group)  


def add_subjects():
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    for subject_name in subjects:
        subject = Subject(subject_name=subject_name)
        session.add(subject)
    session.commit()


def add_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for subject in subjects:
            num_grades = random.randint(1, 20)
            for _ in range(num_grades):
                date_received = fake.date_time_between(start_date='-30d', end_date='now')
                grade = Grade(student_id=student.id, subject_id=subject.id, grade=random.uniform(1, 10), grade_date=date_received)
                session.add(grade)
    session.commit()    


if __name__ == '__main__':
    add_groups()
    add_students()
    add_teachers()
    add_grades()
    add_subjects()
