"""
The first task of Workshop1.
"""


class Student:
    def __init__(self, name, languages_spoken, student_id, subjects):
        self.name = name
        self.languages_spoken = languages_spoken
        self.student_id = student_id
        self.subjects = subjects


class Teacher:
    def __init__(self, name, languages_spoken, started_teaching, subjects,
                 wage):
        self.name = name
        self.languages_spoken = languages_spoken
        self.started_teaching = started_teaching
        self.subjects = subjects
        self.wage = wage


class Receptionist:
    def __init__(self, name, languages_spoken, words_per_minute, wage):
        self.name = name
        self.languages_spoken = languages_spoken
        self.words_per_minute = words_per_minute
        self.wage = wage


class Dog:
    def __init__(self, name):
        self.name = name


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
