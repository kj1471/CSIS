"""
The first task of Workshop1.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}."


class Human(Animal):
    def __init__(self, name, languages_spoken):
        super().__init__(name)
        self.languages_spoken = languages_spoken

    def speaks(self):
        return ", ".join(self.languages_spoken)


class Staff(Human):
    def __init__(self, name, languages_spoken, wage):
        super().__init__(name, languages_spoken)
        self.wage = wage

    def monthly_wage(self):
        return self.wage / 12


class Student(Human):
    def __init__(self, name, languages_spoken, student_id, subjects):
        super().__init__(name, languages_spoken)
        self.student_id = student_id
        self.subjects = subjects

    def greet(self):
        return f"Hello, {self.name} (id={self.student_id})."

    def studies(self):
        return ", ".join(self.subjects)


class Teacher(Staff):
    def __init__(self, name, languages_spoken, started_teaching, subjects,
                 wage):
        super().__init__(name, languages_spoken, wage)
        self.started_teaching = started_teaching
        self.subjects = subjects

    def teaches(self):
        return ", ".join(self.subjects)


class Receptionist(Staff):
    def __init__(self, name, languages_spoken, words_per_minute, wage):
        super().__init__(name, languages_spoken, wage)
        self.words_per_minute = words_per_minute


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        return f"Hello, {self.name}, who's a good dog?"


if __name__ == '__main__':
    spot = Dog("Spot")
    print(f"Have you met my dog, {spot.name}?")
    mark = Receptionist("Mark", ["English", "Arabic"], 93, 20000)
    print(f"Have you met {mark.name}, they speak {len(mark.languages_spoken)} "
          f"languages and can type {mark.words_per_minute} words per minute.")
    kieran = Student("Kieran", ["English", ], 6214,
                     ["Computing", "Physics", "Maths"])
    print(f"Have you met {kieran.name} (id={kieran.student_id}), they study"
          f" {', '.join(kieran.subjects)}.")
    lauren = Teacher("Lauren", ["English", "Spanish"], 2016, ["English", "DT"],
                     26500)
    print(f"Have you met {lauren.name}, they've been teaching since "
          f"{lauren.started_teaching}.")