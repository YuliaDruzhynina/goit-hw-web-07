from sqlalchemy import desc, func
from connect_db import session
from model import Student, Teacher, Group, Subject, Grade

if __name__ == '__main__':
    q = session.query(Student.fullname, Student.id, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id, Student.fullname).order_by(desc(Grade.grade)).limit(
        5).all()

    print(q)
