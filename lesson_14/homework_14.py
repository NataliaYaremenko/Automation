#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
#Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу 
# "Студент", який дозволяє змінювати середній бал студента. 
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, middle_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.middle_score = middle_score

    def change_score(self, new_score):
        self.middle_score = new_score

    def our_student(self):
        return f"Student {self.first_name} {self.last_name} at the age {self.age} got the score {self.middle_score}."

student1 = Student("San", "Sanych", 25, 4.5)
print(student1.our_student())

student1.change_score(5)
print(student1.our_student())