from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

ModelBase = declarative_base()

enrollment_association = Table('enrollment_association', ModelBase.metadata,
    Column('people_id', Integer, ForeignKey('people.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id')))

class People(ModelBase):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    subjects = relationship('Subject', secondary=enrollment_association, back_populates='people')

class Subject(ModelBase):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    people = relationship('People', secondary=enrollment_association, back_populates='subjects')

db_connection = create_engine('sqlite:///education.db')
ModelBase.metadata.create_all(db_connection)
DatabaseSession = sessionmaker(bind=db_connection)
db_session = DatabaseSession()

available_subjects = [Subject(subject_name=f'Subject {i}') for i in range(1, 6)]
db_session.add_all(available_subjects)
db_session.commit()

for i in range(1, 21):
    new_person = People(full_name=f'Person {i}')
    new_person.subjects = random.sample(available_subjects, k=random.randint(1, 5))
    db_session.add(new_person)
db_session.commit()

selected_subject = db_session.query(Subject).filter_by(id=1).first()
print(f'People enrolled in {selected_subject.subject_name}:')
for enrolled_person in selected_subject.people:
    print(enrolled_person.full_name)

selected_person = db_session.query(People).filter_by(id=1).first()
print(f'Subjects for {selected_person.full_name}:')
for enrolled_subject in selected_person.subjects:
    print(enrolled_subject.subject_name)

person_to_update = db_session.query(People).filter_by(id=1).first()
person_to_update.full_name = 'Modified Person Name'
db_session.commit()

person_to_remove = db_session.query(People).filter_by(id=2).first()
db_session.delete(person_to_remove)
db_session.commit()