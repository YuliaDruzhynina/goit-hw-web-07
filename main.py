from sqlalchemy import desc, func
from connect_db import session
from model import Student, Teacher, Group, Subject, Grade


if __name__ == '__main__':
    session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc(Grade.grade)).limit(5).all()

    session.query(Student.fullname, Student.id, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id, Student.fullname).order_by(
        desc(Grade.grade)).limit(5).all()

    session.query(Group.id, Group.group_name, Subject.subject_name,func.round(func.avg(Grade.grade), 2)) \
        .select_from(Group).join(Grade).join(Subject).filter(Subject.subject_name == 'Chemistry') \
        .group_by(Group.id, Group.group_name).all()

    session.query(Group.group_name, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Group).join(Subject).group_by(Group.group_name).all()

    session.query(Teacher.id, Teacher.teacher_name, Subject.id, Subject.subject_name) \
        .select_from(Teacher).join(Subject).filter(Teacher.teacher_name == 'Мартин Хорішко').all()

    session.query(Student.id, Student.fullname, Group.group_name) \
        .select_from(Student).join(Group).filter(Group.group_name == 'Group B').all()

    session.query(Group.id, Group.group_name, Student.id, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Group).join(Subject).group_by(Group.group_name).all()

    session.query(Teacher.id, Teacher.teacher_name, Subject.id, Subject.subject_name) \
        .select_from(Subject).join(Teacher).filter(Teacher.id == '3').join(Grade) \
        .group_by(Teacher.teacher_name, Subject.subject_name).all()

    session.query(Student.id, Student.fullname, Subject.subject_name) \
        .select_from(Student).join(Grade).join(Subject).filter(Student.id == '3') \
        .group_by(Subject.subject_name).order_by(Subject.subject_name).all()

    session.query(Student.id, Student.fullname, Teacher.id, Teacher.teacher_name, Subject.subject_name) \
        .select_from(Subject).join(Teacher).filter(Teacher.teacher_name == 'Мартин Хорішко').join(Grade) \
        .join(Student).filter(Student.id == '3').group_by(Subject.id, Student.id).all()

    session.query(Teacher.teacher_name, Student.id, Student.fullname,
                  func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Teacher).filter(Teacher.teacher_name == 'Мартин Хорішко').join(Grade).join(Student) \
        .group_by(Teacher.id, Student.id).all()

    session.query(Group.group_name, Subject.subject_name, Student.id, Grade.grade, Grade.grade_date) \
        .select_from(Grade).join(Subject).filter(Subject.subject_name == 'Chemistry').join(Student) \
        .join(Group).filter(Group.group_name == 'Group B').join(Grade)\
        .order_by(desc(Grade.grade_date)).limit(1).all()
