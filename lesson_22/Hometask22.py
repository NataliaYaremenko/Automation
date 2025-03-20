from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import random

# Базовий клас для декларативних оголошень моделей
Base = declarative_base()

# Таблиця зв'язку між студентами та курсами (багато-до-багатьох)
student_course = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Модель студента
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)  # Унікальний ідентифікатор студента
    name = Column(String)  # Ім'я студента
    # Відношення до курсів через таблицю зв'язку
    courses = relationship('Course', secondary=student_course, back_populates='students')

# Модель курсу
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)  # Унікальний ідентифікатор курсу
    title = Column(String)  # Назва курсу
    # Відношення до студентів через таблицю зв'язку
    students = relationship('Student', secondary=student_course, back_populates='courses')

# Створення двигуна бази даних SQLite
engine = create_engine('sqlite:///students.db')
# Створення всіх таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Створення 5 курсів
courses = [Course(title=f'Course {i}') for i in range(1, 6)]
session.add_all(courses)  # Додавання курсів до сесії
session.commit()  # Збереження змін у базі даних

# Створення 20 студентів та випадковий розподіл по курсах
for i in range(1, 21):
    student = Student(name=f'Student {i}')  # Створення нового студента
    # Випадкове призначення курсів студенту (від 1 до 5 курсів)
    student.courses = random.sample(courses, k=random.randint(1, 5))
    session.add(student)  # Додавання студента до сесії

session.commit()  # Збереження змін у базі даних

# Отримати всіх студентів, зареєстрованих на курс з id=1
course = session.query(Course).filter_by(id=1).first()
print(f'Students in {course.title}:')
for student in course.students:
    print(student.name)

# Отримати всі курси, на які зареєстрований студент з id=1
student = session.query(Student).filter_by(id=1).first()
print(f'Courses for {student.name}:')
for course in student.courses:
    print(course.title)

# Оновлення імені студента з id=1
student = session.query(Student).filter_by(id=1).first()
student.name = 'Updated Student Name'  # Зміна імені студента
session.commit()  # Збереження змін у базі даних

# Видалення студента з id=2
student = session.query(Student).filter_by(id=2).first()
session.delete(student)  # Видалення студента з сесії
session.commit()  # Збереження змін у базі даних
