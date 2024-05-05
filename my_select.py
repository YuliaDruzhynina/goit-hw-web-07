from sqlalchemy import desc, func
from connect_db import session
from model import Student, Teacher, Group, Subject, Grade


def select_1(session):
    query = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5)
    return query.all()

def select_2(session, subject_name):  
    query = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.subject_name == subject_name) \
        .group_by(Student.id).order_by(desc('avg_grade')).limit(1)
    return query.first()


def select_3(session, subject_name):
    query = session.query(Subject.subject_name, Group.group_name, func.round(func.avg(Grade.grade), 2) \
        .label('avg_grade')) \
        .select_from(Grade).join(Student).join(Group).join(Subject).filter(Subject.subject_name==subject_name)  \
        .group_by(Group.group_name)
    return query.all()  

def select_4(session):
    query = session.query(Group.group_name, func.round(func.avg(Grade.grade))) \
        .select_from(Grade).join(Student).join(Group) \
        .group_by(Group.id)
    return query.all()

# def select_4(session):
#     query = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#     return query.first()

def select_5(session, teacher_name):
    query = session.query(Subject.subject_name) \
        .select_from(Subject).join(Teacher).filter(Teacher.teacher_name == teacher_name)
    return query.all()

def select_6(session, group_name):
    query = session.query(Student.fullname) \
        .select_from(Student).join(Group).filter(Group.group_name == group_name)
    return query.all()

def select_7(session, subject_name, group_name):
    query = session.query(Group.group_name, Student.fullname, Grade.grade) \
        .select_from(Student).join(Group).filter(Group.id==group_name).join(Grade).join(Subject) \
        .filter(Subject.subject_name==subject_name) \
        .group_by(Group.group_name)
    return query.all()

def select_8(session, teacher_name):
    query = session.query(Teacher.teacher_name, Subject.subject_name, func.round(func.avg(Grade.grade), 2) \
        .label('avg_grade')) \
        .select_from(Teacher).filter(Teacher.teacher_name==teacher_name).join(Subject).join(Grade) \
        .group_by(Teacher.teacher_name)
    return query.all()

def select_9(session, student_name):
    query = session.query(Subject.subject_name) \
        .select_from(Subject).join(Grade).join(Student).filter(Student.fullname==student_name) \
        .group_by(Subject.id)
    return query.all()

def select_10(session, fullname, teacher_name):
    query = session.query(Subject.subject_name) \
        .select_from(Grade).join(Subject).join(Teacher).filter(Teacher.teacher_name==teacher_name) \
        .join(Student).filter(Student.fullname==fullname)
    return query.all()   


if __name__ == '__main__':

    result_1 = select_1(session)
    print("5 студентів із найбільшим середнім балом з усіх предметів:", result_1)
    result_2 = select_2(session, 'Physics')
    print("Студент із найвищим середнім балом з фізики:", result_2)
    result_3 = select_3(session, 'Physics')
    print("середній бал у групах з фізики:", result_3)
    result_4 = select_4(session)
    print("середній бал на потоці по всій таблиці оцінок:", result_4)
    result_5 = select_5(session, 'Єфрем Ярема')
    print("які курси читає фрем Ярема:", result_5)
    result_6 = select_6(session, 'Group C')
    print("список студентів у  групі Group C:", result_6)
    result_7 = select_7(session, 'Group C', 'Physics')
    print("список студентів у групі Group C:", result_7)
    result_8= select_8(session,'Антон Фаренюк')
    print("середній бал, який ставить Антон Фаренюк зі своїх предметів:", result_8)
    result_9= select_9(session,'Руслан Гаврилів')
    print("список курсів, які відвідує студент Руслан Гаврилів:", result_9)
    result_10= select_10(session,'Руслан Гаврилів', 'Антон Фаренюк')
    print("список курсів, які відвідує студент Руслан Гаврилів у викладача Антон Фаренюк:", result_10)
