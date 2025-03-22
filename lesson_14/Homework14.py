class Student:
    def __init__(self, first_name, last_name, age, average_grade=100):
        """
        Ініціалізує об'єкт студента.
        :param first_name: Ім'я студента
        :param last_name: Прізвище студента
        :param age: Вік студента
        :param average_grade: Середній бал студента
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        """
        Змінює середній бал студента.
        :param new_grade: Нове значення середнього балу
        """
        self.average_grade = new_grade

    def tell_about_yourself(self):
        """
        Повертає інформацію про студента у зручному вигляді.
        """
        return (f"Студент: {self.first_name} {self.last_name}, Вік: {self.age}, "
                f"Середній бал: {self.average_grade}")

